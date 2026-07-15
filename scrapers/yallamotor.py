"""
YallaMotor.com scraper for Egyptian used car market pricing data.

Strategy: YallaMotor serves paginated listing pages with standard HTML.
Listing cards contain price, year, mileage, make/model as text + data attributes.
No client-side JavaScript required (SSR).

URL pattern: https://www.yallamotor.com/used-cars/{brand}?page={n}
"""

import json
import os
import re
import time
import random
import statistics
import logging
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

BASE_URL = "https://www.yallamotor.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

BRANDS = [
    "toyota", "hyundai", "kia", "nissan", "chevrolet", "volkswagen",
    "mg", "chery", "byd", "geely", "bmw", "mercedes-benz",
    "mitsubishi", "suzuki", "peugeot", "renault", "fiat", "opel",
    "skoda", "baic", "honda", "mazda", "ford", "jeep",
    "audi", "land-rover", "volvo", "subaru", "lexus", "infiniti",
]

MAX_PAGES = 8


def _sleep():
    time.sleep(random.uniform(1.0, 2.5))


def _fetch(url: str) -> Optional[BeautifulSoup]:
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=20, allow_redirects=True)
            if r.status_code == 200:
                return BeautifulSoup(r.text, "html.parser")
            if r.status_code in (404, 403):
                return None
        except requests.RequestException as e:
            log.warning("Attempt %d failed for %s: %s", attempt + 1, url, e)
        time.sleep(1.5 * (attempt + 1))
    return None


def _parse_price(text: str) -> Optional[int]:
    """Extract integer price from strings like 'EGP 1,200,000' or '1200000 LE'."""
    digits = re.sub(r"[^\d]", "", text)
    if not digits:
        return None
    val = int(digits)
    # EGP plausibility check
    if val < 5_000 or val > 60_000_000:
        return None
    return val


def _parse_km(text: str) -> Optional[int]:
    digits = re.sub(r"[^\d]", "", text)
    return int(digits) if digits else None


def _parse_year(text: str) -> Optional[int]:
    m = re.search(r"\b(19[89]\d|20[012]\d)\b", text)
    return int(m.group(1)) if m else None


def _parse_listing_cards(soup: BeautifulSoup, brand: str) -> list[dict]:
    results = []

    # YallaMotor listing cards: .car-card, .listing-card, or article elements
    cards = (
        soup.select(".car-card")
        or soup.select(".listing-card")
        or soup.select("article.car")
        or soup.select("[data-testid='car-card']")
        or soup.select(".cars-list__item")
    )

    if not cards:
        # Generic fallback: any container with a price and year
        cards = soup.find_all("div", class_=re.compile(r"car|listing|vehicle", re.I))

    for card in cards:
        try:
            entry = _parse_single_card(card, brand)
            if entry:
                results.append(entry)
        except Exception:
            continue

    return results


def _parse_single_card(card, brand: str) -> Optional[dict]:
    text_block = card.get_text(" ", strip=True)

    # Price
    price_el = card.find(class_=re.compile(r"price|سعر", re.I))
    price_text = price_el.get_text(" ", strip=True) if price_el else text_block
    price = _parse_price(price_text)
    if not price:
        return None

    # Year
    year = _parse_year(text_block)
    if not year:
        return None

    # Model name — title/h2/h3 usually has "Brand Model Year"
    title_el = card.find(["h2", "h3", "h4"], class_=re.compile(r"title|name", re.I))
    if not title_el:
        title_el = card.find(["h2", "h3", "h4"])
    title_text = title_el.get_text(" ", strip=True) if title_el else ""

    model = _extract_model_name(title_text, brand)

    # Mileage
    km_el = card.find(string=re.compile(r"\d[\d,]+\s*km", re.I))
    mileage = _parse_km(km_el) if km_el else None

    # City
    city_el = card.find(class_=re.compile(r"location|city|area", re.I))
    city = city_el.get_text(strip=True) if city_el else None

    # URL
    link = card.find("a", href=True)
    url = None
    if link:
        href = link["href"]
        url = href if href.startswith("http") else BASE_URL + href

    return {
        "make": brand.replace("-", " ").title(),
        "model": model,
        "year": year,
        "price_egp": price,
        "mileage_km": mileage,
        "city": city,
        "transmission": None,
        "fuel_type": None,
        "condition": None,
        "url": url,
        "source": "yallamotor",
    }


def _extract_model_name(title: str, brand: str) -> str:
    # Remove brand name from title
    clean = re.sub(re.escape(brand.replace("-", " ")), "", title, flags=re.I).strip()
    # Remove year
    clean = re.sub(r"\b(19[89]\d|20[012]\d)\b", "", clean).strip()
    # Remove price-like numbers
    clean = re.sub(r"\b\d[\d,]+\b", "", clean).strip()
    return clean.title().strip() or "Unknown"


def scrape_brand(brand: str, max_pages: int = MAX_PAGES) -> list[dict]:
    results = []
    seen_urls: set[str] = set()

    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/used-cars/{brand}"
        if page > 1:
            url += f"?page={page}"

        log.info("YallaMotor: %s page %d", brand, page)
        soup = _fetch(url)
        if not soup:
            log.info("  → no page found, stopping")
            break

        cards = _parse_listing_cards(soup, brand)
        if not cards:
            log.info("  → no cards on page %d, stopping", page)
            break

        new_count = 0
        for entry in cards:
            key = entry.get("url") or f"{entry['make']}{entry['model']}{entry['year']}{entry['price_egp']}"
            if key in seen_urls:
                continue
            seen_urls.add(key)
            results.append(entry)
            new_count += 1

        log.info("  → %d new listings (total: %d)", new_count, len(results))

        # Check for next page link
        next_link = soup.find("a", rel="next") or soup.find(
            "a", string=re.compile(r"next|التالي", re.I)
        )
        if not next_link and page >= max_pages:
            break
        if not next_link:
            break

        _sleep()

    return results


def scrape_all_brands(brands: list[str] = BRANDS, max_pages: int = MAX_PAGES) -> list[dict]:
    all_listings = []
    for brand in brands:
        brand_listings = scrape_brand(brand, max_pages=max_pages)
        log.info("YallaMotor brand '%s': %d listings", brand, len(brand_listings))
        all_listings.extend(brand_listings)
        if brand != brands[-1]:
            _sleep()
    log.info("YallaMotor total: %d listings", len(all_listings))
    return all_listings


def aggregate_prices(listings: list[dict]) -> dict:
    buckets: dict = {}
    for item in listings:
        make  = item.get("make", "").strip()
        model = item.get("model", "").strip()
        year  = item.get("year")
        price = item.get("price_egp")
        if not (make and model and year and price and price > 0):
            continue
        key = (make, model, int(year))
        buckets.setdefault(key, []).append(int(price))

    result = {}
    for (make, model, year), prices in buckets.items():
        prices_s = sorted(prices)
        n = len(prices_s)
        if n == 1:
            result.setdefault((make, model), {})[year] = {
                "median": prices_s[0], "p25": prices_s[0], "p75": prices_s[0], "n": 1
            }
            continue

        def _p(pct):
            idx = pct / 100 * (n - 1)
            lo, hi = int(idx), min(int(idx) + 1, n - 1)
            return prices_s[lo] + (prices_s[hi] - prices_s[lo]) * (idx - lo)

        filtered = [x for x in prices_s if _p(5) <= x <= _p(95)] or prices_s
        nf = len(filtered)
        fs = sorted(filtered)

        def _pf(pct):
            idx = pct / 100 * (nf - 1)
            lo, hi = int(idx), min(int(idx) + 1, nf - 1)
            return int(fs[lo] + (fs[hi] - fs[lo]) * (idx - lo))

        result.setdefault((make, model), {})[year] = {
            "median": int(statistics.median(filtered)),
            "p25": _pf(25), "p75": _pf(75), "n": nf,
        }

    return result


def save_to_json(data: dict, path: str) -> None:
    serialisable = {
        f"{make}|{model}": {str(year): stats for year, stats in yd.items()}
        for (make, model), yd in data.items()
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serialisable, f, ensure_ascii=False, indent=2)
    log.info("Saved to %s", path)


OUTPUT_PATH = "/Users/kimo/Projects/egypt-marketplace/data/yallamotor_prices.json"


def main():
    log.info("=== YallaMotor scraper starting ===")
    listings = scrape_all_brands()
    if not listings:
        log.error("No listings collected.")
        return
    agg = aggregate_prices(listings)
    save_to_json(agg, OUTPUT_PATH)
    log.info("=== Done ===")


if __name__ == "__main__":
    main()
