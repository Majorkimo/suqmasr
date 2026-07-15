"""
Master scraper runner — fetches from hatla2ee + contactcars + yallamotor,
merges results, and writes the unified price file used by the AI assessor.

Usage:
    python -m scrapers.run_all          # full run (all brands, all pages)
    python -m scrapers.run_all --quick  # 3 pages per brand, for testing

Output:
    data/all_prices.json   — merged aggregated prices by make|model|year
    data/raw_listings.json — flat list of every individual listing scraped
"""

import json
import logging
import statistics
import argparse
from pathlib import Path

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

DATA_DIR = Path(__file__).parent.parent / "data"


def merge_price_dicts(dicts: list[dict]) -> dict:
    """
    Given N price-aggregate dicts (each keyed "Make|Model" → {year: {median, p25, p75, n}}),
    merge them by pooling the underlying sample counts and recomputing statistics.

    Since we only have summary stats (no raw prices), we take a weighted average
    for median/p25/p75 weighted by n, and sum sample counts.
    """
    merged: dict[str, dict[str, dict]] = {}

    for d in dicts:
        for key, year_dict in d.items():
            merged.setdefault(key, {})
            for year_str, stats in year_dict.items():
                if year_str not in merged[key]:
                    merged[key][year_str] = {
                        "median": stats["median"],
                        "p25": stats["p25"],
                        "p75": stats["p75"],
                        "n": stats["n"],
                        "_sources": [stats],
                    }
                else:
                    # Append source stats; recompute weighted average
                    merged[key][year_str]["_sources"].append(stats)

    # Finalise: compute weighted medians
    for key, year_dict in merged.items():
        for year_str, entry in year_dict.items():
            sources = entry.pop("_sources")
            total_n = sum(s["n"] for s in sources)
            # Weighted average of median/p25/p75
            def _wavg(field: str) -> int:
                return int(sum(s[field] * s["n"] for s in sources) / total_n)

            entry["median"] = _wavg("median")
            entry["p25"]    = _wavg("p25")
            entry["p75"]    = _wavg("p75")
            entry["n"]      = total_n

    return merged


def run(quick: bool = False):
    max_pages = 3 if quick else 50
    all_raw_listings = []
    price_dicts = []

    # ── Hatla2ee ────────────────────────────────────────────────────────────
    try:
        from scrapers.hatla2ee import scrape_all_brands as h_scrape
        from scrapers.hatla2ee import aggregate_prices as h_agg, save_to_json as h_save
        log.info("=== Running Hatla2ee scraper ===")
        h_listings = h_scrape(max_pages=max_pages)
        all_raw_listings.extend(h_listings)
        h_agg_data = h_agg(h_listings)
        h_save(h_agg_data, str(DATA_DIR / "hatla2ee_prices.json"))
        # convert tuple-keyed dict to string-keyed for merge
        price_dicts.append({
            f"{make}|{model}": {str(y): s for y, s in yd.items()}
            for (make, model), yd in h_agg_data.items()
        })
        log.info("Hatla2ee: %d listings", len(h_listings))
    except Exception as e:
        log.error("Hatla2ee scraper failed: %s", e)

    # ── ContactCars ─────────────────────────────────────────────────────────
    try:
        from scrapers.contactcars import scrape_all_brands as cc_scrape
        from scrapers.contactcars import aggregate_prices as cc_agg, save_to_json as cc_save
        log.info("=== Running ContactCars scraper ===")
        cc_listings = cc_scrape(max_pages=max_pages)
        all_raw_listings.extend(cc_listings)
        cc_agg_data = cc_agg(cc_listings)
        cc_save(cc_agg_data, str(DATA_DIR / "contactcars_prices.json"))
        price_dicts.append({
            f"{make}|{model}": {str(y): s for y, s in yd.items()}
            for (make, model), yd in cc_agg_data.items()
        })
        log.info("ContactCars: %d listings", len(cc_listings))
    except Exception as e:
        log.error("ContactCars scraper failed: %s", e)

    # ── YallaMotor ──────────────────────────────────────────────────────────
    try:
        from scrapers.yallamotor import scrape_all_brands as ym_scrape
        from scrapers.yallamotor import aggregate_prices as ym_agg, save_to_json as ym_save
        log.info("=== Running YallaMotor scraper ===")
        ym_listings = ym_scrape(max_pages=max_pages)
        all_raw_listings.extend(ym_listings)
        ym_agg_data = ym_agg(ym_listings)
        ym_save(ym_agg_data, str(DATA_DIR / "yallamotor_prices.json"))
        price_dicts.append({
            f"{make}|{model}": {str(y): s for y, s in yd.items()}
            for (make, model), yd in ym_agg_data.items()
        })
        log.info("YallaMotor: %d listings", len(ym_listings))
    except Exception as e:
        log.error("YallaMotor scraper failed: %s", e)

    if not price_dicts:
        log.error("All scrapers failed. Exiting.")
        return

    # ── Merge & save ────────────────────────────────────────────────────────
    log.info("Merging %d price datasets...", len(price_dicts))
    merged = merge_price_dicts(price_dicts)

    out_merged = DATA_DIR / "all_prices.json"
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_merged, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    log.info("Merged prices → %s  (%d models)", out_merged, len(merged))

    # Save raw flat list
    out_raw = DATA_DIR / "raw_listings.json"
    with open(out_raw, "w", encoding="utf-8") as f:
        json.dump(all_raw_listings, f, ensure_ascii=False, indent=2)
    log.info("Raw listings → %s  (%d total)", out_raw, len(all_raw_listings))

    # Print summary
    print(f"\n{'═'*60}")
    print(f"  Total raw listings  : {len(all_raw_listings):,}")
    print(f"  Make/model combos   : {len(merged):,}")
    print(f"  Output (merged)     : {out_merged}")
    print(f"{'═'*60}")

    # Sample output
    print("\nSample (top 10 by sample count):")
    items = []
    for key, year_dict in merged.items():
        for year_str, stats in year_dict.items():
            items.append((stats["n"], key, int(year_str), stats))
    items.sort(reverse=True)
    for n, key, year, stats in items[:10]:
        print(f"  {key} {year}: median={stats['median']:,} EGP, n={stats['n']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="Fast test run (3 pages/brand)")
    args = parser.parse_args()
    run(quick=args.quick)
