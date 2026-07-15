"""
Master scraper runner — fetches from hatla2ee (active + sold), contactcars,
yallamotor, olx_egypt, and opensooq. Merges results and writes:

  data/all_prices.json — unified price file used by the AI assessor

Schema:
  {
    "Make|Model": {
      "2024": {
        "offered": {"median": int, "p25": int, "p75": int, "n": int},
        "sold":    {"median": int, "p25": int, "p75": int, "n": int},
        "last_scraped": "YYYY-MM-DD"
      }
    }
  }

  "offered" = active asking prices from all listing sites
  "sold"    = completed/sold transactions (hatla2ee sold section)

Usage:
    python -m scrapers.run_all          # full run (all brands, all pages)
    python -m scrapers.run_all --quick  # 3 pages per brand, for testing
"""

import json
import logging
import statistics
import argparse
from pathlib import Path
from datetime import date

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

DATA_DIR = Path(__file__).parent.parent / "data"


# ─── Aggregation helpers ───────────────────────────────────────────────────────

def _aggregate(listings: list[dict]) -> dict:
    """Group listings by (make, model, year) → price stats."""
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


def _wavg_stats(sources: list[dict]) -> dict:
    total_n = sum(s["n"] for s in sources)
    if total_n == 0:
        return sources[0]
    return {
        "median": int(sum(s["median"] * s["n"] for s in sources) / total_n),
        "p25":    int(sum(s["p25"]    * s["n"] for s in sources) / total_n),
        "p75":    int(sum(s["p75"]    * s["n"] for s in sources) / total_n),
        "n":      total_n,
    }


def _merge_agg_dicts(*agg_dicts) -> dict:
    """Merge N per-source aggregated dicts into one weighted average."""
    merged: dict = {}
    for agg in agg_dicts:
        for (make, model), year_dict in agg.items():
            merged.setdefault((make, model), {})
            for year, stats in year_dict.items():
                merged[(make, model)].setdefault(year, []).append(stats)

    return {
        (make, model): {year: _wavg_stats(srcs) for year, srcs in yd.items()}
        for (make, model), yd in merged.items()
    }


def build_final(offered_agg: dict, sold_agg: dict, last_scraped: str) -> dict:
    """
    Combine offered and sold aggregates into the final JSON schema.
    {"Make|Model": {"2024": {"offered": {...}, "sold": {...}, "last_scraped": "..."}}}
    """
    all_keys: set = set(offered_agg) | set(sold_agg)
    output: dict = {}

    for (make, model) in sorted(all_keys):
        key_str = f"{make}|{model}"
        output[key_str] = {}

        offered_yd = offered_agg.get((make, model), {})
        sold_yd    = sold_agg.get((make, model), {})
        all_years  = sorted(set(offered_yd) | set(sold_yd), reverse=True)

        for year in all_years:
            year_entry: dict = {"last_scraped": last_scraped}
            if year in offered_yd:
                year_entry["offered"] = offered_yd[year]
            if year in sold_yd:
                year_entry["sold"] = sold_yd[year]
            output[key_str][str(year)] = year_entry

    return output


# ─── Main runner ──────────────────────────────────────────────────────────────

def run(quick: bool = False):
    max_pages = 3 if quick else 50
    all_offered: list[dict] = []
    all_sold:    list[dict] = []

    # ── Hatla2ee (active + sold) ───────────────────────────────────────────
    try:
        from scrapers.hatla2ee import (
            scrape_all_brands as h_scrape,
            scrape_all_brands_sold as h_scrape_sold,
            aggregate_prices as h_agg,
            save_to_json as h_save,
        )
        log.info("=== Hatla2ee (active listings) ===")
        h_active = h_scrape(max_pages=max_pages)
        all_offered.extend(h_active)
        h_save(h_agg(h_active), str(DATA_DIR / "hatla2ee_offered_prices.json"))
        log.info("Hatla2ee active: %d listings", len(h_active))

        log.info("=== Hatla2ee (sold listings) ===")
        h_sold_raw = h_scrape_sold(max_pages=max(max_pages, 10))
        all_sold.extend(h_sold_raw)
        h_save(h_agg(h_sold_raw), str(DATA_DIR / "hatla2ee_sold_prices.json"))
        log.info("Hatla2ee sold: %d listings", len(h_sold_raw))
    except Exception as e:
        log.error("Hatla2ee scraper failed: %s", e, exc_info=True)

    # ── ContactCars ────────────────────────────────────────────────────────
    try:
        from scrapers.contactcars import (
            scrape_all_brands as cc_scrape,
            aggregate_prices as cc_agg,
            save_to_json as cc_save,
        )
        log.info("=== ContactCars ===")
        cc_listings = cc_scrape(max_pages=max_pages)
        all_offered.extend(cc_listings)
        cc_save(cc_agg(cc_listings), str(DATA_DIR / "contactcars_prices.json"))
        log.info("ContactCars: %d listings", len(cc_listings))
    except Exception as e:
        log.error("ContactCars failed: %s", e)

    # ── YallaMotor ─────────────────────────────────────────────────────────
    try:
        from scrapers.yallamotor import (
            scrape_all_brands as ym_scrape,
            aggregate_prices as ym_agg,
            save_to_json as ym_save,
        )
        log.info("=== YallaMotor ===")
        ym_listings = ym_scrape(max_pages=max_pages)
        all_offered.extend(ym_listings)
        ym_save(ym_agg(ym_listings), str(DATA_DIR / "yallamotor_prices.json"))
        log.info("YallaMotor: %d listings", len(ym_listings))
    except Exception as e:
        log.error("YallaMotor failed: %s", e)

    # ── OLX Egypt ──────────────────────────────────────────────────────────
    try:
        from scrapers.olx_egypt import (
            scrape_all as olx_scrape,
            aggregate_prices as olx_agg,
            save_to_json as olx_save,
        )
        log.info("=== OLX Egypt ===")
        olx_listings = olx_scrape(max_pages=max_pages)
        all_offered.extend(olx_listings)
        olx_save(olx_agg(olx_listings), str(DATA_DIR / "olx_egypt_prices.json"))
        log.info("OLX Egypt: %d listings", len(olx_listings))
    except Exception as e:
        log.error("OLX Egypt failed: %s", e)

    # ── OpenSooq Egypt ─────────────────────────────────────────────────────
    try:
        from scrapers.opensooq import (
            scrape_all as os_scrape,
            aggregate_prices as os_agg,
            save_to_json as os_save,
        )
        log.info("=== OpenSooq Egypt ===")
        os_listings = os_scrape(max_pages=max_pages)
        all_offered.extend(os_listings)
        os_save(os_agg(os_listings), str(DATA_DIR / "opensooq_prices.json"))
        log.info("OpenSooq: %d listings", len(os_listings))
    except Exception as e:
        log.error("OpenSooq failed: %s", e)

    if not all_offered and not all_sold:
        log.error("All scrapers failed. Exiting.")
        return

    # ── Merge all offered sources, keep sold separate ──────────────────────
    log.info("Aggregating %d offered + %d sold listings...", len(all_offered), len(all_sold))

    offered_agg = _aggregate(all_offered)
    sold_agg    = _aggregate(all_sold)

    today = date.today().isoformat()
    final = build_final(offered_agg, sold_agg, today)

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATA_DIR / "all_prices.json", "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    log.info("Wrote %s", DATA_DIR / "all_prices.json")

    # Raw flat list for debugging
    with open(DATA_DIR / "raw_listings.json", "w", encoding="utf-8") as f:
        json.dump(all_offered + all_sold, f, ensure_ascii=False, indent=2)

    # ── Summary ────────────────────────────────────────────────────────────
    n_offered_entries = sum(1 for v in final.values() for yr in v.values() if "offered" in yr)
    n_sold_entries    = sum(1 for v in final.values() for yr in v.values() if "sold" in yr)

    print(f"\n{'═'*65}")
    print(f"  Raw offered listings : {len(all_offered):,}")
    print(f"  Raw sold listings    : {len(all_sold):,}")
    print(f"  Unique make/models   : {len(final):,}")
    print(f"  Year entries offered : {n_offered_entries:,}")
    print(f"  Year entries sold    : {n_sold_entries:,}")
    print(f"  Output               : {DATA_DIR / 'all_prices.json'}")
    print(f"{'═'*65}")

    # Sample: top 10 by offered count
    print("\nTop 10 by offered sample count:")
    items = []
    for key, year_dict in final.items():
        for year_str, entry in year_dict.items():
            o = entry.get("offered")
            if o:
                items.append((o["n"], key, int(year_str), entry))
    items.sort(reverse=True)
    for n, key, year, entry in items[:10]:
        o = entry["offered"]
        s = entry.get("sold")
        sold_str = f"  │  sold median={s['median']:,} n={s['n']}" if s else ""
        print(f"  {key} {year}:  offered median={o['median']:,} n={o['n']}{sold_str}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="Fast test run (3 pages/brand)")
    args = parser.parse_args()
    run(quick=args.quick)
