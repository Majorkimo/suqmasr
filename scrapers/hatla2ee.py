"""
Hatla2ee.com scraper for Egyptian used car market pricing data.

Strategy: The site is Next.js App Router with RSC streaming. Listing data is embedded
in `self.__next_f.push` scripts as a JSON-encoded `adMetrics` array containing all
listing fields (price, km, year, make/model slugs, city, transmission, fuel type, URL).

URL pattern: https://eg.hatla2ee.com/ar/car/{brand_slug}?page={n}
Returns ~40 listings per page.
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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

BASE_URL = "https://eg.hatla2ee.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ar-EG,ar;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Brand slugs as used in hatla2ee.com URLs
BRANDS = [
    "toyota",
    "hyundai",
    "kia",
    "nissan",
    "volkswagen",
    "chevrolet",
    "moris-garage",  # MG Motor (Morris Garage)
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
    "dfsk",  # Dongfeng (DFSK brand slug on hatla2ee)
    "honda",
    "mazda",
    "ford",
    "jeep",
    "audi",
    "porsche",
    "land-rover",
    "volvo",
    "subaru",
]

MAX_PAGES = 5


def _sleep():
    """Polite random sleep between requests (1-2 seconds)."""
    time.sleep(random.uniform(1.0, 2.0))


def _extract_admetrics(html: str) -> list[dict]:
    """
    Extract the adMetrics array from the RSC (React Server Components) payload.

    The page embeds listing data inside `self.__next_f.push([1,"<JSON_STRING>"])` scripts.
    The JSON string itself contains a nested `adMetrics` array with full listing details.
    """
    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script")

    for script in scripts:
        if not script.string:
            continue
        raw = script.string

        # Only process RSC push scripts that contain adMetrics
        if "adMetrics" not in raw or "__next_f" not in raw:
            continue

        # The format is: self.__next_f.push([1,"<escaped_json>"])
        match = re.match(
            r'self\.__next_f\.push\(\[1,"(.+)"\]\)$', raw, re.DOTALL
        )
        if not match:
            continue

        try:
            # json.loads on the inner string handles \" and \\ escapes
            unescaped = json.loads('"' + match.group(1) + '"')
        except (json.JSONDecodeError, ValueError):
            continue

        pos = unescaped.find('"adMetrics"')
        if pos < 0:
            continue

        # Find the opening [ of the array
        arr_start = unescaped.find("[", pos + len('"adMetrics"'))
        if arr_start < 0:
            continue

        # Walk to the matching ]
        depth = 0
        in_string = False
        escape_next = False
        arr_end = -1

        for i in range(arr_start, len(unescaped)):
            c = unescaped[i]
            if escape_next:
                escape_next = False
                continue
            if c == "\\":
                escape_next = True
                continue
            if c == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if c in ("[", "{"):
                depth += 1
            elif c in ("]", "}"):
                depth -= 1
                if depth == 0 and c == "]":
                    arr_end = i + 1
                    break

        if arr_end < 0:
            continue

        try:
            return json.loads(unescaped[arr_start:arr_end])
        except json.JSONDecodeError:
            continue

    return []


def _parse_item(item: dict) -> Optional[dict]:
    """Convert a raw adMetrics dict to a normalised listing dict."""
    try:
        price = item.get("price")
        if not price or not isinstance(price, (int, float)):
            return None

        make_obj = item.get("make") or {}
        model_obj = item.get("model") or {}
        make = make_obj.get("label") or make_obj.get("slug") or ""
        model = model_obj.get("label") or model_obj.get("slug") or ""

        if not make or not model:
            return None

        year = item.get("year")
        if not year:
            return None

        # Location: breadcrumbs[0]=district, [1]=city/governorate, [2]=Egypt
        breadcrumbs = (item.get("location") or {}).get("breadcrumbs") or []
        city = breadcrumbs[1]["title"] if len(breadcrumbs) >= 2 else None

        transmission_obj = item.get("transmission") or {}
        fuel_obj = item.get("fuel_type") or {}
        condition_obj = item.get("condition") or {}

        url = item.get("url") or item.get("url_l1") or item.get("href") or ""
        if url and not url.startswith("http"):
            url = BASE_URL + url

        return {
            "make": make.strip().title(),
            "model": model.strip().replace("-", " ").title(),
            "year": int(year),
            "price_egp": int(price),
            "mileage_km": item.get("km"),  # None for new cars
            "city": city,
            "transmission": transmission_obj.get("slug") or transmission_obj.get("label"),
            "fuel_type": fuel_obj.get("slug") or fuel_obj.get("label"),
            "condition": condition_obj.get("slug") if isinstance(condition_obj, dict) else condition_obj,
            "url": url,
            "source": "hatla2ee",
        }
    except (KeyError, TypeError, ValueError):
        return None


def scrape_brand(brand_slug: str, max_pages: int = MAX_PAGES) -> list[dict]:
    """Scrape all listings for a single brand across up to `max_pages` pages."""
    results = []
    seen_ids: set[int] = set()

    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/ar/car/{brand_slug}?page={page}"
        try:
            log.info("Fetching %s (page %d)", brand_slug, page)
            resp = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
        except requests.RequestException as exc:
            log.warning("Request failed for %s page %d: %s", brand_slug, page, exc)
            break

        if resp.status_code == 404:
            log.info("Brand %s not found (404), skipping.", brand_slug)
            break
        if resp.status_code != 200:
            log.warning("HTTP %d for %s page %d", resp.status_code, brand_slug, page)
            break

        items_raw = _extract_admetrics(resp.text)
        if not items_raw:
            log.info("No more listings for %s (page %d empty)", brand_slug, page)
            break

        new_count = 0
        for raw in items_raw:
            listing_id = raw.get("listing_id") or raw.get("id")
            if listing_id and listing_id in seen_ids:
                continue
            if listing_id:
                seen_ids.add(listing_id)
            parsed = _parse_item(raw)
            if parsed:
                results.append(parsed)
                new_count += 1

        log.info("  → %d new listings (total so far: %d)", new_count, len(results))

        # If we got fewer items than expected, this is likely the last page
        if len(items_raw) < 10:
            break

        if page < max_pages:
            _sleep()

    return results


def scrape_brand_sold(brand_slug: str, max_pages: int = MAX_PAGES) -> list[dict]:
    """
    Scrape SOLD/completed listings for a brand from hatla2ee /ar/car/sold/{slug}.
    Same RSC payload extraction as active listings; marks condition='sold'.
    """
    results = []
    seen_ids: set[int] = set()

    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/ar/car/sold/{brand_slug}?page={page}"
        try:
            log.info("Fetching SOLD %s (page %d)", brand_slug, page)
            resp = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
        except requests.RequestException as exc:
            log.warning("Request failed for sold %s page %d: %s", brand_slug, page, exc)
            break

        if resp.status_code in (404, 403):
            log.info("Sold page for %s not found (%d), skipping.", brand_slug, resp.status_code)
            break
        if resp.status_code != 200:
            log.warning("HTTP %d for sold %s page %d", resp.status_code, brand_slug, page)
            break

        items_raw = _extract_admetrics(resp.text)
        if not items_raw:
            log.info("No more sold listings for %s (page %d empty)", brand_slug, page)
            break

        new_count = 0
        for raw in items_raw:
            listing_id = raw.get("listing_id") or raw.get("id")
            if listing_id and listing_id in seen_ids:
                continue
            if listing_id:
                seen_ids.add(listing_id)
            parsed = _parse_item(raw)
            if parsed:
                parsed["condition"] = "sold"
                results.append(parsed)
                new_count += 1

        log.info("  → %d new sold listings (total so far: %d)", new_count, len(results))

        if len(items_raw) < 10:
            break
        if page < max_pages:
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
        log.info(
            "Brand '%s': collected %d listings", brand, len(brand_listings)
        )
        all_listings.extend(brand_listings)
        if brand != brands[-1]:
            _sleep()

    log.info("Total listings collected: %d", len(all_listings))
    return all_listings


def scrape_all_brands_sold(
    brands: list[str] = BRANDS, max_pages: int = MAX_PAGES
) -> list[dict]:
    """Scrape sold/completed listings for all brands."""
    all_sold: list[dict] = []
    for brand in brands:
        sold = scrape_brand_sold(brand, max_pages=max_pages)
        log.info("Sold '%s': %d listings", brand, len(sold))
        all_sold.extend(sold)
        if brand != brands[-1]:
            _sleep()
    log.info("Total sold listings: %d", len(all_sold))
    return all_sold


# ---------------------------------------------------------------------------
# Aggregation
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
    # Collect prices: {(make, model, year): [price, ...]}
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
        if len(prices) < 2:
            # Keep single-observation entries but with no p stats
            result.setdefault((make, model), {})[year] = {
                "median": prices[0],
                "p25": prices[0],
                "p75": prices[0],
                "n": 1,
            }
            continue

        sorted_prices = sorted(prices)
        n = len(sorted_prices)

        def _pct(p: float) -> float:
            idx = (p / 100) * (n - 1)
            lo, hi = int(idx), min(int(idx) + 1, n - 1)
            return sorted_prices[lo] + (sorted_prices[hi] - sorted_prices[lo]) * (idx - lo)

        p5 = _pct(5)
        p95 = _pct(95)

        filtered = [x for x in sorted_prices if p5 <= x <= p95]
        if not filtered:
            filtered = sorted_prices  # fallback: keep all if filter removes everything

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

OUTPUT_PATH = "/Users/kimo/Projects/egypt-marketplace/data/hatla2ee_prices.json"


def main():
    log.info("=== Hatla2ee scraper starting ===")
    listings = scrape_all_brands()

    if not listings:
        log.error("No listings collected. Exiting.")
        return

    log.info("Aggregating prices across %d listings...", len(listings))
    aggregated = aggregate_prices(listings)

    # Summary stats
    total_models = len(aggregated)
    total_year_entries = sum(len(v) for v in aggregated.values())
    log.info(
        "Aggregation complete: %d make/model combos, %d year-level entries",
        total_models,
        total_year_entries,
    )

    save_to_json(aggregated, OUTPUT_PATH)
    log.info("=== Done ===")

    # Print a quick sample of the output
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
