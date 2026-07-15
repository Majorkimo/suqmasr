# Egypt real estate location data — verified slugs
# aqarmap_slug  → /en/for-sale/{type}/egypt/{slug}/
# dubizzle_slug → /en/properties/{type}-for-sale/{slug}/
# pf_city/pf_area → propertyfinder.eg/en/buy/{pf_city}/{type}-for-sale{pf_area}.html
#
# territory — sub-zone within the area used for territorial median calculation.
#   Territories reflect geographic / price-band groupings (e.g. northern vs southern
#   strips within 6th October, km-band zones along the North Coast).

CITIES = [
    {"id": "cairo",       "label": "Cairo"},
    {"id": "giza",        "label": "Giza"},
    {"id": "alexandria",  "label": "Alexandria"},
    {"id": "north_coast", "label": "North Coast (Sahel)"},
    {"id": "ain_sokhna",  "label": "Ain Sokhna / Red Sea"},
    {"id": "new_capital", "label": "New Administrative Capital"},
]

AREAS = {
    "cairo": [
        {"id": "new_cairo",      "label": "New Cairo / 5th Settlement", "aqarmap": "new-cairo",          "dubizzle": "new-cairo",          "pf_city": "cairo", "pf_area": "-new-cairo-city"},
        {"id": "maadi",          "label": "Maadi",                      "aqarmap": "el-maadi",           "dubizzle": "el-maadi",           "pf_city": "cairo", "pf_area": "-hay-el-maadi"},
        {"id": "heliopolis",     "label": "Heliopolis",                 "aqarmap": "heliopolis",         "dubizzle": "heliopolis",         "pf_city": "cairo", "pf_area": "-heliopolis-masr-el-gedida"},
        {"id": "nasr_city",      "label": "Nasr City",                  "aqarmap": "nasr-city",          "dubizzle": "nasr-city",          "pf_city": "cairo", "pf_area": "-nasr-city"},
        {"id": "zamalek",        "label": "Zamalek",                    "aqarmap": "zamalek",            "dubizzle": "zamalek",            "pf_city": "cairo", "pf_area": "-zamalek"},
        {"id": "garden_city",    "label": "Garden City",                "aqarmap": "garden-city",        "dubizzle": "garden-city",        "pf_city": "cairo", "pf_area": "-garden-city"},
        {"id": "downtown",       "label": "Downtown Cairo",             "aqarmap": "downtown-cairo",     "dubizzle": "downtown",           "pf_city": "cairo", "pf_area": "-downtown"},
        {"id": "shorouk",        "label": "El Shorouk",                 "aqarmap": "el-shorouk-city",    "dubizzle": "el-shorouk-city",    "pf_city": "cairo", "pf_area": "-shorouk-city"},
        {"id": "rehab",          "label": "El Rehab",                   "aqarmap": "el-rehab-city",      "dubizzle": "el-rehab",           "pf_city": "cairo", "pf_area": "-el-rehab-city"},
        {"id": "mostakbal",      "label": "Mostakbal City",             "aqarmap": "mostakbal-city",     "dubizzle": "mostakbal-city",     "pf_city": "cairo", "pf_area": "-mostakbal-city-future-city"},
        {"id": "badr",           "label": "Badr City",                  "aqarmap": "badr-city",          "dubizzle": "badr-city",          "pf_city": "cairo", "pf_area": "-badr-city"},
        {"id": "obour",          "label": "El Obour",                   "aqarmap": "el-obour",           "dubizzle": "el-obour",           "pf_city": "cairo", "pf_area": ""},
        {"id": "new_heliopolis", "label": "New Heliopolis",             "aqarmap": "new-heliopolis",     "dubizzle": "new-heliopolis",     "pf_city": "cairo", "pf_area": "-new-heliopolis"},
        {"id": "masr_gedida",    "label": "Masr El Gedida",            "aqarmap": "masr-el-gedida",     "dubizzle": "masr-el-gedida",     "pf_city": "cairo", "pf_area": "-heliopolis-masr-el-gedida"},
        {"id": "mohandessin",    "label": "Mohandessin",                "aqarmap": "mohandessin",        "dubizzle": "mohandessin",        "pf_city": "cairo", "pf_area": ""},
        {"id": "dokki",          "label": "Dokki",                      "aqarmap": "dokki",              "dubizzle": "dokki",              "pf_city": "cairo", "pf_area": ""},
        {"id": "new_capital_c",  "label": "New Capital City",           "aqarmap": "new-administrative-capital", "dubizzle": "new-administrative-capital", "pf_city": "cairo", "pf_area": "-new-capital-city"},
    ],
    "giza": [
        {"id": "sheikh_zayed",   "label": "Sheikh Zayed",               "aqarmap": "sheikh-zayed",       "dubizzle": "sheikh-zayed",       "pf_city": "giza",  "pf_area": "-sheikh-zayed-city"},
        {"id": "oct_6",          "label": "6th of October",             "aqarmap": "6th-of-october",     "dubizzle": "6th-of-october",     "pf_city": "giza",  "pf_area": ""},
        {"id": "hadayek_oct",    "label": "Hadayek October",            "aqarmap": "hadayek-october",    "dubizzle": "hadayek-october",    "pf_city": "giza",  "pf_area": ""},
        {"id": "haram",          "label": "Haram",                      "aqarmap": "haram",              "dubizzle": "haram",              "pf_city": "giza",  "pf_area": ""},
        {"id": "giza_city",      "label": "Giza City",                  "aqarmap": "giza",               "dubizzle": "giza",               "pf_city": "giza",  "pf_area": ""},
        {"id": "dream_land",     "label": "Dream Land / Abu Rawash",    "aqarmap": "abu-rawash",         "dubizzle": "abu-rawash",         "pf_city": "giza",  "pf_area": ""},
    ],
    "alexandria": [
        {"id": "smouha",         "label": "Smouha",                     "aqarmap": "smouha",             "dubizzle": "smouha",             "pf_city": "alexandria", "pf_area": "-smouha"},
        {"id": "sidi_bishr",     "label": "Sidi Bishr",                 "aqarmap": "sidi-bishr",         "dubizzle": "sidi-bishr",         "pf_city": "alexandria", "pf_area": ""},
        {"id": "stanley",        "label": "Stanley",                    "aqarmap": "stanley",            "dubizzle": "stanley",            "pf_city": "alexandria", "pf_area": ""},
        {"id": "montaza",        "label": "Montaza",                    "aqarmap": "montaza",            "dubizzle": "montaza",            "pf_city": "alexandria", "pf_area": ""},
        {"id": "new_alex",       "label": "New Alexandria",             "aqarmap": "new-alexandria",     "dubizzle": "new-alexandria",     "pf_city": "alexandria", "pf_area": ""},
        {"id": "agami",          "label": "Agami / Hanouvil",           "aqarmap": "agami",              "dubizzle": "agami",              "pf_city": "alexandria", "pf_area": ""},
        {"id": "borg_arab",      "label": "Borg El Arab",               "aqarmap": "borg-el-arab",       "dubizzle": "borg-el-arab",       "pf_city": "alexandria", "pf_area": ""},
    ],
    "north_coast": [
        {"id": "north_coast",    "label": "North Coast (All)",          "aqarmap": "north-coast",        "dubizzle": "north-coast",        "pf_city": "north-coast", "pf_area": ""},
        {"id": "sidi_abd",       "label": "Sidi Abdel Rahman",          "aqarmap": "sidi-abd-el-rahman", "dubizzle": "north-coast",        "pf_city": "north-coast", "pf_area": ""},
        {"id": "ras_el_hekma",   "label": "Ras El Hekma",              "aqarmap": "ras-el-hekma",       "dubizzle": "north-coast",        "pf_city": "north-coast", "pf_area": ""},
        {"id": "el_alamein",     "label": "El Alamein / New Alamein",   "aqarmap": "new-alamein",        "dubizzle": "new-alamein",        "pf_city": "north-coast", "pf_area": ""},
        {"id": "marsa_matrouh",  "label": "Marsa Matrouh",              "aqarmap": "marsa-matrouh",      "dubizzle": "marsa-matrouh",      "pf_city": "north-coast", "pf_area": ""},
    ],
    "ain_sokhna": [
        {"id": "ain_sokhna",     "label": "Ain Sokhna",                 "aqarmap": "ain-sokhna",         "dubizzle": "ain-sokhna",         "pf_city": "suez",  "pf_area": ""},
        {"id": "el_gouna",       "label": "El Gouna",                   "aqarmap": "el-gouna",           "dubizzle": "el-gouna",           "pf_city": "red-sea", "pf_area": ""},
        {"id": "hurghada",       "label": "Hurghada",                   "aqarmap": "hurghada",           "dubizzle": "hurghada",           "pf_city": "red-sea", "pf_area": ""},
    ],
    "new_capital": [
        {"id": "nac_general",    "label": "New Capital (General)",      "aqarmap": "new-administrative-capital", "dubizzle": "new-administrative-capital", "pf_city": "cairo", "pf_area": "-new-capital-city"},
    ],
}

# ── Territory label maps ───────────────────────────────────────────────────────
# Human-readable territory labels per area_id
TERRITORY_LABELS = {
    "oct_6": {
        "south_october":   "South October (Al Wahat Rd) — Premium",
        "central_october": "Central October (26th July Corridor) — Mid",
        "north_october":   "North October (Industrial Belt) — Affordable",
    },
    "new_cairo": {
        "golden_square":     "Golden Square / 5th Settlement — Premium",
        "north_settlements": "3rd Settlement / North New Cairo — Mid",
        "mostakbal":         "Mostakbal City / East Cairo — Emerging",
    },
    "sheikh_zayed": {
        "premium_belt": "Sheikh Zayed Premium Belt — Premium",
        "mid_belt":     "Sheikh Zayed Mid Belt — Mid",
    },
    "north_coast": {
        "sidi_abd":      "Sidi Abd El Rahman (km 95-120) — Ultra Premium",
        "ras_el_hekma":  "Ras El Hekma (km 145-200) — Premium New",
        "western_sahel": "Western Sahel (km 45-90) — Mid / Affordable",
    },
    "ain_sokhna": {
        "south_sokhna": "South Sokhna (km 110+) — Premium",
        "north_sokhna": "North Sokhna (km 45-80) — Mid / Affordable",
    },
    "nac_general": {
        "r7_r8": "R7/R8 Districts — Premium",
        "r2_r5": "R2/R5 Districts — Mid / Affordable",
    },
    "new_capital_c": {
        "r7_r8": "R7/R8 Districts — Premium",
        "r2_r5": "R2/R5 Districts — Mid / Affordable",
    },
}


# ── Compounds keyed by area_id ─────────────────────────────────────────────────
# aqarmap slug → .../compounds/{slug}/   |   dubizzle → text filter in card content
# territory    → sub-zone for price segmentation (see TERRITORY_LABELS above)
COMPOUNDS = {
    # ── New Cairo / 5th Settlement ────────────────────────────────────────────
    "new_cairo": [
        # Golden Square / 5th Settlement — premium gated belt south of the ring road
        {"label": "Hyde Park",                   "aqarmap": "hyde-park-new-cairo",          "dubizzle": "hyde park",                  "territory": "golden_square"},
        {"label": "Mountain View iCity",         "aqarmap": "mountain-view-icity",          "dubizzle": "mountain view icity",        "territory": "golden_square"},
        {"label": "Mountain View Hyde Park",     "aqarmap": "mountain-view-hyde-park",      "dubizzle": "mountain view hyde park",    "territory": "golden_square"},
        {"label": "Palm Hills New Cairo",        "aqarmap": "palm-hills-new-cairo",         "dubizzle": "palm hills new cairo",       "territory": "golden_square"},
        {"label": "Eastown (Sodic)",             "aqarmap": "eastown",                      "dubizzle": "eastown",                    "territory": "golden_square"},
        {"label": "Mivida (Emaar)",              "aqarmap": "mivida",                       "dubizzle": "mivida",                     "territory": "golden_square"},
        {"label": "Swan Lake New Cairo",         "aqarmap": "swan-lake-new-cairo",          "dubizzle": "swan lake",                  "territory": "golden_square"},
        {"label": "Katameya Dunes",              "aqarmap": "katameya-dunes",               "dubizzle": "katameya dunes",             "territory": "golden_square"},
        {"label": "Katameya Heights",            "aqarmap": "katameya-heights",             "dubizzle": "katameya heights",           "territory": "golden_square"},
        {"label": "La Vista New Cairo",          "aqarmap": "la-vista-new-cairo",           "dubizzle": "la vista",                   "territory": "golden_square"},
        {"label": "Aliva (Mountain View)",       "aqarmap": "aliva-compound-mountain-view", "dubizzle": "aliva",                      "territory": "golden_square"},
        # 3rd Settlement / north belt — mid-tier
        {"label": "Marasem / Fifth Square",      "aqarmap": "fifth-square",                 "dubizzle": "fifth square",               "territory": "north_settlements"},
        {"label": "Capital Gardens",             "aqarmap": "capital-gardens",              "dubizzle": "capital gardens",            "territory": "north_settlements"},
        {"label": "City Gate (Sapphire)",        "aqarmap": "city-gate",                    "dubizzle": "city gate",                  "territory": "north_settlements"},
        {"label": "Taj City",                    "aqarmap": "taj-city",                     "dubizzle": "taj city",                   "territory": "north_settlements"},
        {"label": "The Square (Sabbour)",        "aqarmap": "the-square",                   "dubizzle": "the square",                 "territory": "north_settlements"},
        {"label": "Lake Park",                   "aqarmap": "lake-park",                    "dubizzle": "lake park",                  "territory": "north_settlements"},
        {"label": "Trio Gardens",                "aqarmap": "trio-gardens",                 "dubizzle": "trio gardens",               "territory": "north_settlements"},
        {"label": "Beit Al Watan",               "aqarmap": "beit-el-watan",                "dubizzle": "beit al watan",              "territory": "north_settlements"},
        # Mostakbal / far east — emerging
        {"label": "Sarai (Madinet Masr)",        "aqarmap": "sarai",                        "dubizzle": "sarai",                      "territory": "mostakbal"},
        {"label": "Azha",                        "aqarmap": "azha",                         "dubizzle": "azha",                       "territory": "mostakbal"},
        {"label": "Cairo Gate",                  "aqarmap": "cairo-gate",                   "dubizzle": "cairo gate",                 "territory": "mostakbal"},
        {"label": "Arabella",                    "aqarmap": "arabella-new-cairo",           "dubizzle": "arabella",                   "territory": "mostakbal"},
    ],

    # ── Sheikh Zayed ─────────────────────────────────────────────────────────
    "sheikh_zayed": [
        {"label": "Palm Hills Golf Extension",   "aqarmap": "palm-hills-golf-extension",    "dubizzle": "palm hills golf",            "territory": "premium_belt"},
        {"label": "Palm Hills October",          "aqarmap": "palm-hills-october",           "dubizzle": "palm hills october",         "territory": "premium_belt"},
        {"label": "Allegria (Sodic)",            "aqarmap": "allegria",                     "dubizzle": "allegria",                   "territory": "premium_belt"},
        {"label": "Westown (Sodic)",             "aqarmap": "westown",                      "dubizzle": "westown",                    "territory": "premium_belt"},
        {"label": "ZED West",                    "aqarmap": "zed-west",                     "dubizzle": "zed west",                   "territory": "premium_belt"},
        {"label": "ZED Sheikh Zayed",            "aqarmap": "zed-sheikh-zayed",             "dubizzle": "zed sheikh zayed",           "territory": "premium_belt"},
        {"label": "Beverly Hills",               "aqarmap": "beverly-hills-sheikh-zayed",   "dubizzle": "beverly hills",              "territory": "premium_belt"},
        {"label": "Sodic West",                  "aqarmap": "sodic-west",                   "dubizzle": "sodic west",                 "territory": "premium_belt"},
        {"label": "El Rabwa",                    "aqarmap": "el-rabwa",                     "dubizzle": "el rabwa",                   "territory": "mid_belt"},
        {"label": "Mirage City",                 "aqarmap": "mirage-city",                  "dubizzle": "mirage city",                "territory": "mid_belt"},
        {"label": "Royal City",                  "aqarmap": "royal-city",                   "dubizzle": "royal city",                 "territory": "mid_belt"},
    ],

    # ── 6th of October ───────────────────────────────────────────────────────
    # south_october  = Al Wahat Road / Desert Road belt — premium (Palm Hills, Mountain View, Emaar)
    # central_october = 26th July Corridor / interior — mid-tier
    # north_october  = northern industrial / older districts — affordable
    "oct_6": [
        {"label": "Badya (Palm Hills)",          "aqarmap": "badya",                        "dubizzle": "badya",                      "territory": "south_october"},
        {"label": "O West (Palm Hills)",         "aqarmap": "o-west",                       "dubizzle": "o west",                     "territory": "south_october"},
        {"label": "Mountain View iCity October", "aqarmap": "mountain-view-icity-october",  "dubizzle": "mountain view icity",        "territory": "south_october"},
        {"label": "Mountain View 4",             "aqarmap": "mountain-view-4",              "dubizzle": "mountain view 4",            "territory": "south_october"},
        {"label": "Mountain View Chillout Park", "aqarmap": "mountain-view-chillout-park",  "dubizzle": "chillout park",              "territory": "south_october"},
        {"label": "Palm Hills WoodVille",        "aqarmap": "palm-hills-woodville",         "dubizzle": "woodville",                  "territory": "south_october"},
        {"label": "Palm Parks (Palm Hills)",     "aqarmap": "palm-parks",                   "dubizzle": "palm parks",                 "territory": "south_october"},
        {"label": "Joulz (Emaar)",               "aqarmap": "joulz",                        "dubizzle": "joulz",                      "territory": "south_october"},
        {"label": "New Giza",                    "aqarmap": "new-giza",                     "dubizzle": "new giza",                   "territory": "south_october"},
        {"label": "Soleya",                      "aqarmap": "soleya",                       "dubizzle": "soleya",                     "territory": "south_october"},
        {"label": "Beverly Hills October",       "aqarmap": "beverly-hills-october",        "dubizzle": "beverly hills october",      "territory": "south_october"},
        {"label": "Mountain View October Park",  "aqarmap": "mountain-view-october-park",   "dubizzle": "mountain view october park", "territory": "central_october"},
        {"label": "Swan Lake West",              "aqarmap": "swan-lake-west",               "dubizzle": "swan lake west",             "territory": "central_october"},
        {"label": "Swan Lake October",           "aqarmap": "swan-lake-october",            "dubizzle": "swan lake october",          "territory": "central_october"},
        {"label": "Keeva (Al Ahly Sabbour)",     "aqarmap": "keeva",                        "dubizzle": "keeva",                      "territory": "central_october"},
        {"label": "Grand Heights",               "aqarmap": "grand-heights",                "dubizzle": "grand heights",              "territory": "central_october"},
        {"label": "ECO West",                    "aqarmap": "eco-west",                     "dubizzle": "eco west",                   "territory": "north_october"},
        {"label": "Beit Alwatan",                "aqarmap": "beit-alwatan",                 "dubizzle": "beit alwatan",               "territory": "north_october"},
        {"label": "Sun Capital",                 "aqarmap": "sun-capital",                  "dubizzle": "sun capital",                "territory": "north_october"},
        {"label": "Green IV (Mabany Edrees)",    "aqarmap": "green-iv-october",             "dubizzle": "green iv",                   "territory": "north_october"},
        {"label": "ABHA",                        "aqarmap": "abha-october",                 "dubizzle": "abha",                       "territory": "north_october"},
        {"label": "Al Karma 4",                  "aqarmap": "al-karma-4",                   "dubizzle": "al karma 4",                 "territory": "north_october"},
        {"label": "Dar Misr",                    "aqarmap": "dar-misr",                     "dubizzle": "dar misr",                   "territory": "north_october"},
    ],

    # ── Maadi ─────────────────────────────────────────────────────────────────
    "maadi": [
        {"label": "Degla",                       "aqarmap": "degla",                        "dubizzle": "degla",                      "territory": "maadi_core"},
        {"label": "Zahraa El Maadi",             "aqarmap": "zahraa-el-maadi",              "dubizzle": "zahraa el maadi",            "territory": "maadi_core"},
        {"label": "New Maadi",                   "aqarmap": "new-maadi",                    "dubizzle": "new maadi",                  "territory": "maadi_core"},
    ],

    # ── Mostakbal ─────────────────────────────────────────────────────────────
    "mostakbal": [
        {"label": "Sarai (Madinet Masr)",        "aqarmap": "sarai",                        "dubizzle": "sarai",                      "territory": "mostakbal"},
        {"label": "Azha",                        "aqarmap": "azha",                         "dubizzle": "azha",                       "territory": "mostakbal"},
        {"label": "Haptown (Hassan Allam)",      "aqarmap": "haptown",                      "dubizzle": "haptown",                    "territory": "mostakbal"},
        {"label": "Al Burouj",                   "aqarmap": "al-burouj",                    "dubizzle": "al burouj",                  "territory": "mostakbal"},
    ],

    # ── North Coast ───────────────────────────────────────────────────────────
    # western_sahel = km 45-90  — mixed, mid to affordable (Marina, Porto, Silver Sands…)
    # sidi_abd      = km 90-135 — ultra-premium (Marassi, Hacienda Bay, Fouka Bay…)
    # ras_el_hekma  = km 145-200 — new premium (Mountain View, SODIC The Estates, Jefaira…)
    "north_coast": [
        {"label": "Marassi",                     "aqarmap": "marassi",                      "dubizzle": "marassi",                    "territory": "sidi_abd"},
        {"label": "Hacienda Bay",                "aqarmap": "hacienda-bay",                 "dubizzle": "hacienda bay",               "territory": "sidi_abd"},
        {"label": "Hacienda White",              "aqarmap": "hacienda-white",               "dubizzle": "hacienda white",             "territory": "sidi_abd"},
        {"label": "Fouka Bay",                   "aqarmap": "fouka-bay",                    "dubizzle": "fouka bay",                  "territory": "sidi_abd"},
        {"label": "Amwaj",                       "aqarmap": "amwaj",                        "dubizzle": "amwaj",                      "territory": "sidi_abd"},
        {"label": "Bo Islands",                  "aqarmap": "bo-islands",                   "dubizzle": "bo islands",                 "territory": "sidi_abd"},
        {"label": "Palm Hills North Coast",      "aqarmap": "palm-hills-north-coast",       "dubizzle": "palm hills north coast",     "territory": "sidi_abd"},
        {"label": "Swan Lake North Coast",       "aqarmap": "swan-lake-north-coast",        "dubizzle": "swan lake north coast",      "territory": "sidi_abd"},
        {"label": "Kingsway",                    "aqarmap": "kingsway",                     "dubizzle": "kingsway",                   "territory": "sidi_abd"},
        {"label": "La Vista Gardens (NC)",       "aqarmap": "la-vista-gardens",             "dubizzle": "la vista gardens",           "territory": "sidi_abd"},
        {"label": "Al Alamein Towers",           "aqarmap": "al-alamein-towers",            "dubizzle": "al alamein",                 "territory": "sidi_abd"},
        {"label": "Marasy (Sidi Abd El Rahman)", "aqarmap": "marasy",                       "dubizzle": "marasy",                     "territory": "sidi_abd"},
        {"label": "Mountain View Ras El Hekma",  "aqarmap": "mountain-view-ras-el-hekma",   "dubizzle": "mountain view ras el hekma", "territory": "ras_el_hekma"},
        {"label": "SODIC The Estates",           "aqarmap": "sodic-the-estates",            "dubizzle": "the estates",                "territory": "ras_el_hekma"},
        {"label": "Jefaira",                     "aqarmap": "jefaira",                      "dubizzle": "jefaira",                    "territory": "ras_el_hekma"},
        {"label": "Telal North Coast",           "aqarmap": "telal-north-coast",            "dubizzle": "telal",                      "territory": "ras_el_hekma"},
        {"label": "Diplo North Coast",           "aqarmap": "diplo-north-coast",            "dubizzle": "diplo",                      "territory": "ras_el_hekma"},
        {"label": "Masa North Coast",            "aqarmap": "masa-north-coast",             "dubizzle": "masa",                       "territory": "ras_el_hekma"},
        {"label": "Koun",                        "aqarmap": "koun",                         "dubizzle": "koun",                       "territory": "ras_el_hekma"},
        {"label": "Sur Mer",                     "aqarmap": "sur-mer",                      "dubizzle": "sur mer",                    "territory": "ras_el_hekma"},
        {"label": "White Bay",                   "aqarmap": "white-bay",                    "dubizzle": "white bay",                  "territory": "ras_el_hekma"},
        {"label": "Ayla",                        "aqarmap": "ayla",                         "dubizzle": "ayla",                       "territory": "ras_el_hekma"},
        {"label": "La Mirage",                   "aqarmap": "la-mirage-north-coast",        "dubizzle": "la mirage",                  "territory": "ras_el_hekma"},
        {"label": "Caesars",                     "aqarmap": "caesars",                      "dubizzle": "caesars",                    "territory": "western_sahel"},
        {"label": "Marina",                      "aqarmap": "marina",                       "dubizzle": "marina",                     "territory": "western_sahel"},
        {"label": "Porto Marina",                "aqarmap": "porto-marina",                 "dubizzle": "porto marina",               "territory": "western_sahel"},
        {"label": "Silver Sands",                "aqarmap": "silver-sands",                 "dubizzle": "silver sands",               "territory": "western_sahel"},
        {"label": "Seashore",                    "aqarmap": "seashore",                     "dubizzle": "seashore",                   "territory": "western_sahel"},
        {"label": "Nawara",                      "aqarmap": "nawara",                       "dubizzle": "nawara",                     "territory": "western_sahel"},
        {"label": "Blue Blue",                   "aqarmap": "blue-blue",                    "dubizzle": "blue blue",                  "territory": "western_sahel"},
        {"label": "La Costa",                    "aqarmap": "la-costa",                     "dubizzle": "la costa",                   "territory": "western_sahel"},
        {"label": "Bali North Coast",            "aqarmap": "bali-north-coast",             "dubizzle": "bali",                       "territory": "western_sahel"},
        {"label": "North Coast Village",         "aqarmap": "north-coast-village",          "dubizzle": "north coast village",        "territory": "western_sahel"},
        {"label": "Retal",                       "aqarmap": "retal",                        "dubizzle": "retal",                      "territory": "western_sahel"},
        {"label": "ABHA",                        "aqarmap": "abha",                         "dubizzle": "abha",                       "territory": "western_sahel"},
        {"label": "Mabany Edrees",               "aqarmap": "mabany-edrees",                "dubizzle": "mabany edrees",              "territory": "western_sahel"},
    ],

    # ── Sidi Abd El Rahman (sub-area of North Coast) ──────────────────────────
    "sidi_abd": [
        {"label": "Marassi",                     "aqarmap": "marassi",                      "dubizzle": "marassi",                    "territory": "sidi_abd"},
        {"label": "Hacienda Bay",                "aqarmap": "hacienda-bay",                 "dubizzle": "hacienda bay",               "territory": "sidi_abd"},
        {"label": "Hacienda White",              "aqarmap": "hacienda-white",               "dubizzle": "hacienda white",             "territory": "sidi_abd"},
        {"label": "Marasy",                      "aqarmap": "marasy",                       "dubizzle": "marasy",                     "territory": "sidi_abd"},
        {"label": "Bo Islands",                  "aqarmap": "bo-islands",                   "dubizzle": "bo islands",                 "territory": "sidi_abd"},
        {"label": "Fouka Bay",                   "aqarmap": "fouka-bay",                    "dubizzle": "fouka bay",                  "territory": "sidi_abd"},
    ],

    # ── Ras El Hekma (sub-area of North Coast) ────────────────────────────────
    "ras_el_hekma": [
        {"label": "Mountain View Ras El Hekma",  "aqarmap": "mountain-view-ras-el-hekma",   "dubizzle": "mountain view ras el hekma", "territory": "ras_el_hekma"},
        {"label": "SODIC The Estates",           "aqarmap": "sodic-the-estates",            "dubizzle": "the estates",                "territory": "ras_el_hekma"},
        {"label": "Jefaira",                     "aqarmap": "jefaira",                      "dubizzle": "jefaira",                    "territory": "ras_el_hekma"},
    ],

    # ── Ain Sokhna ────────────────────────────────────────────────────────────
    # north_sokhna = km 45-85  (Porto Sokhna, Stella Di Mare…)  — mid/affordable
    # south_sokhna = km 90-160 (Il Monte Galala, Mountain View…) — premium/resort
    "ain_sokhna": [
        {"label": "Porto Sokhna",                "aqarmap": "porto-sokhna",                 "dubizzle": "porto sokhna",               "territory": "north_sokhna"},
        {"label": "Swan Lake Sokhna",            "aqarmap": "swan-lake-sokhna",             "dubizzle": "swan lake sokhna",           "territory": "north_sokhna"},
        {"label": "Stella Di Mare",              "aqarmap": "stella-di-mare",               "dubizzle": "stella di mare",             "territory": "north_sokhna"},
        {"label": "Blumar",                      "aqarmap": "blumar",                       "dubizzle": "blumar",                     "territory": "north_sokhna"},
        {"label": "Il Monte Galala",             "aqarmap": "il-monte-galala",              "dubizzle": "il monte galala",            "territory": "south_sokhna"},
        {"label": "Mountain View Sokhna",        "aqarmap": "mountain-view-sokhna",         "dubizzle": "mountain view sokhna",       "territory": "south_sokhna"},
        {"label": "La Vista Sokhna",             "aqarmap": "la-vista-sokhna",              "dubizzle": "la vista sokhna",            "territory": "south_sokhna"},
        {"label": "Palm Hills Sokhna",           "aqarmap": "palm-hills-sokhna",            "dubizzle": "palm hills sokhna",          "territory": "south_sokhna"},
    ],

    # ── New Administrative Capital ────────────────────────────────────────────
    "nac_general": [
        {"label": "IL Bosco (Misr Italia)",      "aqarmap": "il-bosco",                     "dubizzle": "il bosco",                   "territory": "r7_r8"},
        {"label": "Bloomfields",                 "aqarmap": "bloomfields",                  "dubizzle": "bloomfields",                "territory": "r7_r8"},
        {"label": "Scenario (Ora)",              "aqarmap": "scenario",                     "dubizzle": "scenario",                   "territory": "r7_r8"},
        {"label": "Midtown Solo (Better Home)",  "aqarmap": "midtown-solo",                 "dubizzle": "midtown solo",               "territory": "r2_r5"},
    ],
    "new_capital_c": [
        {"label": "IL Bosco (Misr Italia)",      "aqarmap": "il-bosco",                     "dubizzle": "il bosco",                   "territory": "r7_r8"},
        {"label": "Bloomfields",                 "aqarmap": "bloomfields",                  "dubizzle": "bloomfields",                "territory": "r7_r8"},
        {"label": "Midtown Solo (Better Home)",  "aqarmap": "midtown-solo",                 "dubizzle": "midtown solo",               "territory": "r2_r5"},
    ],
}


# ── Helper: build compound→territory lookup ───────────────────────────────────
def build_territory_map() -> dict[str, tuple[str, str]]:
    """Returns {compound_label: (area_id, territory)}"""
    result: dict[str, tuple[str, str]] = {}
    for area_id, comps in COMPOUNDS.items():
        for c in comps:
            t = c.get("territory")
            if t:
                result[c["label"]] = (area_id, t)
    return result


COMPOUND_TERRITORY_MAP: dict[str, tuple[str, str]] = build_territory_map()
