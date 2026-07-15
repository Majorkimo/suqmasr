"""
Developer & compound tier database for Egypt real estate.

Tiers (relative to area median EGP/m²):
  1 = Ultra Premium  — flagship gated communities, international developers, 1.80× median
  2 = Premium        — established quality brands, solid infrastructure,    1.20× median
  3 = Mid-Market     — competent mid-tier developers, standard amenities,   0.85× median
  4 = Affordable     — mass-market / older / smaller developers,            0.45× median

The tier multipliers are used as a Bayesian prior when live market data is sparse.
When a compound has ≥10 listings the market price dominates; at 2–4 listings
the prior contributes ~55%; with zero data the prior is the sole estimate.
"""

# ── Tier multipliers (relative to area-wide median EGP/m²) ──────────────────
TIER_MULTIPLIERS = {
    1: 1.80,
    2: 1.20,
    3: 0.85,
    4: 0.45,
}

TIER_LABELS = {
    1: "Ultra Premium",
    2: "Premium",
    3: "Mid-Market",
    4: "Affordable",
}

# ── Blending weights: how much to weight market vs. tier prior ───────────────
# Key = listings_with_area count, value = (market_weight, tier_weight)
def blend_weights(n: int) -> tuple[float, float]:
    if n >= 10: return (0.95, 0.05)
    if n >= 5:  return (0.75, 0.25)
    if n >= 2:  return (0.45, 0.55)
    return (0.10, 0.90)   # near-zero data: rely almost entirely on tier prior


# ── Compound tier map ────────────────────────────────────────────────────────
# Keys match the "label" field in locations.py COMPOUNDS exactly.
COMPOUND_TIERS: dict[str, dict] = {

    # ── North Coast / Sahel ──────────────────────────────────────────────────
    "Marassi":                  {"developer": "Emaar Misr",            "tier": 1},
    "Hacienda Bay":             {"developer": "Palm Hills",             "tier": 1},
    "Fouka Bay":                {"developer": "Tatweer Misr",           "tier": 1},
    "Mountain View Ras el Hekma":{"developer": "Mountain View",         "tier": 1},
    "SODIC The Estates":        {"developer": "SODIC",                  "tier": 1},
    "Jefaira":                  {"developer": "Inertia",                "tier": 2},
    "Hacienda White":           {"developer": "Palm Hills",             "tier": 2},
    "Amwaj":                    {"developer": "Mountain View",          "tier": 2},
    "Swan Lake North Coast":    {"developer": "Hassan Allam",           "tier": 2},
    "Kingsway":                 {"developer": "Mountain View",          "tier": 2},
    "La Vista Gardens":         {"developer": "La Vista",               "tier": 2},
    "Bo Islands":               {"developer": "Ora Developers",         "tier": 2},
    "Diplo North Coast":        {"developer": "Diplo",                  "tier": 3},
    "Telal North Coast":        {"developer": "Telal",                  "tier": 3},
    "Blue-Blue":                {"developer": "Blue-Blue",              "tier": 3},
    "Caesars":                  {"developer": "Caesars",                "tier": 3},
    "Sur Mer":                  {"developer": "Sur Mer",                "tier": 3},
    "Ayla":                     {"developer": "Ayla",                   "tier": 3},
    "White Bay":                {"developer": "White Bay",              "tier": 3},
    "Retal":                    {"developer": "Retal",                  "tier": 3},
    "Masa North Coast":         {"developer": "Masa",                   "tier": 3},
    "Koun":                     {"developer": "Mabany Edrees",          "tier": 3},
    "Marina":                   {"developer": "Marina",                 "tier": 3},
    "Porto Marina":             {"developer": "Porto Group",            "tier": 3},
    "Al Alamein Towers":        {"developer": "City Edge",              "tier": 2},
    "La Mirage North Coast":    {"developer": "La Mirage",              "tier": 3},
    "Palm Hills North Coast":   {"developer": "Palm Hills",             "tier": 2},
    "La Costa":                 {"developer": "La Costa",               "tier": 3},
    "Silver Sands":             {"developer": "Silver Sands",           "tier": 4},
    "Seashore":                 {"developer": "Seashore",               "tier": 4},
    "Nawara":                   {"developer": "Nawara",                 "tier": 4},
    "North Coast Village":      {"developer": "Various",                "tier": 4},
    "Bali North Coast":         {"developer": "Bali NC",                "tier": 4},
    "ABHA":                     {"developer": "El Shabory",             "tier": 4},
    "Mabany Edrees":            {"developer": "Mabany Edrees",          "tier": 4},
    "Makadi Heights":           {"developer": "Orascom",                "tier": 2},
    "Swan Lake":                {"developer": "Hassan Allam",           "tier": 2},
    "Porto Sokhna":             {"developer": "Porto Group",            "tier": 3},

    # ── New Cairo / 5th Settlement ───────────────────────────────────────────
    "Mivida (Emaar)":           {"developer": "Emaar Misr",            "tier": 1},
    "Eastown (Sodic)":          {"developer": "SODIC",                  "tier": 1},
    "Hyde Park":                {"developer": "Hassan Allam",           "tier": 1},
    "Mountain View iCity":      {"developer": "Mountain View",          "tier": 1},
    "Palm Hills New Cairo":     {"developer": "Palm Hills",             "tier": 1},
    "Katameya Heights":         {"developer": "Golf Heights",           "tier": 1},
    "City Gate (Sapphire)":     {"developer": "City Edge",              "tier": 2},
    "Mountain View Hyde Park":  {"developer": "Mountain View",          "tier": 1},
    "Swan Lake New Cairo":      {"developer": "Hassan Allam",           "tier": 1},
    "Marasem / Fifth Square":   {"developer": "Al Marasem",            "tier": 2},
    "Aliva (Mountain View)":    {"developer": "Mountain View",          "tier": 2},
    "Capital Gardens":          {"developer": "City Edge",              "tier": 3},
    "Trio Gardens":             {"developer": "M Squared",              "tier": 3},
    "Taj City":                 {"developer": "Madinet Masr",           "tier": 3},
    "The Square (Sabbour)":     {"developer": "Al Ahly Sabbour",        "tier": 3},
    "Beit Al Watan":            {"developer": "Various",                "tier": 4},

    # ── 6th October ─────────────────────────────────────────────────────────
    "Badya (Palm Hills)":       {"developer": "Palm Hills",             "tier": 1},
    "O West (Palm Hills)":      {"developer": "Palm Hills",             "tier": 1},
    "Mountain View iCity October":{"developer": "Mountain View",        "tier": 1},
    "Mountain View 4":          {"developer": "Mountain View",          "tier": 1},
    "Mountain View Chillout Park":{"developer": "Mountain View",        "tier": 1},
    "Palm Hills WoodVille":     {"developer": "Palm Hills",             "tier": 1},
    "Palm Parks (Palm Hills)":  {"developer": "Palm Hills",             "tier": 1},
    "Joulz (Emaar)":            {"developer": "Emaar Misr",            "tier": 1},
    "Mountain View October Park":{"developer": "Mountain View",         "tier": 2},
    "Swan Lake West":           {"developer": "Hassan Allam",           "tier": 2},
    "Swan Lake October":        {"developer": "Hassan Allam",           "tier": 2},
    "Keeva (Al Ahly Sabbour)":  {"developer": "Al Ahly Sabbour",        "tier": 2},
    "New Giza":                 {"developer": "G Developments",         "tier": 2},
    "Grand Heights":            {"developer": "Hassan Allam",           "tier": 2},
    "Soleya":                   {"developer": "Inertia",                "tier": 2},
    "Beverly Hills October":    {"developer": "SODIC",                  "tier": 2},
    "ECO West":                 {"developer": "ECO West",               "tier": 3},
    "Beit Alwatan":             {"developer": "Various",                "tier": 3},
    "Sun Capital":              {"developer": "Sun Capital",            "tier": 3},
    "Green IV (Mabany Edrees)": {"developer": "Mabany Edrees",          "tier": 3},
    "Al Karma 4":               {"developer": "Al Karma",               "tier": 4},
    "Dar Misr":                 {"developer": "Various",                "tier": 4},

    # ── Sheikh Zayed ─────────────────────────────────────────────────────────
    "Palm Hills Golf Extension": {"developer": "Palm Hills",            "tier": 1},
    "Palm Hills October":       {"developer": "Palm Hills",             "tier": 1},
    "Allegria (Sodic)":         {"developer": "SODIC",                  "tier": 1},
    "Westown (Sodic)":          {"developer": "SODIC",                  "tier": 1},
    "ZED West":                 {"developer": "Ora Developers",         "tier": 2},
    "ZED Sheikh Zayed":         {"developer": "Ora Developers",         "tier": 2},
    "Beverly Hills":            {"developer": "SODIC",                  "tier": 2},
    "El Rabwa":                 {"developer": "Al Karma",               "tier": 2},
    "Sodic West":               {"developer": "SODIC",                  "tier": 2},
    "Royal City":               {"developer": "City Edge",              "tier": 3},
    "Mirage City":              {"developer": "Mirage City",            "tier": 3},

    # ── NAC / Mostakbal ──────────────────────────────────────────────────────
    "Sarai (Madinet Masr)":     {"developer": "Madinet Masr",           "tier": 2},
    "Azha":                     {"developer": "Al Ahly Sabbour",        "tier": 2},
    "Haptown (Hassan Allam)":   {"developer": "Hassan Allam",           "tier": 2},
    "Al Burouj":                {"developer": "Al Burouj",              "tier": 2},
}
