"""
reference_prices.py — Knowledge-based compound price benchmarks (Egypt real estate).

These are researched median resale prices (EGP/m², fully finished apartment baseline)
as of Q4 2024 / Q1 2025.  They serve as the primary prior when live scraped data or
the historical DB are sparse.

Priority in build_compound_report():
  1. Live market data (current scrape, n ≥ 5)
  2. Historical DB snapshot for this compound + area
  3. Reference price here          ← this file
  4. Tier × area-median estimate   ← last resort

Structure: {compound_label: {"p25": int, "median": int, "p75": int}}
All prices are EGP/m², normalized to fully-finished apartments.
For villas multiply by ~1.4–1.8 (not applied here — villa searches are separate).
"""

REFERENCE_PRICES: dict[str, dict] = {

    # ══════════════════════════════════════════════════════════════════
    # 6TH OF OCTOBER CITY
    # ══════════════════════════════════════════════════════════════════

    # ── South October — Premium belt (Al Wahat / Desert Road) ────────
    # Flagship compounds from Palm Hills, Mountain View, Emaar
    "O West (Palm Hills)":             {"p25":  42_000, "median":  55_000, "p75":  68_000},
    "Badya (Palm Hills)":              {"p25":  38_000, "median":  52_000, "p75":  65_000},
    "Palm Hills WoodVille":            {"p25":  40_000, "median":  53_000, "p75":  66_000},
    "Palm Parks (Palm Hills)":         {"p25":  40_000, "median":  53_000, "p75":  66_000},
    "Joulz (Emaar)":                   {"p25":  45_000, "median":  60_000, "p75":  78_000},
    "Mountain View iCity October":     {"p25":  40_000, "median":  55_000, "p75":  70_000},
    "Mountain View 4":                 {"p25":  36_000, "median":  48_000, "p75":  62_000},
    "Mountain View Chillout Park":     {"p25":  36_000, "median":  47_000, "p75":  60_000},
    "New Giza":                        {"p25":  55_000, "median":  72_000, "p75":  92_000},
    "Soleya":                          {"p25":  28_000, "median":  40_000, "p75":  52_000},
    "Beverly Hills October":           {"p25":  32_000, "median":  44_000, "p75":  58_000},

    # ── Central October — Mid belt (26th July Corridor) ───────────────
    "Mountain View October Park":      {"p25":  35_000, "median":  48_000, "p75":  62_000},
    "Swan Lake West":                  {"p25":  35_000, "median":  46_000, "p75":  58_000},
    "Swan Lake October":               {"p25":  32_000, "median":  43_000, "p75":  55_000},
    "Keeva (Al Ahly Sabbour)":         {"p25":  30_000, "median":  41_000, "p75":  53_000},
    "Grand Heights":                   {"p25":  32_000, "median":  45_000, "p75":  58_000},

    # ── North October — Affordable (old/government districts) ─────────
    # Prices updated Q1 2025 after March 2024 EGP devaluation (~1.6× uplift on older stock).
    # These are decades-old government-subsidised compounds — cheaper than premium belts
    # but no longer as cheap as pre-devaluation figures.
    "ECO West":                        {"p25":  22_000, "median":  30_000, "p75":  40_000},
    "Sun Capital":                     {"p25":  20_000, "median":  28_000, "p75":  38_000},
    "Green IV (Mabany Edrees)":        {"p25":  18_000, "median":  25_000, "p75":  34_000},
    "Beit Alwatan":                    {"p25":  16_000, "median":  22_000, "p75":  30_000},
    "ABHA":                            {"p25":  18_000, "median":  24_000, "p75":  32_000},
    "Al Karma 4":                      {"p25":  15_000, "median":  21_000, "p75":  28_000},
    "Dar Misr":                        {"p25":  14_000, "median":  19_000, "p75":  26_000},

    # ══════════════════════════════════════════════════════════════════
    # NEW CAIRO / 5TH SETTLEMENT
    # ══════════════════════════════════════════════════════════════════

    # ── Golden Square / 5th Settlement — Ultra-premium belt ──────────
    "Mivida (Emaar)":                  {"p25":  72_000, "median":  95_000, "p75": 125_000},
    "Katameya Heights":                {"p25":  70_000, "median":  92_000, "p75": 120_000},
    "Eastown (Sodic)":                 {"p25":  65_000, "median":  87_000, "p75": 115_000},
    "Hyde Park":                       {"p25":  62_000, "median":  84_000, "p75": 112_000},
    "Palm Hills New Cairo":            {"p25":  58_000, "median":  76_000, "p75": 100_000},
    "Mountain View iCity":             {"p25":  55_000, "median":  74_000, "p75":  97_000},
    "Mountain View Hyde Park":         {"p25":  53_000, "median":  71_000, "p75":  93_000},
    "Swan Lake New Cairo":             {"p25":  52_000, "median":  70_000, "p75":  92_000},
    "Katameya Dunes":                  {"p25":  50_000, "median":  67_000, "p75":  88_000},
    "La Vista New Cairo":              {"p25":  48_000, "median":  65_000, "p75":  86_000},
    "Aliva (Mountain View)":           {"p25":  42_000, "median":  58_000, "p75":  76_000},

    # ── 3rd Settlement / North New Cairo — Mid tier ───────────────────
    "City Gate (Sapphire)":            {"p25":  38_000, "median":  52_000, "p75":  68_000},
    "Marasem / Fifth Square":          {"p25":  36_000, "median":  50_000, "p75":  65_000},
    "Capital Gardens":                 {"p25":  28_000, "median":  40_000, "p75":  53_000},
    "Taj City":                        {"p25":  26_000, "median":  38_000, "p75":  50_000},
    "The Square (Sabbour)":            {"p25":  25_000, "median":  37_000, "p75":  49_000},
    "Trio Gardens":                    {"p25":  24_000, "median":  35_000, "p75":  47_000},
    "Lake Park":                       {"p25":  24_000, "median":  35_000, "p75":  46_000},
    "Beit Al Watan":                   {"p25":  16_000, "median":  23_000, "p75":  31_000},

    # ── Mostakbal / East — Emerging ───────────────────────────────────
    "Sarai (Madinet Masr)":            {"p25":  32_000, "median":  46_000, "p75":  62_000},
    "Azha":                            {"p25":  30_000, "median":  43_000, "p75":  57_000},
    "Cairo Gate":                      {"p25":  30_000, "median":  43_000, "p75":  57_000},
    "Arabella":                        {"p25":  22_000, "median":  33_000, "p75":  44_000},

    # ══════════════════════════════════════════════════════════════════
    # SHEIKH ZAYED
    # ══════════════════════════════════════════════════════════════════

    # ── Premium Belt ─────────────────────────────────────────────────
    "Palm Hills Golf Extension":       {"p25":  44_000, "median":  60_000, "p75":  78_000},
    "Palm Hills October":              {"p25":  40_000, "median":  55_000, "p75":  72_000},
    "Allegria (Sodic)":                {"p25":  42_000, "median":  58_000, "p75":  76_000},
    "Westown (Sodic)":                 {"p25":  38_000, "median":  53_000, "p75":  70_000},
    "ZED West":                        {"p25":  33_000, "median":  47_000, "p75":  62_000},
    "ZED Sheikh Zayed":                {"p25":  32_000, "median":  45_000, "p75":  60_000},
    "Beverly Hills":                   {"p25":  32_000, "median":  46_000, "p75":  61_000},
    "Sodic West":                      {"p25":  30_000, "median":  44_000, "p75":  58_000},

    # ── Mid Belt ─────────────────────────────────────────────────────
    "El Rabwa":                        {"p25":  26_000, "median":  38_000, "p75":  51_000},
    "Mirage City":                     {"p25":  22_000, "median":  32_000, "p75":  43_000},
    "Royal City":                      {"p25":  16_000, "median":  24_000, "p75":  33_000},

    # ══════════════════════════════════════════════════════════════════
    # NORTH COAST  (all figures = EGP/m², vacation-use chalet/apt)
    # ══════════════════════════════════════════════════════════════════

    # ── Sidi Abd El Rahman zone (km 95–130) — ultra-premium ──────────
    "Marassi":                         {"p25": 105_000, "median": 155_000, "p75": 220_000},
    "Hacienda Bay":                    {"p25":  90_000, "median": 130_000, "p75": 175_000},
    "Hacienda White":                  {"p25":  65_000, "median":  95_000, "p75": 130_000},
    "Fouka Bay":                       {"p25":  85_000, "median": 125_000, "p75": 170_000},
    "Bo Islands":                      {"p25":  75_000, "median": 110_000, "p75": 150_000},
    "Amwaj":                           {"p25":  55_000, "median":  82_000, "p75": 112_000},
    "Palm Hills North Coast":          {"p25":  60_000, "median":  88_000, "p75": 120_000},
    "Swan Lake North Coast":           {"p25":  52_000, "median":  76_000, "p75": 104_000},
    "Kingsway":                        {"p25":  50_000, "median":  72_000, "p75":  98_000},
    "La Vista Gardens (NC)":           {"p25":  50_000, "median":  71_000, "p75":  96_000},
    "Al Alamein Towers":               {"p25":  60_000, "median":  87_000, "p75": 118_000},
    "Marasy (Sidi Abd El Rahman)":     {"p25":  60_000, "median":  86_000, "p75": 116_000},

    # ── Ras El Hekma zone (km 145–200) — new premium ─────────────────
    "Mountain View Ras El Hekma":      {"p25":  75_000, "median": 110_000, "p75": 150_000},
    "SODIC The Estates":               {"p25":  80_000, "median": 118_000, "p75": 160_000},
    "Jefaira":                         {"p25":  58_000, "median":  88_000, "p75": 120_000},
    "Telal North Coast":               {"p25":  38_000, "median":  58_000, "p75":  80_000},
    "Diplo North Coast":               {"p25":  33_000, "median":  50_000, "p75":  68_000},
    "Masa North Coast":                {"p25":  32_000, "median":  48_000, "p75":  65_000},
    "Koun":                            {"p25":  52_000, "median":  76_000, "p75": 102_000},
    "Sur Mer":                         {"p25":  36_000, "median":  55_000, "p75":  74_000},
    "White Bay":                       {"p25":  36_000, "median":  54_000, "p75":  72_000},
    "Ayla":                            {"p25":  32_000, "median":  48_000, "p75":  65_000},
    "La Mirage":                       {"p25":  30_000, "median":  46_000, "p75":  62_000},

    # ── Western Sahel (km 45–90) — mid / affordable ───────────────────
    "Marina":                          {"p25":  28_000, "median":  44_000, "p75":  62_000},
    "Porto Marina":                    {"p25":  24_000, "median":  38_000, "p75":  54_000},
    "Caesars":                         {"p25":  22_000, "median":  34_000, "p75":  46_000},
    "Blue Blue":                       {"p25":  20_000, "median":  30_000, "p75":  42_000},
    "La Costa":                        {"p25":  19_000, "median":  29_000, "p75":  40_000},
    "Silver Sands":                    {"p25":  18_000, "median":  28_000, "p75":  39_000},
    "Seashore":                        {"p25":  17_000, "median":  26_000, "p75":  36_000},
    "Retal":                           {"p25":  15_000, "median":  23_000, "p75":  32_000},
    "Nawara":                          {"p25":  13_000, "median":  20_000, "p75":  28_000},
    "Bali North Coast":                {"p25":  13_000, "median":  20_000, "p75":  28_000},
    "North Coast Village":             {"p25":  11_000, "median":  17_000, "p75":  24_000},
    "ABHA (North Coast)":              {"p25":  13_000, "median":  20_000, "p75":  28_000},   # NC ABHA (vacation)
    "Mabany Edrees":                   {"p25":  13_000, "median":  20_000, "p75":  27_000},

    # ══════════════════════════════════════════════════════════════════
    # AIN SOKHNA / RED SEA
    # ══════════════════════════════════════════════════════════════════

    # ── South Sokhna — premium resort (km 90–160) ─────────────────────
    "Il Monte Galala":                 {"p25":  80_000, "median": 112_000, "p75": 150_000},
    "Mountain View Sokhna":            {"p25":  60_000, "median":  90_000, "p75": 122_000},
    "La Vista Sokhna":                 {"p25":  52_000, "median":  76_000, "p75": 102_000},
    "Palm Hills Sokhna":               {"p25":  50_000, "median":  74_000, "p75": 100_000},
    "Blumar":                          {"p25":  36_000, "median":  54_000, "p75":  74_000},

    # ── North Sokhna — mid / affordable (km 45–80) ───────────────────
    "Swan Lake Sokhna":                {"p25":  40_000, "median":  60_000, "p75":  82_000},
    "Stella Di Mare":                  {"p25":  28_000, "median":  44_000, "p75":  60_000},
    "Porto Sokhna":                    {"p25":  26_000, "median":  40_000, "p75":  55_000},

    # ══════════════════════════════════════════════════════════════════
    # NEW ADMINISTRATIVE CAPITAL
    # ══════════════════════════════════════════════════════════════════
    "IL Bosco (Misr Italia)":          {"p25":  28_000, "median":  40_000, "p75":  55_000},
    "Bloomfields":                     {"p25":  30_000, "median":  43_000, "p75":  58_000},
    "Scenario (Ora)":                  {"p25":  28_000, "median":  41_000, "p75":  56_000},
    "Midtown Solo (Better Home)":      {"p25":  20_000, "median":  30_000, "p75":  42_000},

    # ══════════════════════════════════════════════════════════════════
    # MOSTAKBAL CITY (separate area)
    # ══════════════════════════════════════════════════════════════════
    "Haptown (Hassan Allam)":          {"p25":  30_000, "median":  44_000, "p75":  59_000},
    "Al Burouj":                       {"p25":  24_000, "median":  35_000, "p75":  47_000},
}


# ──────────────────────────────────────────────────────────────────────────────
# AREA-SPECIFIC OVERRIDES
# For compound names that appear in multiple areas with different price profiles,
# use this dict keyed by (area_id, compound_label) to get the correct price.
# This is checked BEFORE REFERENCE_PRICES in the lookup chain.
# ──────────────────────────────────────────────────────────────────────────────

AREA_REFERENCE_PRICES: dict[tuple, dict] = {
    # ABHA appears in both 6th October (affordable gov. housing ~11.5K) and
    # North Coast (western_sahel vacation, ~20K).  Must be separated by area.
    ("oct_6",        "ABHA"):  {"p25":  18_000, "median":  24_000, "p75":  32_000},
    ("north_coast",  "ABHA"):  {"p25":  13_000, "median":  20_000, "p75":  28_000},
    ("sidi_abd",     "ABHA"):  {"p25":  13_000, "median":  20_000, "p75":  28_000},
    ("ras_el_hekma", "ABHA"):  {"p25":  13_000, "median":  20_000, "p75":  28_000},
    ("western_sahel","ABHA"):  {"p25":  13_000, "median":  20_000, "p75":  28_000},
}
