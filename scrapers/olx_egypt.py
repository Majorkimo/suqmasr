"""
OLX Egypt (olx.com.eg) scraper for used car listings.

Strategy: OLX Egypt embeds listing data in a Next.js __NEXT_DATA__ JSON blob
inside <script id="__NEXT_DATA__"> or falls back to HTML card parsing.
Each listing card has data-aut-id attributes and price/title/year text.

URL pattern: https://www.olx.com.eg/en/ads/Cars-Motorcycles-Boats/cars-for-sale
Pagination:  ?page=N
Brand filter: the site uses internal param IDs; we scrape all and filter by brand.
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

BASE_URL = "https://www.olx.com.eg"
CARS_URL = f"{BASE_URL}/en/ads/Cars-Motorcycles-Boats/cars-for-sale"

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

MAX_PAGES = 10


def _sleep():
    time.sleep(random.uniform(1.5, 3.0))


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


# Known make name variants on OLX Egypt
_MAKE_ALIASES = {
    "moris garage": "MG", "morris garage": "MG", "mg motor": "MG",
    "mercedes": "Mercedes-Benz", "merced": "Mercedes-Benz",
    "land rover": "Land Rover", "range rover": "Land Rover",
    "bmw": "BMW", "vw": "Volkswagen",
    "chevy": "Chevrolet", "gmc": "GMC",
    "byd": "BYD", "geely": "Geely", "chery": "Chery",
    "haval": "Haval", "great wall": "Haval",
}

_KNOWN_MAKES = [
    "Toyota", "Hyundai", "Kia", "Nissan", "Volkswagen", "Chevrolet",
    "MG", "Chery", "BYD", "Geely", "BMW", "Mercedes-Benz", "Mitsubishi",
    "Suzuki", "Peugeot", "Renault", "Fiat", "Opel", "Skoda", "BAIC",
    "Honda", "Mazda", "Ford", "Jeep", "Audi", "Porsche", "Land Rover",
    "Volvo", "Subaru", "Lexus", "Infiniti", "JAC", "JETOUR", "Haval",
    "Changan", "GAC", "Exeed", "Omoda", "JAECOO", "Soueast",
]


def _extract_make_model(title: str) -> tuple[str, str]:
    """Heuristic extraction of make and model from an OLX title string."""
    clean = title.strip()
    # Check aliases first (case-insensitive)
    for alias, canonical in _MAKE_ALIASES.items():
        if alias.lower() in clean.lower():
            # model = everything after the alias
            idx = clean.lower().find(alias.lower())
            model_raw = clean[idx + len(alias):].strip(" -–")
            model = re.sub(r"\b(19[89]\d|20[012]\d)\b", "", model_raw).strip()
            return canonical, model.title().strip() or "Unknown"

    for make in sorted(_KNOWN_MAKES, key=len, reverse=True):
        if make.lower() in clean.lower():
            idx = clean.lower().find(make.lower())
            model_raw = clean[idx + len(make):].strip(" -–")
            model = re.sub(r"\b(19[89]\d|20[012]\d)\b", "", model_raw).strip()
            return make, model.title().strip() or "Unknown"

    parts = clean.split()
    return parts[0].title() if parts else "Unknown", " ".join(parts[1:3]).title() or "Unknown"


def _parse_next_data(soup: BeautifulSoup) -> list[dict]:
    """Extract listings from Next.js __NEXT_DATA__ JSON blob."""
    script = soup.find("script", id="__NEXT_DATA__")
    if not script or not script.string:
        return []
    try:
        data = json.loads(script.string)
    except json.JSONDecodeError:
        return []

    # Navigate into the page props to find listing data
    try:
        props = data["props"]["pageProps"]
    except (KeyError, TypeError):
        return []

    # Look for ads/listings array in several possible locations
    ads = (
        props.get("ads")
        or props.get("listings")
        or props.get("data", {}).get("ads")
        or props.get("initialState", {}).get("listings", {}).get("ads")
        or []
    )

    results = []
    for ad in ads:
        try:
            price_val = None
            price_raw = ad.get("price") or ad.get("params", {}).get("price")
            if isinstance(price_raw, dict):
                price_val = _parse_price(str(price_raw.get("value", "")))
            elif price_raw:
                price_val = _parse_price(str(price_raw))

            if not price_val:
                continue

            title = ad.get("title") or ad.get("name") or ""
            year_raw = ad.get("params", {}).get("year") or ""
            year = _parse_year(str(year_raw)) or _parse_year(title)
            if not year:
                continue

            make, model = _extract_make_model(title)
            url = ad.get("url") or ""
            if url and not url.startswith("http"):
                url = BASE_URL + url

            city_obj = ad.get("location") or {}
            city = (city_obj.get("city", {}) or {}).get("name") or None

            results.append({
                "make": make,
                "model": model,
                "year": year,
                "price_egp": price_val,
                "mileage_km": None,
                "city": city,
                "transmission": None,
                "fuel_type": None,
                "condition": "used",
                "url": url,
                "source": "olx_egypt",
            })
        except Exception:
            continue

    return results


def _parse_html_cards(soup: BeautifulSoup) -> list[dict]:
    """Fallback: parse listing cards from rendered HTML."""
    results = []

    # OLX card selectors (may vary by version)
    cards = (
        soup.select("[data-aut-id='itemBox']")
        or soup.select(".EIR5N")          # OLX card class (varies)
        or soup.select("li[data-aut-id]")
        or soup.select(".listing-card")
    )

    for card in cards:
        try:
            text = card.get_text(" ", strip=True)

            # Price
            price_el = card.find(attrs={"data-aut-id": "itemPrice"}) or \
                       card.find(class_=re.compile(r"price|Price", re.I))
            price_text = price_el.get_text(" ", strip=True) if price_el else text
            price = _parse_price(price_text)
            if not price:
                continue

            # Year
            year = _parse_year(text)
            if not year:
                continue

            # Title
            title_el = card.find(attrs={"data-aut-id": "itemTitle"}) or \
                       card.find(["h2", "h3", "strong"])
            title = title_el.get_text(" ", strip=True) if title_el else text[:80]

            make, model = _extract_make_model(title)

            # URL
            link = card.find("a", href=True)
            url = None
            if link:
                href = link["href"]
                url = href if href.startswith("http") else BASE_URL + href

            results.append({
                "make": make,
                "model": model,
                "year": year,
                "price_egp": price,
                "mileage_km": None,
                "city": None,
                "transmission": None,
                "fuel_type": None,
                "condition": "used",
                "url": url,
                "source": "olx_egypt",
            })
        except Exception:
            continue

    return results


def scrape_page(page: int = 1) -> list[dict]:
    """Scrape a single page of all car listings."""
    url = CARS_URL if page == 1 else f"{CARS_URL}?page={page}"
    log.info("OLX Egypt page %d: %s", page, url)
    soup = _fetch(url)
    if not soup:
        return []

    listings = _parse_next_data(soup)
    if not listings:
        listings = _parse_html_cards(soup)

    log.info("  → %d listings on page %d", len(listings), page)
    return listings


def scrape_all(max_pages: int = MAX_PAGES) -> list[dict]:
    """Scrape all car listings from OLX Egypt across multiple pages."""
    all_listings: list[dict] = []
    seen_urls: set[str] = set()

    for page in range(1, max_pages + 1):
        page_listings = scrape_page(page)
        if not page_listings:
            log.info("OLX Egypt: no listings on page %d, stopping", page)
            break

        new_count = 0
        for item in page_listings:
            key = item.get("url") or f"{item['make']}{item['model']}{item['year']}{item['price_egp']}"
            if key in seen_urls:
                continue
            seen_urls.add(key)
            all_listings.append(item)
            new_count += 1

        log.info("OLX Egypt page %d: %d new (total %d)", page, new_count, len(all_listings))

        if new_count == 0:
            break

        if page < max_pages:
            _sleep()

    log.info("OLX Egypt total: %d listings", len(all_listings))
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
    log.info("Saved OLX Egypt prices to %s", path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    listings = scrape_all(max_pages=5)
    log.info("Total: %d listings", len(listings))
    agg = aggregate_prices(listings)
    save_to_json(agg, "data/olx_egypt_prices.json")
