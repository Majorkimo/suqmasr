"""
OpenSooq Egypt (eg.opensooq.com) scraper for used car listings.

Strategy: OpenSooq uses server-side rendered HTML with listing cards.
Each card contains title, price, year, and location info as visible text.
Results are paginated with ?page=N.

URL pattern: https://eg.opensooq.com/en/cars?page=N
"""

import json
import os
import re
import time
import random
import statistics
import logging
from typing import Optional

import requests
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

BASE_URL = "https://eg.opensooq.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": BASE_URL,
}

# Per-brand URLs for targeted scraping
BRAND_SLUGS = {
    "Toyota": "toyota",
    "Hyundai": "hyundai",
    "Kia": "kia",
    "Nissan": "nissan",
    "Chevrolet": "chevrolet",
    "Volkswagen": "volkswagen",
    "MG": "mg",
    "Chery": "chery",
    "BYD": "byd",
    "Geely": "geely",
    "BMW": "bmw",
    "Mercedes-Benz": "mercedes-benz",
    "Mitsubishi": "mitsubishi",
    "Suzuki": "suzuki",
    "Peugeot": "peugeot",
    "Renault": "renault",
    "Fiat": "fiat",
    "Opel": "opel",
    "Skoda": "skoda",
    "BAIC": "baic",
    "Honda": "honda",
    "Mazda": "mazda",
    "Ford": "ford",
    "Jeep": "jeep",
    "Audi": "audi",
    "Land Rover": "land-rover",
    "Volvo": "volvo",
    "Subaru": "subaru",
    "Lexus": "lexus",
    "Infiniti": "infiniti",
    "JAC": "jac",
    "JETOUR": "jetour",
    "Haval": "haval",
    "Changan": "changan",
}

MAX_PAGES = 8


def _sleep():
    time.sleep(random.uniform(1.5, 2.5))


def _fetch(url: str) -> Optional[BeautifulSoup]:
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=25, allow_redirects=True)
            if r.status_code == 200:
                return BeautifulSoup(r.text, "html.parser")
            if r.status_code in (404, 403, 429):
                log.warning("HTTP %d for %s", r.status_code, url)
                return None
        except requests.RequestException as e:
            log.warning("Attempt %d failed for %s: %s", attempt + 1, url, e)
        time.sleep(2.0 * (attempt + 1))
    return None


def _parse_price(text: str) -> Optional[int]:
    digits = re.sub(r"[^\d]", "", text)
    if not digits:
        return None
    val = int(digits)
    if val < 5_000 or val > 60_000_000:
        return None
    return val


def _parse_year(text: str) -> Optional[int]:
    m = re.search(r"\b(19[89]\d|20[012]\d)\b", text)
    return int(m.group(1)) if m else None


def _parse_km(text: str) -> Optional[int]:
    m = re.search(r"([\d,]+)\s*(?:km|كم)", text, re.I)
    if m:
        return int(re.sub(r"[^\d]", "", m.group(1)))
    return None


def _extract_model_from_title(title: str, make: str) -> str:
    clean = re.sub(re.escape(make), "", title, flags=re.I).strip(" -–")
    clean = re.sub(r"\b(19[89]\d|20[012]\d)\b", "", clean).strip()
    clean = re.sub(r"\bfor sale\b|\bمعروض\b", "", clean, flags=re.I).strip()
    return clean.title().strip() or "Unknown"


def _parse_listing_card(card: BeautifulSoup, make: str) -> Optional[dict]:
    text = card.get_text(" ", strip=True)

    # Price
    price_el = card.find(class_=re.compile(r"price|سعر", re.I))
    price = _parse_price(price_el.get_text() if price_el else text)
    if not price:
        return None

    # Year
    year = _parse_year(text)
    if not year:
        return None

    # Model from title
    title_el = card.find(["h2", "h3", "h4", "strong"], class_=re.compile(r"title|name|heading", re.I))
    if not title_el:
        title_el = card.find(["h2", "h3", "h4"])
    title = title_el.get_text(" ", strip=True) if title_el else text[:100]
    model = _extract_model_from_title(title, make)

    # Mileage
    mileage = _parse_km(text)

    # URL
    link = card.find("a", href=True)
    url = None
    if link:
        href = link["href"]
        url = href if href.startswith("http") else BASE_URL + href

    # City (last breadcrumb-style element with location class)
    city_el = card.find(class_=re.compile(r"location|city|area|governorate", re.I))
    city = city_el.get_text(strip=True) if city_el else None

    return {
        "make": make,
        "model": model,
        "year": year,
        "price_egp": price,
        "mileage_km": mileage,
        "city": city,
        "transmission": None,
        "fuel_type": None,
        "condition": "used",
        "url": url,
        "source": "opensooq",
    }


def _try_json_ld(soup: BeautifulSoup, make: str) -> list[dict]:
    """Extract structured data from JSON-LD if present."""
    results = []
    for script in soup.find_all("script", type="application/ld+json"):
        if not script.string:
            continue
        try:
            data = json.loads(script.string)
        except json.JSONDecodeError:
            continue

        items = data if isinstance(data, list) else [data]
        for item in items:
            if item.get("@type") not in ("Vehicle", "Car", "Product"):
                continue
            try:
                price = _parse_price(str(item.get("offers", {}).get("price", "")))
                if not price:
                    continue
                year = _parse_year(str(item.get("vehicleModelDate") or item.get("productionDate") or ""))
                if not year:
                    continue
                model = (item.get("model") or "").strip().title()
                url = item.get("url") or ""
                results.append({
                    "make": make,
                    "model": model or "Unknown",
                    "year": year,
                    "price_egp": price,
                    "mileage_km": None,
                    "city": None,
                    "transmission": None,
                    "fuel_type": None,
                    "condition": "used",
                    "url": url,
                    "source": "opensooq",
                })
            except Exception:
                continue
    return results


def scrape_brand(make: str, brand_slug: str, max_pages: int = MAX_PAGES) -> list[dict]:
    results: list[dict] = []
    seen_urls: set[str] = set()

    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/en/cars/{brand_slug}"
        if page > 1:
            url += f"?page={page}"

        log.info("OpenSooq: %s page %d", make, page)
        soup = _fetch(url)
        if not soup:
            break

        # Try JSON-LD first
        listings = _try_json_ld(soup, make)

        # Fall back to card parsing
        if not listings:
            cards = (
                soup.select(".listing-item")
                or soup.select(".post-item")
                or soup.select("li.listing")
                or soup.select("[class*='listing']")
                or soup.select("article")
            )
            for card in cards:
                parsed = _parse_listing_card(card, make)
                if parsed:
                    listings.append(parsed)

        if not listings:
            log.info("  → no listings on page %d for %s, stopping", page, make)
            break

        new_count = 0
        for item in listings:
            key = item.get("url") or f"{item['make']}{item['model']}{item['year']}{item['price_egp']}"
            if key in seen_urls:
                continue
            seen_urls.add(key)
            results.append(item)
            new_count += 1

        log.info("  → %d new listings (total: %d)", new_count, len(results))

        if new_count == 0:
            break

        next_link = soup.find("a", rel="next") or soup.find("a", string=re.compile(r"Next|التالي", re.I))
        if not next_link:
            break

        _sleep()

    return results


def scrape_all(brand_slugs: dict = BRAND_SLUGS, max_pages: int = MAX_PAGES) -> list[dict]:
    all_listings: list[dict] = []
    for make, slug in brand_slugs.items():
        brand_listings = scrape_brand(make, slug, max_pages=max_pages)
        log.info("OpenSooq '%s': %d listings", make, len(brand_listings))
        all_listings.extend(brand_listings)
        _sleep()
    log.info("OpenSooq total: %d listings", len(all_listings))
    return all_listings


def aggregate_prices(listings: list[dict]) -> dict:
    buckets: dict = {}
    for item in listings:
        make = item.get("make", "").strip()
        model = item.get("model", "").strip()
        year = item.get("year")
        price = item.get("price_egp")
        if not (make and model and year and price and price > 0):
            continue
        key = (make, model, int(year))
        buckets.setdefault(key, []).append(int(price))

    result = {}
    for (make, model, year), prices in buckets.items():
        prices_s = sorted(prices)
        n = len(prices_s)

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
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serialisable, f, ensure_ascii=False, indent=2)
    log.info("Saved OpenSooq prices to %s", path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    listings = scrape_all(max_pages=3)
    log.info("Total: %d listings", len(listings))
    agg = aggregate_prices(listings)
    save_to_json(agg, "data/opensooq_prices.json")
