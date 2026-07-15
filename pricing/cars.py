"""
Car price reference data for Egypt market.
Prices are in EGP for a fully-stock, good condition unit at ~50,000 km.
Updated Q1 2025 — post March 2024 devaluation.

Depreciation applied:
  - Per year (from 2025): ~12% for recent, ~8% for older
  - Per 20,000 km above 50k baseline: ~5%
  - Condition: excellent 1.10×, good 1.0×, fair 0.82×, needs_work 0.60×
"""

# {(make, model): {year: median_egp}} — good condition, ~50k km baseline
CAR_REFERENCE_PRICES: dict[tuple, dict] = {

    # ── Toyota ─────────────────────────────────────────────────────────────
    ("Toyota", "Corolla"):      {2024: 1_250_000, 2023: 1_100_000, 2022: 980_000,
                                  2021: 860_000,  2020: 750_000,  2019: 640_000,
                                  2018: 550_000,  2017: 460_000,  2016: 390_000},
    ("Toyota", "Yaris"):        {2024: 980_000,  2023: 870_000,  2022: 760_000,
                                  2021: 660_000,  2020: 570_000,  2019: 480_000,
                                  2018: 400_000,  2017: 340_000,  2016: 290_000},
    ("Toyota", "Camry"):        {2024: 2_100_000, 2023: 1_850_000, 2022: 1_620_000,
                                  2021: 1_400_000, 2020: 1_200_000, 2019: 1_020_000,
                                  2018: 850_000},
    ("Toyota", "C-HR"):         {2024: 1_600_000, 2023: 1_400_000, 2022: 1_220_000,
                                  2021: 1_050_000, 2020: 900_000,  2019: 760_000},
    ("Toyota", "RAV4"):         {2024: 2_400_000, 2023: 2_100_000, 2022: 1_850_000,
                                  2021: 1_620_000, 2020: 1_400_000, 2019: 1_180_000},
    ("Toyota", "Fortuner"):     {2024: 3_200_000, 2023: 2_800_000, 2022: 2_450_000,
                                  2021: 2_100_000, 2020: 1_800_000, 2019: 1_520_000},
    ("Toyota", "Rush"):         {2024: 1_350_000, 2023: 1_180_000, 2022: 1_020_000,
                                  2021: 870_000,  2020: 740_000},
    ("Toyota", "Hilux"):        {2024: 2_800_000, 2023: 2_450_000, 2022: 2_100_000,
                                  2021: 1_800_000, 2020: 1_550_000, 2019: 1_300_000},
    ("Toyota", "Land Cruiser"): {2024: 8_500_000, 2023: 7_500_000, 2022: 6_500_000,
                                  2021: 5_600_000, 2020: 4_800_000},

    # ── Hyundai ────────────────────────────────────────────────────────────
    ("Hyundai", "Elantra"):     {2024: 1_050_000, 2023: 920_000,  2022: 800_000,
                                  2021: 690_000,  2020: 590_000,  2019: 500_000,
                                  2018: 420_000,  2017: 350_000},
    ("Hyundai", "Tucson"):      {2024: 1_650_000, 2023: 1_450_000, 2022: 1_260_000,
                                  2021: 1_080_000, 2020: 920_000,  2019: 780_000,
                                  2018: 650_000},
    ("Hyundai", "Santa Fe"):    {2024: 2_800_000, 2023: 2_450_000, 2022: 2_100_000,
                                  2021: 1_800_000, 2020: 1_530_000},
    ("Hyundai", "Accent"):      {2024: 820_000,  2023: 720_000,  2022: 630_000,
                                  2021: 540_000,  2020: 460_000,  2019: 390_000},
    ("Hyundai", "Creta"):       {2024: 1_280_000, 2023: 1_120_000, 2022: 970_000,
                                  2021: 830_000},
    ("Hyundai", "i10"):         {2024: 620_000,  2023: 540_000,  2022: 470_000,
                                  2021: 400_000,  2020: 340_000},

    # ── Kia ────────────────────────────────────────────────────────────────
    ("Kia", "Sportage"):        {2024: 1_700_000, 2023: 1_500_000, 2022: 1_300_000,
                                  2021: 1_120_000, 2020: 960_000,  2019: 810_000,
                                  2018: 680_000},
    ("Kia", "Cerato"):          {2024: 1_050_000, 2023: 920_000,  2022: 800_000,
                                  2021: 690_000,  2020: 590_000,  2019: 500_000,
                                  2018: 420_000},
    ("Kia", "Picanto"):         {2024: 650_000,  2023: 570_000,  2022: 490_000,
                                  2021: 420_000,  2020: 360_000},
    ("Kia", "Sorento"):         {2024: 2_600_000, 2023: 2_280_000, 2022: 1_980_000,
                                  2021: 1_700_000},
    ("Kia", "Sonet"):           {2024: 980_000,  2023: 860_000,  2022: 740_000},

    # ── Nissan ─────────────────────────────────────────────────────────────
    ("Nissan", "Sunny"):        {2024: 820_000,  2023: 720_000,  2022: 630_000,
                                  2021: 540_000,  2020: 460_000,  2019: 390_000,
                                  2018: 330_000},
    ("Nissan", "Sentra"):       {2024: 980_000,  2023: 860_000,  2022: 750_000,
                                  2021: 640_000,  2020: 540_000},
    ("Nissan", "Qashqai"):      {2024: 1_550_000, 2023: 1_360_000, 2022: 1_180_000,
                                  2021: 1_010_000, 2020: 860_000,  2019: 720_000},
    ("Nissan", "X-Trail"):      {2024: 2_100_000, 2023: 1_850_000, 2022: 1_620_000,
                                  2021: 1_390_000, 2020: 1_190_000},
    ("Nissan", "Navara"):       {2024: 2_200_000, 2023: 1_930_000, 2022: 1_670_000,
                                  2021: 1_430_000},

    # ── Volkswagen ─────────────────────────────────────────────────────────
    ("Volkswagen", "Polo"):     {2024: 980_000,  2023: 860_000,  2022: 740_000,
                                  2021: 640_000,  2020: 540_000,  2019: 460_000},
    ("Volkswagen", "Tiguan"):   {2024: 2_200_000, 2023: 1_930_000, 2022: 1_680_000,
                                  2021: 1_450_000, 2020: 1_230_000},
    ("Volkswagen", "Passat"):   {2024: 1_850_000, 2023: 1_620_000, 2022: 1_400_000,
                                  2021: 1_200_000, 2020: 1_020_000},

    # ── Chevrolet ──────────────────────────────────────────────────────────
    ("Chevrolet", "Cruze"):     {2024: 780_000,  2023: 680_000,  2022: 590_000,
                                  2021: 510_000,  2020: 430_000,  2019: 360_000,
                                  2018: 300_000},
    ("Chevrolet", "Aveo"):      {2024: 560_000,  2023: 490_000,  2022: 420_000,
                                  2021: 360_000,  2020: 305_000},
    ("Chevrolet", "Captiva"):   {2024: 1_200_000, 2023: 1_050_000, 2022: 910_000,
                                  2021: 780_000,  2020: 660_000},
    ("Chevrolet", "Equinox"):   {2024: 1_650_000, 2023: 1_440_000, 2022: 1_250_000},
    ("Chevrolet", "Traverse"):  {2024: 2_800_000, 2023: 2_450_000},

    # ── MG ─────────────────────────────────────────────────────────────────
    ("MG", "ZS"):               {2024: 1_100_000, 2023: 960_000,  2022: 830_000,
                                  2021: 710_000,  2020: 600_000},
    ("MG", "5"):                {2024: 820_000,  2023: 720_000,  2022: 620_000,
                                  2021: 530_000},
    ("MG", "6"):                {2024: 1_050_000, 2023: 920_000,  2022: 790_000,
                                  2021: 680_000},
    ("MG", "RX5"):              {2024: 1_350_000, 2023: 1_180_000, 2022: 1_020_000},
    ("MG", "HS"):               {2024: 1_800_000, 2023: 1_580_000, 2022: 1_360_000},

    # ── Geely ──────────────────────────────────────────────────────────────
    ("Geely", "Emgrand"):       {2024: 750_000,  2023: 660_000,  2022: 570_000,
                                  2021: 480_000},
    ("Geely", "Coolray"):       {2024: 980_000,  2023: 860_000,  2022: 740_000,
                                  2021: 630_000},
    ("Geely", "Tugella"):       {2024: 1_650_000, 2023: 1_440_000, 2022: 1_250_000},

    # ── Mitsubishi ─────────────────────────────────────────────────────────
    ("Mitsubishi", "Eclipse Cross"): {2024: 1_550_000, 2023: 1_360_000, 2022: 1_180_000,
                                       2021: 1_010_000, 2020: 860_000},
    ("Mitsubishi", "ASX"):      {2024: 1_100_000, 2023: 960_000,  2022: 830_000,
                                  2021: 710_000},
    ("Mitsubishi", "L200"):     {2024: 2_100_000, 2023: 1_840_000, 2022: 1_600_000,
                                  2021: 1_370_000},

    # ── Skoda ──────────────────────────────────────────────────────────────
    ("Skoda", "Octavia"):       {2024: 1_450_000, 2023: 1_270_000, 2022: 1_100_000,
                                  2021: 940_000,  2020: 800_000},
    ("Skoda", "Superb"):        {2024: 2_100_000, 2023: 1_840_000, 2022: 1_600_000},
    ("Skoda", "Kodiaq"):        {2024: 2_400_000, 2023: 2_100_000, 2022: 1_820_000},
    ("Skoda", "Karoq"):         {2024: 1_650_000, 2023: 1_440_000, 2022: 1_250_000},

    # ── BYD ────────────────────────────────────────────────────────────────
    ("BYD", "Seal"):            {2024: 1_850_000, 2023: 1_620_000},
    ("BYD", "Atto 3"):          {2024: 1_650_000, 2023: 1_440_000},
    ("BYD", "Song Plus"):       {2024: 1_400_000, 2023: 1_220_000},
    ("BYD", "Dolphin"):         {2024: 1_100_000, 2023: 960_000},

    # ── Renault ────────────────────────────────────────────────────────────
    ("Renault", "Duster"):      {2024: 950_000,  2023: 830_000,  2022: 720_000,
                                  2021: 610_000,  2020: 520_000,  2019: 440_000},
    ("Renault", "Symbol"):      {2024: 620_000,  2023: 540_000,  2022: 470_000,
                                  2021: 400_000,  2020: 340_000},

    # ── Peugeot ────────────────────────────────────────────────────────────
    ("Peugeot", "208"):         {2024: 850_000,  2023: 740_000,  2022: 640_000,
                                  2021: 550_000},
    ("Peugeot", "3008"):        {2024: 1_800_000, 2023: 1_580_000, 2022: 1_370_000,
                                  2021: 1_170_000},
    ("Peugeot", "2008"):        {2024: 1_200_000, 2023: 1_050_000, 2022: 910_000},
    ("Peugeot", "508"):         {2024: 1_850_000, 2023: 1_620_000, 2022: 1_400_000},

    # ── BAIC ───────────────────────────────────────────────────────────────
    ("BAIC", "X35"):            {2024: 680_000,  2023: 595_000,  2022: 515_000},
    ("BAIC", "X55"):            {2024: 950_000,  2023: 830_000,  2022: 720_000},
    ("BAIC", "EU5"):            {2024: 780_000,  2023: 680_000},

    # ── Fiat ───────────────────────────────────────────────────────────────
    ("Fiat", "Tipo"):           {2024: 650_000,  2023: 570_000,  2022: 490_000,
                                  2021: 420_000,  2020: 355_000},
    ("Fiat", "500X"):           {2024: 1_100_000, 2023: 960_000,  2022: 830_000},

    # ── Jeep ───────────────────────────────────────────────────────────────
    ("Jeep", "Wrangler"):       {2024: 5_500_000, 2023: 4_800_000, 2022: 4_100_000,
                                  2021: 3_500_000},
    ("Jeep", "Grand Cherokee"): {2024: 4_200_000, 2023: 3_700_000, 2022: 3_200_000},
    ("Jeep", "Compass"):        {2024: 2_100_000, 2023: 1_840_000, 2022: 1_600_000},

    # ── BMW ────────────────────────────────────────────────────────────────
    ("BMW", "3 Series"):        {2024: 4_200_000, 2023: 3_700_000, 2022: 3_200_000,
                                  2021: 2_750_000, 2020: 2_350_000},
    ("BMW", "5 Series"):        {2024: 6_500_000, 2023: 5_700_000, 2022: 4_950_000,
                                  2021: 4_250_000},
    ("BMW", "X5"):              {2024: 9_500_000, 2023: 8_300_000, 2022: 7_200_000},

    # ── Mercedes ───────────────────────────────────────────────────────────
    ("Mercedes-Benz", "C-Class"):    {2024: 5_500_000, 2023: 4_800_000, 2022: 4_150_000,
                                  2021: 3_550_000, 2020: 3_000_000},
    ("Mercedes-Benz", "E-Class"):    {2024: 8_500_000, 2023: 7_500_000, 2022: 6_500_000,
                                  2021: 5_600_000},
    ("Mercedes-Benz", "GLC"):        {2024: 9_000_000, 2023: 7_900_000, 2022: 6_850_000},
}

CONDITION_FACTORS = {
    "excellent":  1.10,
    "good":       1.00,
    "fair":       0.82,
    "needs_work": 0.60,
}

MILEAGE_BASELINE = 50_000   # km — reference point for CAR_REFERENCE_PRICES
MILEAGE_PENALTY  = 0.05     # 5% per 20,000 km above baseline


# ── Scraped live-market data ───────────────────────────────────────────────────
# Loaded on first access from data/all_prices.json (output of run_all.py scraper).
#
# New schema (run_all.py v2):
#   {"Make|Model": {"2024": {"offered": {median,p25,p75,n}, "sold": {...}, "last_scraped": "..."}}}
# Legacy schema (v1, backward-compat):
#   {"Make|Model": {"2024": {"median": int, "p25": int, "p75": int, "n": int}}}

import json as _json
import os as _os
from pathlib import Path as _Path

_SCRAPED_PRICES: dict | None = None


def _load_scraped() -> dict:
    global _SCRAPED_PRICES
    if _SCRAPED_PRICES is not None:
        return _SCRAPED_PRICES
    data_file = _Path(_os.path.dirname(_os.path.dirname(__file__))) / "data" / "all_prices.json"
    if data_file.exists():
        try:
            with open(data_file, encoding="utf-8") as f:
                _SCRAPED_PRICES = _json.load(f)
        except Exception:
            _SCRAPED_PRICES = {}
    else:
        _SCRAPED_PRICES = {}
    return _SCRAPED_PRICES


def _entry_stats(entry: dict, prefer: str = "sold") -> dict | None:
    """
    Extract stat dict from a year entry, handling both schema versions.

    New schema: entry has "offered" and/or "sold" keys.
    Old schema: entry has "median"/"p25"/"p75"/"n" directly.

    prefer = "sold"    → use sold if available, else offered
    prefer = "offered" → always use offered stats
    """
    if entry is None:
        return None
    # New schema
    if "offered" in entry or "sold" in entry:
        if prefer == "sold" and "sold" in entry and entry["sold"].get("n", 0) >= 2:
            return entry["sold"]
        if "offered" in entry and entry["offered"].get("n", 0) >= 1:
            return entry["offered"]
        # Fall back to sold even if n==1
        return entry.get("sold") or entry.get("offered")
    # Old / legacy schema — flat stats dict
    if "median" in entry:
        return entry
    return None


def _scraped_price_detail(make: str, model: str, year: int) -> dict | None:
    """
    Return a dict with offered_median, sold_median, offered_n, sold_n
    for this make/model/year (or nearby year), or None if no data.
    """
    data = _load_scraped()
    key = f"{make}|{model}"
    year_dict = data.get(key, {})

    def _extract(yr: int) -> dict | None:
        entry = year_dict.get(str(yr))
        if not entry:
            return None
        # New schema
        if "offered" in entry or "sold" in entry:
            offered = entry.get("offered")
            sold    = entry.get("sold")
            if (offered and offered.get("n", 0) >= 1) or (sold and sold.get("n", 0) >= 1):
                return {"offered": offered, "sold": sold, "year_used": yr}
        # Legacy flat schema
        elif "median" in entry and entry.get("n", 0) >= 2:
            return {"offered": entry, "sold": None, "year_used": yr}
        return None

    result = _extract(year)
    if result:
        return result

    # Try nearby years with depreciation penalty
    for offset in (1, -1, 2, -2):
        result = _extract(year + offset)
        if result:
            factor = 0.88 ** abs(offset)
            if result.get("offered"):
                o = result["offered"]
                result["offered"] = {
                    "median": int(o["median"] * factor),
                    "p25":    int(o["p25"]    * factor),
                    "p75":    int(o["p75"]    * factor),
                    "n":      o["n"],
                }
            if result.get("sold"):
                s = result["sold"]
                result["sold"] = {
                    "median": int(s["median"] * factor),
                    "p25":    int(s["p25"]    * factor),
                    "p75":    int(s["p75"]    * factor),
                    "n":      s["n"],
                }
            return result

    return None


def _scraped_price(make: str, model: str, year: int) -> int | None:
    """
    Return best available scraped median EGP (sold preferred, else offered).
    """
    detail = _scraped_price_detail(make, model, year)
    if not detail:
        return None
    # Prefer sold price (actual transaction) with n >= 2
    sold = detail.get("sold")
    if sold and sold.get("n", 0) >= 2:
        return sold["median"]
    offered = detail.get("offered")
    if offered and offered.get("n", 0) >= 1:
        return offered["median"]
    return None


def get_car_market_price(make: str, model: str, year: int,
                          mileage_km: int = 50_000,
                          condition: str = "good") -> dict | None:
    """
    Return estimated market price for a car.

    Priority:
      1. Live scraped sold price    (actual transactions — most accurate)
      2. Live scraped offered price (active asking prices)
      3. Static reference table     (fallback if no scraped data)

    Returns None if make/model/year is completely unknown.
    Also returns offered_price and sold_price separately for UI display.
    """
    # 1 + 2. Try live scraped data (returns both offered & sold)
    detail = _scraped_price_detail(make, model, year)

    sold_stats    = detail.get("sold")    if detail else None
    offered_stats = detail.get("offered") if detail else None

    # Choose base price: sold (n≥2) → offered (n≥1) → static
    if sold_stats and sold_stats.get("n", 0) >= 2:
        base_price = sold_stats["median"]
        basis = "scraped_sold"
    elif offered_stats and offered_stats.get("n", 0) >= 1:
        base_price = offered_stats["median"]
        basis = "scraped_offered"
    else:
        ref = CAR_REFERENCE_PRICES.get((make, model))
        if not ref:
            return None
        base_price = ref.get(year)
        if base_price is None:
            years = sorted(ref.keys())
            closest = min(years, key=lambda y: abs(y - year))
            base_price = ref[closest]
            year_gap = abs(closest - year)
            if year_gap > 0:
                base_price = int(base_price * (0.88 ** year_gap))
        basis = "reference"
        sold_stats    = None
        offered_stats = None

    # Mileage adjustment
    km_diff = max(0, mileage_km - MILEAGE_BASELINE)
    km_buckets = km_diff / 20_000
    mileage_factor = max(0.40, 1.0 - (km_buckets * MILEAGE_PENALTY))

    # Condition
    cond_factor = CONDITION_FACTORS.get(condition, 1.0)

    market_price = int(base_price * mileage_factor * cond_factor)

    # Raw offered / sold medians (before mileage/condition adjustment)
    offered_raw = offered_stats["median"] if offered_stats else None
    sold_raw    = sold_stats["median"]    if sold_stats    else None

    return {
        "market_price":     market_price,
        "base_price":       base_price,
        "basis":            basis,
        "mileage_factor":   round(mileage_factor, 3),
        "condition_factor": cond_factor,
        # Live market insight (unadjusted medians, for UI display)
        "offered_price":    offered_raw,
        "offered_n":        offered_stats["n"] if offered_stats else None,
        "offered_p25":      offered_stats["p25"] if offered_stats else None,
        "offered_p75":      offered_stats["p75"] if offered_stats else None,
        "sold_price":       sold_raw,
        "sold_n":           sold_stats["n"] if sold_stats else None,
        "sold_p25":         sold_stats["p25"] if sold_stats else None,
        "sold_p75":         sold_stats["p75"] if sold_stats else None,
    }


def score_car_asking(asking_price: int, market_price: int) -> dict:
    ratio = asking_price / market_price
    if ratio <= 0.82:
        verdict, label = "deal",      "Great Deal"
    elif ratio <= 0.94:
        verdict, label = "fair",      "Good Price"
    elif ratio <= 1.06:
        verdict, label = "fair",      "Fair Market Price"
    elif ratio <= 1.18:
        verdict, label = "above",     "Above Market"
    else:
        verdict, label = "overpriced","Overpriced"

    pct = round((ratio - 1) * 100, 1)
    return {
        "verdict":       verdict,
        "label":         label,
        "pct_vs_market": pct,
        "market_price":  market_price,
        "ratio":         round(ratio, 3),
    }


def _all_makes() -> list[str]:
    """Union of static reference table + catalog makes."""
    static = set(k[0] for k in CAR_REFERENCE_PRICES)
    try:
        from pricing.egypt_car_catalog import CATALOG
        catalog = set(CATALOG.keys())
    except ImportError:
        catalog = set()
    return sorted(static | catalog)

CAR_MAKES = _all_makes()


def get_models_for_make(make: str) -> list[str]:
    """Return all known models for a make (static + scraped + catalog)."""
    static_models = {m for (mk, m) in CAR_REFERENCE_PRICES if mk == make}

    # Include scraped models
    scraped = _load_scraped()
    scraped_models = {
        key.split("|", 1)[1]
        for key in scraped
        if key.startswith(f"{make}|")
    }

    # Include catalog models
    try:
        from pricing.egypt_car_catalog import CATALOG
        catalog_models = set(CATALOG.get(make, {}).keys())
    except ImportError:
        catalog_models = set()

    return sorted(static_models | scraped_models | catalog_models)


def get_car_info(make: str, model: str) -> dict | None:
    """Return catalog entry for a make/model if available."""
    try:
        from pricing.egypt_car_catalog import get_model_info
        return get_model_info(make, model)
    except ImportError:
        return None
