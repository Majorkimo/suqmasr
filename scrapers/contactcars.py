"""
ContactCars.com scraper for Egyptian used car market pricing data.

Strategy: The site is Next.js App Router. Listing data is embedded as a
JSON-LD `application/ld+json` script containing an array of schema.org Vehicle
objects, each with price, mileage, brand, model, year, and URL.

URL patterns:
  - Brand page:  https://www.contactcars.com/ar/used-cars/{brand_slug}
  - Model page:  https://www.contactcars.com/ar/used-cars/{brand_slug}-{model_slug}

Each page yields up to 25 listings. Model-specific pages are discovered by parsing
the brand page for model links. This maximises coverage without requiring
client-side JS execution.
"""

import json
import os
import re
import time
import random
import statistics
import logging
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

BASE_URL = "https://www.contactcars.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ar-EG,ar;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Brand slugs as used in contactcars.com /ar/used-cars/{slug} URLs
BRANDS = [
    "toyota",
    "hyundai",
    "kia",
    "nissan",
    "volkswagen",
    "chevrolet",
    "mg",
    "chery",
    "byd",
    "geely",
    "bmw",
    "mercedes",
    "mitsubishi",
    "suzuki",
    "peugeot",
    "renault",
    "fiat",
    "opel",
    "skoda",
    "baic",
    "dongfeng",
    "honda",
    "mazda",
    "ford",
    "jeep",
    "audi",
    "porsche",
    "land_rover",
    "volvo",
    "subaru",
]

MAX_PAGES = 5


def _sleep():
    """Polite random sleep between requests (1-2 seconds)."""
    time.sleep(random.uniform(1.0, 2.0))


def _extract_vehicles_from_html(html: str) -> list[dict]:
    """
    Extract Vehicle listings from JSON-LD scripts embedded in the page.

    ContactCars embeds an `application/ld+json` array of schema.org Vehicle objects
    for each listing on the page (typically script index 2, but we search all scripts).
    """
    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        if not script.string:
            continue
        try:
            data = json.loads(script.string)
        except (json.JSONDecodeError, ValueError):
            continue

        if isinstance(data, list) and data and data[0].get("@type") == "Vehicle":
            return data

    return []


def _parse_vehicle(v: dict) -> Optional[dict]:
    """Convert a schema.org Vehicle dict to a normalised listing dict."""
    try:
        offers = v.get("offers") or {}
        price = offers.get("price")
        if not price or not isinstance(price, (int, float)):
            return None

        brand_obj = v.get("brand") or {}
        make = brand_obj.get("name", "").strip()
        model = (v.get("model") or "").strip()
        year = v.get("vehicleModelDate") or v.get("productionDate")

        if not (make and model and year):
            return None

        mileage_obj = v.get("mileageFromOdometer") or {}
        mileage_km = mileage_obj.get("value")  # already in km (unitCode: KMT)

        item_condition = v.get("itemCondition", "")
        condition = "used" if "Used" in item_condition else "new" if "New" in item_condition else None

        url = v.get("url") or ""

        # Transmission and fuel type are not in the JSON-LD schema.org data;
        # they would require fetching each listing detail page.
        # vehicleConfiguration holds the trim string (e.g. "1.6 A/T Feel").
        config = v.get("vehicleConfiguration") or ""
        transmission = None
        if " A/T" in config or "/AT" in config.upper():
            transmission = "automatic"
        elif " M/T" in config or "/MT" in config.upper() or "Manual" in config:
            transmission = "manual"

        return {
            "make": make.title(),
            "model": model.title(),
            "year": int(year),
            "price_egp": int(price),
            "mileage_km": int(mileage_km) if mileage_km is not None else None,
            "city": None,  # ContactCars JSON-LD does not expose city
            "transmission": transmission,
            "fuel_type": None,  # Not available in JSON-LD
            "condition": condition,
            "url": url,
            "source": "contactcars",
        }
    except (KeyError, TypeError, ValueError):
        return None


def _get_model_urls(brand_slug: str) -> list[str]:
    """
    Fetch the brand page and extract individual model URLs.

    ContactCars exposes per-model links on the brand listing page,
    e.g. /ar/used-cars/toyota-corolla, /ar/used-cars/toyota-fortuner, ...
    """
    url = f"{BASE_URL}/ar/used-cars/{brand_slug}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
    except requests.RequestException as exc:
        log.warning("Failed to fetch brand page %s: %s", url, exc)
        return []

    if resp.status_code != 200:
        log.warning("HTTP %d for brand page %s", resp.status_code, url)
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    model_urls = []
    prefix = f"/ar/used-cars/{brand_slug}-"

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(prefix) and href not in model_urls:
            model_urls.append(href)

    # Also include the brand-level URL itself
    brand_path = f"/ar/used-cars/{brand_slug}"
    all_urls = [brand_path] + model_urls
    return list(dict.fromkeys(all_urls))  # deduplicate while preserving order


def scrape_brand(brand_slug: str, max_pages: int = MAX_PAGES) -> list[dict]:
    """
    Scrape all listings for a brand by:
    1. Fetching the brand page and discovering model URLs.
    2. Fetching each model URL (25 listings per page, no working server-side pagination).
    """
    results: list[dict] = []
    seen_urls: set[str] = set()

    log.info("Discovering model URLs for brand '%s'", brand_slug)
    paths = _get_model_urls(brand_slug)
    _sleep()

    if not paths:
        log.info("No paths found for '%s'", brand_slug)
        return results

    log.info("Found %d paths for '%s'", len(paths), brand_slug)

    for path in paths:
        full_url = BASE_URL + path
        try:
            log.info("  Fetching %s", full_url)
            resp = requests.get(full_url, headers=HEADERS, timeout=30, allow_redirects=True)
        except requests.RequestException as exc:
            log.warning("  Request failed: %s", exc)
            _sleep()
            continue

        if resp.status_code != 200:
            log.warning("  HTTP %d for %s", resp.status_code, full_url)
            _sleep()
            continue

        vehicles_raw = _extract_vehicles_from_html(resp.text)
        if not vehicles_raw:
            log.info("  No vehicles found on %s", full_url)
            _sleep()
            continue

        new_count = 0
        for v in vehicles_raw:
            listing_url = v.get("url", "")
            if listing_url and listing_url in seen_urls:
                continue
            if listing_url:
                seen_urls.add(listing_url)
            parsed = _parse_vehicle(v)
            if parsed:
                results.append(parsed)
                new_count += 1

        log.info("  → %d new listings (total: %d)", new_count, len(results))
        _sleep()

    return results


def scrape_all_brands(
    brands: list[str] = BRANDS, max_pages: int = MAX_PAGES
) -> list[dict]:
    """
    Scrape all brands and return a flat list of listing dicts.

    Each dict has: make, model, year, price_egp, mileage_km, city,
                   transmission, fuel_type, condition, url, source
    """
    all_listings: list[dict] = []

    for brand in brands:
        brand_listings = scrape_brand(brand, max_pages=max_pages)
        log.info("Brand '%s': collected %d listings", brand, len(brand_listings))
        all_listings.extend(brand_listings)
        if brand != brands[-1]:
            _sleep()

    log.info("Total listings collected: %d", len(all_listings))
    return all_listings


# ---------------------------------------------------------------------------
# Aggregation (same logic as hatla2ee.py)
# ---------------------------------------------------------------------------

def aggregate_prices(
    listings: list[dict],
) -> dict[tuple[str, str], dict[int, dict]]:
    """
    Group listings by (make, model) → year → price statistics.

    Outlier filtering: drop prices below p5 or above p95 within each group,
    then compute median, p25, p75, and sample count.

    Returns:
        {
            (make, model): {
                year: {"median": int, "p25": int, "p75": int, "n": int}
            }
        }
    """
    buckets: dict[tuple[str, str, int], list[int]] = {}

    for listing in listings:
        make = listing.get("make", "").strip()
        model = listing.get("model", "").strip()
        year = listing.get("year")
        price = listing.get("price_egp")

        if not (make and model and year and price and price > 0):
            continue

        key = (make, model, int(year))
        buckets.setdefault(key, []).append(int(price))

    result: dict[tuple[str, str], dict[int, dict]] = {}

    for (make, model, year), prices in buckets.items():
        sorted_prices = sorted(prices)
        n = len(sorted_prices)

        if n == 1:
            result.setdefault((make, model), {})[year] = {
                "median": sorted_prices[0],
                "p25": sorted_prices[0],
                "p75": sorted_prices[0],
                "n": 1,
            }
            continue

        def _pct(p: float) -> float:
            idx = (p / 100) * (n - 1)
            lo, hi = int(idx), min(int(idx) + 1, n - 1)
            return sorted_prices[lo] + (sorted_prices[hi] - sorted_prices[lo]) * (idx - lo)

        p5 = _pct(5)
        p95 = _pct(95)

        filtered = [x for x in sorted_prices if p5 <= x <= p95]
        if not filtered:
            filtered = sorted_prices

        nf = len(filtered)
        filtered_sorted = sorted(filtered)

        def _pct_f(p: float) -> int:
            idx = (p / 100) * (nf - 1)
            lo, hi = int(idx), min(int(idx) + 1, nf - 1)
            return int(
                filtered_sorted[lo]
                + (filtered_sorted[hi] - filtered_sorted[lo]) * (idx - lo)
            )

        median = int(statistics.median(filtered))
        p25 = _pct_f(25)
        p75 = _pct_f(75)

        result.setdefault((make, model), {})[year] = {
            "median": median,
            "p25": p25,
            "p75": p75,
            "n": nf,
        }

    return result


def save_to_json(data: dict[tuple[str, str], dict[int, dict]], path: str) -> None:
    """
    Serialise the aggregated price dict to JSON.

    Keys are converted from tuple to "Make|Model" strings for JSON compatibility.
    """
    serialisable = {
        f"{make}|{model}": {str(year): stats for year, stats in year_dict.items()}
        for (make, model), year_dict in data.items()
    }

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serialisable, f, ensure_ascii=False, indent=2)

    log.info("Saved aggregated prices to %s", path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

OUTPUT_PATH = "/Users/kimo/Projects/egypt-marketplace/data/contactcars_prices.json"


def main():
    log.info("=== ContactCars scraper starting ===")
    listings = scrape_all_brands()

    if not listings:
        log.error("No listings collected. Exiting.")
        return

    log.info("Aggregating prices across %d listings...", len(listings))
    aggregated = aggregate_prices(listings)

    total_models = len(aggregated)
    total_year_entries = sum(len(v) for v in aggregated.values())
    log.info(
        "Aggregation complete: %d make/model combos, %d year-level entries",
        total_models,
        total_year_entries,
    )

    save_to_json(aggregated, OUTPUT_PATH)
    log.info("=== Done ===")

    print("\n--- Sample output (first 5 make/model/year entries) ---")
    count = 0
    for (make, model), year_dict in sorted(aggregated.items()):
        for year, stats in sorted(year_dict.items(), reverse=True):
            print(
                f"  {make} {model} {year}: "
                f"median={stats['median']:,} EGP, "
                f"p25={stats['p25']:,}, p75={stats['p75']:,}, n={stats['n']}"
            )
            count += 1
            if count >= 5:
                break
        if count >= 5:
            break


if __name__ == "__main__":
    main()
