"""
Egypt Car Catalog — comprehensive specs, generations, engines, new prices.

Structure per model:
  first_year_global  : year car was first produced anywhere
  egypt_from         : first year officially sold/assembled in Egypt
  assembled_in_egypt : True if locally assembled (lower price, more common)
  assembler          : factory name if assembled in Egypt
  body_types         : list of body styles
  segments           : e.g. B-segment, C-segment, SUV-compact
  generations        : ordered list of generation dicts
  engines_egypt      : engines actually sold in Egypt (may differ from global)
  new_price_egp_2025 : official new car price range in EGP (early 2025)
  new_price_egp_2024 : official new car price range in EGP (2024)
  trims_egypt        : trim levels sold in Egypt
  notes              : market-specific notes
"""

CATALOG: dict[str, dict] = {

    # ════════════════════════════════════════════════════════════════════
    # TOYOTA
    # ════════════════════════════════════════════════════════════════════

    "Toyota": {
        "Corolla": {
            "first_year_global": 1966,
            "egypt_from": 1990,
            "assembled_in_egypt": True,
            "assembler": "ETCO – Egypt Toyota Company (6th of October City)",
            "body_types": ["sedan"],
            "segments": ["C-segment", "compact sedan"],
            "generations": [
                {"gen": "E140/150 (10th)", "years": "2006-2013", "facelift": "2009"},
                {"gen": "E170 (11th)", "years": "2013-2019", "facelift": "2016"},
                {"gen": "E210 (12th)", "years": "2019-present", "facelift": "2022", "notes": "1.5L assembled locally from 2021"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L 4-cyl", "hp": 107, "torque_nm": 138, "trans": ["auto 7-spd CVT"]},
                {"cc": 1798, "label": "1.8L 4-cyl", "hp": 140, "torque_nm": 172, "trans": ["auto 7-spd CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 950_000, "max": 1_250_000},
            "trims_egypt": ["Classic", "SE", "Sport"],
            "notes": "Best-selling sedan in Egypt; assembled locally keeps price competitive",
        },
        "Yaris": {
            "first_year_global": 1999,
            "egypt_from": 2006,
            "assembled_in_egypt": True,
            "assembler": "ETCO",
            "body_types": ["sedan", "hatchback"],
            "segments": ["B-segment", "subcompact"],
            "generations": [
                {"gen": "XP90 (2nd)", "years": "2005-2011", "facelift": "2008"},
                {"gen": "XP130 (3rd)", "years": "2011-2020", "facelift": "2014"},
                {"gen": "XP210 (4th)", "years": "2020-present", "facelift": "2023", "notes": "Sedan-only in Egypt"},
            ],
            "engines_egypt": [
                {"cc": 1496, "label": "1.5L 4-cyl", "hp": 107, "torque_nm": 138, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 890_000, "max": 1_050_000},
            "new_price_egp_2024": {"min": 780_000, "max": 980_000},
            "trims_egypt": ["SE", "SE+"],
            "notes": "Entry-level Toyota; locally assembled sedan popular as first car",
        },
        "Camry": {
            "first_year_global": 1982,
            "egypt_from": 1995,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "XV50 (7th)", "years": "2012-2017", "facelift": "2014"},
                {"gen": "XV70 (8th)", "years": "2018-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 2487, "label": "2.5L 4-cyl", "hp": 203, "torque_nm": 243, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_750_000, "max": 2_100_000},
            "trims_egypt": ["SE", "GLE"],
        },
        "C-HR": {
            "first_year_global": 2016,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "subcompact SUV"],
            "generations": [
                {"gen": "1st gen AX10", "years": "2016-2023", "facelift": "2020"},
                {"gen": "2nd gen AX50", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1987, "label": "2.0L hybrid", "hp": 184, "torque_nm": 190, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_400_000, "max": 1_650_000},
            "trims_egypt": ["GLE", "GR-S"],
            "notes": "Popular hybrid; good resale value",
        },
        "RAV4": {
            "first_year_global": 1994,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "compact SUV"],
            "generations": [
                {"gen": "4th gen XA40", "years": "2012-2018", "facelift": "2015"},
                {"gen": "5th gen XA50", "years": "2018-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 2487, "label": "2.5L 4-cyl", "hp": 203, "torque_nm": 243, "trans": ["auto 8-spd"]},
                {"cc": 2487, "label": "2.5L hybrid", "hp": 222, "torque_nm": None, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 2_300_000, "max": 2_700_000},
            "new_price_egp_2024": {"min": 2_000_000, "max": 2_400_000},
            "trims_egypt": ["GLE", "GLE+"],
        },
        "Fortuner": {
            "first_year_global": 2004,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "body-on-frame SUV"],
            "generations": [
                {"gen": "1st gen AN50/60", "years": "2004-2015", "facelift": "2011"},
                {"gen": "2nd gen AN150/160", "years": "2015-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 2693, "label": "2.7L 4-cyl petrol", "hp": 163, "torque_nm": 245, "trans": ["auto 6-spd"]},
                {"cc": 2755, "label": "2.8L diesel turbo", "hp": 204, "torque_nm": 500, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_100_000, "max": 3_600_000},
            "new_price_egp_2024": {"min": 2_700_000, "max": 3_200_000},
            "trims_egypt": ["EXR", "GXR", "VXR"],
            "notes": "Iconic family SUV; diesel version premium priced",
        },
        "Hilux": {
            "first_year_global": 1968,
            "egypt_from": 1990,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["pickup", "light commercial"],
            "generations": [
                {"gen": "7th gen AN10/20", "years": "2004-2015"},
                {"gen": "8th gen AN120/130", "years": "2015-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 2393, "label": "2.4L diesel turbo", "hp": 150, "torque_nm": 400, "trans": ["auto 6-spd", "manual 6-spd"]},
                {"cc": 2755, "label": "2.8L diesel turbo", "hp": 204, "torque_nm": 500, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_700_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_350_000, "max": 2_800_000},
            "trims_egypt": ["S", "SR", "SR+", "SR5"],
        },
        "Land Cruiser": {
            "first_year_global": 1951,
            "egypt_from": 1980,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV", "full-size SUV"],
            "generations": [
                {"gen": "J200 (200 series)", "years": "2007-2021", "facelift": "2012/2015"},
                {"gen": "J300 (300 series)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 3346, "label": "3.3L twin-turbo diesel V6", "hp": 309, "torque_nm": 700, "trans": ["auto 10-spd"]},
                {"cc": 3444, "label": "3.5L twin-turbo petrol V6", "hp": 415, "torque_nm": 650, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 8_000_000, "max": 12_000_000},
            "new_price_egp_2024": {"min": 7_000_000, "max": 10_500_000},
            "trims_egypt": ["GX-R", "GX-R+", "VX-R", "VX-S"],
            "notes": "Extremely high demand; resale value near or above new price",
        },
        "Land Cruiser 70": {
            "first_year_global": 1984,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup", "wagon", "4x4"],
            "segments": ["off-road", "light commercial"],
            "generations": [
                {"gen": "J70 (ongoing)", "years": "1984-present", "notes": "Continuously updated; reintroduced in Egypt 2014"},
            ],
            "engines_egypt": [
                {"cc": 4000, "label": "4.0L V6 petrol", "hp": 236, "torque_nm": 381, "trans": ["manual 5-spd"]},
                {"cc": 4461, "label": "4.5L V8 diesel", "hp": 202, "torque_nm": 430, "trans": ["manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_800_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 2_400_000, "max": 3_000_000},
            "trims_egypt": ["GX", "GXL"],
            "notes": "Workhorse 4x4; popular in desert/commercial use",
        },
        "Rush": {
            "first_year_global": 2006,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "2nd gen F800", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1496, "label": "1.5L 4-cyl", "hp": 104, "torque_nm": 136, "trans": ["auto 4-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_250_000, "max": 1_450_000},
            "new_price_egp_2024": {"min": 1_100_000, "max": 1_300_000},
            "trims_egypt": ["EXR"],
            "notes": "Budget 7-seater SUV; popular family choice",
        },
        "Prado": {
            "first_year_global": 1984,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "5/7-seater"],
            "segments": ["D-SUV", "mid-size SUV"],
            "generations": [
                {"gen": "J150 (4th)", "years": "2009-2024", "facelift": "2013/2017"},
                {"gen": "J250 (5th)", "years": "2024-present"},
            ],
            "engines_egypt": [
                {"cc": 2694, "label": "2.7L 4-cyl petrol", "hp": 163, "torque_nm": 246, "trans": ["auto 6-spd"]},
                {"cc": 2755, "label": "2.8L diesel turbo", "hp": 204, "torque_nm": 500, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 6_000_000},
            "new_price_egp_2024": {"min": 3_900_000, "max": 5_200_000},
            "trims_egypt": ["EXR", "GXR", "TXL", "VXL"],
        },
        "Corolla Cross": {
            "first_year_global": 2020,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "C-SUV"],
            "generations": [
                {"gen": "1st gen AX10", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1987, "label": "2.0L hybrid", "hp": 196, "torque_nm": 188, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_700_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_480_000, "max": 1_750_000},
            "trims_egypt": ["GLE", "GLE+"],
            "notes": "Hybrid-only in Egypt; bridges Corolla and RAV4",
        },
        "Avanza": {
            "first_year_global": 2003,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["MPV", "7-seater"],
            "segments": ["MPV", "budget family"],
            "generations": [
                {"gen": "F654 (2nd)", "years": "2012-2022", "facelift": "2015"},
            ],
            "engines_egypt": [
                {"cc": 1329, "label": "1.3L 4-cyl", "hp": 95, "torque_nm": 121, "trans": ["auto 4-spd", "manual 5-spd"]},
                {"cc": 1496, "label": "1.5L 4-cyl", "hp": 104, "torque_nm": 136, "trans": ["auto 4-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "trims_egypt": ["E", "G"],
            "notes": "Discontinued; strong used market presence in Egypt",
        },
        "Veloz": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["MPV", "7-seater"],
            "segments": ["MPV"],
            "generations": [
                {"gen": "1st gen A453F", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1496, "label": "1.5L 4-cyl", "hp": 104, "torque_nm": 136, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_150_000},
            "new_price_egp_2024": {"min": 830_000, "max": 1_000_000},
            "trims_egypt": ["G", "Q"],
        },
        "Raize": {
            "first_year_global": 2019,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["A-SUV", "mini SUV"],
            "generations": [
                {"gen": "1st gen A200A", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 998, "label": "1.0L turbo 3-cyl", "hp": 98, "torque_nm": 140, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 800_000, "max": 980_000},
            "new_price_egp_2024": {"min": 700_000, "max": 855_000},
            "trims_egypt": ["G", "GZ"],
        },
        "Prius": {
            "first_year_global": 1997,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "hybrid"],
            "segments": ["C-segment", "hybrid"],
            "generations": [
                {"gen": "ZVW30 (3rd)", "years": "2009-2015"},
                {"gen": "ZVW50 (4th)", "years": "2015-2022"},
                {"gen": "ZVW60 (5th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1798, "label": "1.8L hybrid", "hp": 122, "torque_nm": 142, "trans": ["e-CVT"]},
                {"cc": 1987, "label": "2.0L hybrid (5th gen)", "hp": 196, "torque_nm": 188, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_650_000},
            "trims_egypt": ["Standard", "Advanced"],
            "notes": "Pioneer hybrid in Egypt; strong fuel economy appeal",
        },
        "Aurion": {
            "first_year_global": 2006,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "XV40 (1st)", "years": "2006-2012"},
                {"gen": "XV50 (2nd)", "years": "2012-2017"},
            ],
            "engines_egypt": [
                {"cc": 3456, "label": "3.5L V6", "hp": 277, "torque_nm": 340, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "trims_egypt": ["Executive", "Prestige"],
            "notes": "Discontinued; Middle East/Australia exclusive V6 sedan; used stock remains",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # HYUNDAI
    # ════════════════════════════════════════════════════════════════════

    "Hyundai": {
        "Elantra": {
            "first_year_global": 1990,
            "egypt_from": 1996,
            "assembled_in_egypt": True,
            "assembler": "GB Auto (Giza)",
            "body_types": ["sedan"],
            "segments": ["C-segment", "compact sedan"],
            "generations": [
                {"gen": "MD (5th)", "years": "2010-2016", "facelift": "2013"},
                {"gen": "AD (6th)", "years": "2015-2020", "facelift": "2018"},
                {"gen": "CN7 (7th)", "years": "2020-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L MPI", "hp": 123, "torque_nm": 151, "trans": ["auto 6-spd", "manual 6-spd"]},
                {"cc": 1999, "label": "2.0L MPI", "hp": 152, "torque_nm": 192, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 980_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 850_000, "max": 1_050_000},
            "trims_egypt": ["Comfort", "Smart", "Sport", "GLS"],
            "notes": "Top-3 best seller in Egypt; locally assembled by GB Auto",
        },
        "Tucson": {
            "first_year_global": 2004,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "TL (3rd)", "years": "2015-2020", "facelift": "2018"},
                {"gen": "NX4 (4th)", "years": "2020-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L T-GDI turbo", "hp": 180, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
                {"cc": 1999, "label": "2.0L MPI", "hp": 156, "torque_nm": 192, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_400_000, "max": 1_750_000},
            "trims_egypt": ["Smart", "GLS", "Sport"],
        },
        "Santa Fe": {
            "first_year_global": 2000,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "DM (3rd)", "years": "2012-2018", "facelift": "2015"},
                {"gen": "TM (4th)", "years": "2018-2023", "facelift": "2020"},
                {"gen": "MX (5th)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 2359, "label": "2.4L GDI", "hp": 188, "torque_nm": 241, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_600_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_250_000, "max": 2_800_000},
            "trims_egypt": ["GLS", "Sport"],
        },
        "Accent": {
            "first_year_global": 1994,
            "egypt_from": 2000,
            "assembled_in_egypt": True,
            "assembler": "GB Auto",
            "body_types": ["sedan", "hatchback"],
            "segments": ["B-segment", "subcompact"],
            "generations": [
                {"gen": "RB (4th)", "years": "2011-2017", "facelift": "2014"},
                {"gen": "HC (5th)", "years": "2017-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4L 4-cyl", "hp": 100, "torque_nm": 132, "trans": ["auto 6-spd", "manual 6-spd"]},
                {"cc": 1591, "label": "1.6L 4-cyl", "hp": 123, "torque_nm": 151, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 730_000, "max": 950_000},
            "new_price_egp_2024": {"min": 630_000, "max": 820_000},
            "trims_egypt": ["Standard", "Comfort", "Sport"],
            "notes": "Budget entry; sedan most popular in Egypt",
        },
        "Creta": {
            "first_year_global": 2015,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen SU2", "years": "2015-2020"},
                {"gen": "2nd gen SU2 facelift", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L MPI", "hp": 115, "torque_nm": 144, "trans": ["auto 6-spd"]},
                {"cc": 1591, "label": "1.6L T-GDI turbo", "hp": 138, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_500_000},
            "new_price_egp_2024": {"min": 1_050_000, "max": 1_300_000},
            "trims_egypt": ["Smart", "GLS", "Sport"],
        },
        "i10": {
            "first_year_global": 2007,
            "egypt_from": 2009,
            "assembled_in_egypt": True,
            "assembler": "GB Auto",
            "body_types": ["hatchback"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "PA (1st)", "years": "2007-2013"},
                {"gen": "IA (2nd)", "years": "2013-2019"},
                {"gen": "AC3 (3rd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 998, "label": "1.0L 3-cyl", "hp": 67, "torque_nm": 96, "trans": ["auto 5-AMT", "manual 5-spd"]},
                {"cc": 1197, "label": "1.2L 4-cyl", "hp": 83, "torque_nm": 114, "trans": ["auto 5-AMT"]},
            ],
            "new_price_egp_2025": {"min": 550_000, "max": 720_000},
            "new_price_egp_2024": {"min": 480_000, "max": 620_000},
            "trims_egypt": ["Standard", "Comfort"],
            "notes": "Cheapest new Hyundai in Egypt; popular budget city car",
        },
        "Grand i10": {
            "first_year_global": 2013,
            "egypt_from": 2015,
            "assembled_in_egypt": True,
            "assembler": "GB Auto",
            "body_types": ["hatchback", "sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "1st gen BA", "years": "2013-2019"},
                {"gen": "2nd gen BC3", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1197, "label": "1.2L 4-cyl", "hp": 83, "torque_nm": 114, "trans": ["auto 5-AMT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 600_000, "max": 780_000},
            "new_price_egp_2024": {"min": 520_000, "max": 680_000},
            "trims_egypt": ["GL", "GLS"],
        },
        "i20": {
            "first_year_global": 2008,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "PB (1st)", "years": "2008-2014"},
                {"gen": "GB (2nd)", "years": "2014-2020"},
                {"gen": "BC3 (3rd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1197, "label": "1.2L 4-cyl", "hp": 83, "torque_nm": 114, "trans": ["auto 5-AMT"]},
            ],
            "new_price_egp_2025": {"min": 620_000, "max": 780_000},
            "new_price_egp_2024": {"min": 540_000, "max": 680_000},
            "trims_egypt": ["Comfort"],
        },
        "i30": {
            "first_year_global": 2007,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "FD (1st)", "years": "2007-2011"},
                {"gen": "GD (2nd)", "years": "2011-2017"},
                {"gen": "PD (3rd)", "years": "2017-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L MPI", "hp": 128, "torque_nm": 157, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 780_000, "max": 960_000},
            "trims_egypt": ["Smart", "Sport"],
        },
        "Sonata": {
            "first_year_global": 1985,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "LF (7th)", "years": "2014-2019", "facelift": "2017"},
                {"gen": "DN8 (8th)", "years": "2019-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 1999, "label": "2.0L MPI", "hp": 152, "torque_nm": 192, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_580_000},
            "trims_egypt": ["Smart", "GLS"],
        },
        "Kona": {
            "first_year_global": 2017,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen OS", "years": "2017-2023"},
                {"gen": "2nd gen SX2", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L T-GDI turbo", "hp": 198, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_200_000, "max": 1_500_000},
            "trims_egypt": ["Sport"],
        },
        "Ioniq 5": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV", "crossover EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [
                {"gen": "1st gen NE (E-GMP)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 72.6kWh RWD", "hp": 218, "torque_nm": 350, "trans": ["single-speed"]},
                {"cc": 0, "label": "Electric 72.6kWh AWD", "hp": 305, "torque_nm": 605, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_900_000, "max": 2_450_000},
            "trims_egypt": ["Standard", "Long Range"],
            "notes": "First Hyundai EV launched in Egypt; 800V architecture",
        },
        "Staria": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["minivan", "MPV"],
            "segments": ["large MPV"],
            "generations": [
                {"gen": "1st gen US4", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 2199, "label": "2.2L diesel CRDi", "hp": 177, "torque_nm": 430, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_200_000, "max": 2_800_000},
            "trims_egypt": ["Premium", "Luxury"],
            "notes": "Replaces Starex/H1; prestige MPV for VIP transport",
        },
        "H1": {
            "first_year_global": 1997,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["minivan", "panel van"],
            "segments": ["large MPV", "commercial"],
            "generations": [
                {"gen": "TQ (2nd)", "years": "2007-2021"},
            ],
            "engines_egypt": [
                {"cc": 2497, "label": "2.5L CRDi diesel", "hp": 170, "torque_nm": 441, "trans": ["auto 5-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "trims_egypt": ["GL", "GLS"],
            "notes": "Discontinued new sales (replaced by Staria); massive fleet presence in Egypt",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # KIA
    # ════════════════════════════════════════════════════════════════════

    "Kia": {
        "Cerato": {
            "first_year_global": 2003,
            "egypt_from": 2005,
            "assembled_in_egypt": True,
            "assembler": "GB Auto",
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "LD (2nd)", "years": "2008-2012"},
                {"gen": "YD (3rd)", "years": "2013-2018", "facelift": "2016"},
                {"gen": "BD (4th)", "years": "2018-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L MPI", "hp": 128, "torque_nm": 157, "trans": ["auto 6-spd", "manual 6-spd"]},
                {"cc": 1999, "label": "2.0L MPI", "hp": 154, "torque_nm": 192, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 980_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 850_000, "max": 1_050_000},
            "trims_egypt": ["Comfort", "EX", "GT-Line"],
            "notes": "Sister car to Elantra; assembled locally by GB Auto",
        },
        "Sportage": {
            "first_year_global": 1993,
            "egypt_from": 2005,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "QL (4th)", "years": "2015-2021", "facelift": "2018"},
                {"gen": "NQ5 (5th)", "years": "2021-present", "facelift": "2024"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L T-GDI turbo", "hp": 177, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
                {"cc": 1999, "label": "2.0L MPI", "hp": 155, "torque_nm": 192, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_050_000},
            "new_price_egp_2024": {"min": 1_400_000, "max": 1_800_000},
            "trims_egypt": ["LX", "EX", "GT-Line"],
        },
        "Picanto": {
            "first_year_global": 2004,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "SA (1st)", "years": "2004-2011"},
                {"gen": "TA (2nd)", "years": "2011-2017"},
                {"gen": "JA (3rd)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 998, "label": "1.0L 3-cyl", "hp": 67, "torque_nm": 96, "trans": ["auto 4-spd", "manual 5-spd"]},
                {"cc": 1197, "label": "1.2L 4-cyl", "hp": 84, "torque_nm": 121, "trans": ["auto 4-spd"]},
            ],
            "new_price_egp_2025": {"min": 570_000, "max": 720_000},
            "new_price_egp_2024": {"min": 490_000, "max": 620_000},
            "trims_egypt": ["LX", "EX"],
        },
        "Sorento": {
            "first_year_global": 2002,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "XM (2nd)", "years": "2009-2014"},
                {"gen": "UM (3rd)", "years": "2014-2020", "facelift": "2017"},
                {"gen": "MQ4 (4th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 2359, "label": "2.4L GDI", "hp": 188, "torque_nm": 241, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_400_000, "max": 2_900_000},
            "new_price_egp_2024": {"min": 2_100_000, "max": 2_550_000},
            "trims_egypt": ["LX", "EX"],
        },
        "Sonet": {
            "first_year_global": 2020,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen QY", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L MPI", "hp": 115, "torque_nm": 144, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_150_000},
            "new_price_egp_2024": {"min": 820_000, "max": 1_000_000},
            "trims_egypt": ["LX", "EX"],
        },
        "Stinger": {
            "first_year_global": 2017,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["fastback sedan"],
            "segments": ["D-segment", "sports sedan"],
            "generations": [
                {"gen": "CK (1st)", "years": "2017-2023"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0L T-GDI turbo", "hp": 255, "torque_nm": 353, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_900_000, "max": 2_300_000},
            "trims_egypt": ["GT"],
            "notes": "Niche product in Egypt; limited units",
        },
        "Rio": {
            "first_year_global": 2000,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "UB (3rd)", "years": "2011-2017"},
                {"gen": "YB (4th)", "years": "2017-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4L MPI", "hp": 100, "torque_nm": 132, "trans": ["auto 6-spd", "manual 6-spd"]},
                {"cc": 1591, "label": "1.6L MPI", "hp": 123, "torque_nm": 151, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 660_000, "max": 830_000},
            "new_price_egp_2024": {"min": 575_000, "max": 720_000},
            "trims_egypt": ["LX", "EX"],
        },
        "K5": {
            "first_year_global": 2010,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "JF (2nd Optima)", "years": "2015-2020", "facelift": "2018"},
                {"gen": "DL3 (K5 3rd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6L T-GDI turbo", "hp": 180, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
                {"cc": 1999, "label": "2.0L MPI", "hp": 152, "torque_nm": 192, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_350_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_180_000, "max": 1_480_000},
            "trims_egypt": ["LX", "EX", "GT-Line"],
            "notes": "Formerly sold as Optima in Egypt",
        },
        "Carnival": {
            "first_year_global": 1998,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["minivan", "MPV"],
            "segments": ["large MPV"],
            "generations": [
                {"gen": "KA4 (4th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 2199, "label": "2.2L diesel CRDi", "hp": 202, "torque_nm": 440, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_300_000, "max": 2_900_000},
            "new_price_egp_2024": {"min": 2_000_000, "max": 2_550_000},
            "trims_egypt": ["EX", "SX"],
        },
        "Stonic": {
            "first_year_global": 2017,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "YB (1st)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4L MPI", "hp": 100, "torque_nm": 132, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 780_000, "max": 960_000},
            "trims_egypt": ["LX", "EX"],
        },
        "Niro": {
            "first_year_global": 2016,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover", "hybrid"],
            "segments": ["B-SUV", "hybrid"],
            "generations": [
                {"gen": "DE (1st)", "years": "2016-2022"},
                {"gen": "SG2 (2nd)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1580, "label": "1.6L hybrid GDI", "hp": 141, "torque_nm": 265, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_220_000, "max": 1_480_000},
            "trims_egypt": ["EX", "EX+"],
        },
        "EV6": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["crossover EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [
                {"gen": "1st gen CV (E-GMP)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 77.4kWh RWD", "hp": 229, "torque_nm": 350, "trans": ["single-speed"]},
                {"cc": 0, "label": "Electric 77.4kWh GT-Line AWD", "hp": 325, "torque_nm": 605, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_300_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 2_000_000, "max": 2_600_000},
            "trims_egypt": ["Standard", "GT-Line"],
        },
        "Telluride": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7/8-seater"],
            "segments": ["E-SUV"],
            "generations": [
                {"gen": "ON (1st)", "years": "2019-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 3778, "label": "3.8L V6 GDI", "hp": 291, "torque_nm": 355, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_200_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 2_800_000, "max": 3_500_000},
            "trims_egypt": ["EX", "SX"],
            "notes": "Premium large SUV; competes with Palisade/Explorer",
        },
        "Seltos": {
            "first_year_global": 2019,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2019-2023"},
                {"gen": "2nd gen", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1591, "label": "1.6 MPI naturally aspirated", "hp": 123, "torque_nm": 151, "trans": ["auto 6-spd IVT"]},
                {"cc": 1353, "label": "1.4T turbo", "hp": 140, "torque_nm": 242, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 609_000, "max": 826_000},
            "trims_egypt": ["EX", "GT Line"],
            "notes": "Growing B-SUV segment; competes with Creta and Captur",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # NISSAN
    # ════════════════════════════════════════════════════════════════════

    "Nissan": {
        "Sunny": {
            "first_year_global": 1966,
            "egypt_from": 1985,
            "assembled_in_egypt": True,
            "assembler": "Nasco – National Automotive Company",
            "body_types": ["sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "N17 (7th)", "years": "2011-present", "facelift": "2014/2020", "notes": "Produced continuously in Egypt"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L 4-cyl", "hp": 99, "torque_nm": 133, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 680_000, "max": 850_000},
            "new_price_egp_2024": {"min": 590_000, "max": 740_000},
            "trims_egypt": ["S", "SV", "SL"],
            "notes": "Staple of Egyptian fleet/taxi market",
        },
        "Sentra": {
            "first_year_global": 1982,
            "egypt_from": 2013,
            "assembled_in_egypt": True,
            "assembler": "Nasco",
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "B17 (7th)", "years": "2012-2019", "facelift": "2016"},
                {"gen": "B18 (8th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1597, "label": "1.6L 4-cyl", "hp": 117, "torque_nm": 159, "trans": ["auto CVT", "manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 840_000, "max": 1_020_000},
            "new_price_egp_2024": {"min": 720_000, "max": 890_000},
            "trims_egypt": ["S", "SV", "SL"],
        },
        "Qashqai": {
            "first_year_global": 2006,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "J10 (1st)", "years": "2006-2013", "facelift": "2010"},
                {"gen": "J11 (2nd)", "years": "2013-2021", "facelift": "2017"},
                {"gen": "J12 (3rd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "1.3L DiG-T turbo", "hp": 158, "torque_nm": 260, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_850_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_620_000},
            "trims_egypt": ["SV", "SL"],
        },
        "X-Trail": {
            "first_year_global": 2000,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV", "D-SUV"],
            "generations": [
                {"gen": "T31 (2nd)", "years": "2007-2013"},
                {"gen": "T32 (3rd)", "years": "2013-2022", "facelift": "2017"},
                {"gen": "T33 (4th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L VC-Turbo", "hp": 163, "torque_nm": 300, "trans": ["auto CVT"]},
                {"cc": 2488, "label": "2.5L 4-cyl", "hp": 184, "torque_nm": 237, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_750_000, "max": 2_250_000},
            "trims_egypt": ["SV", "SL"],
        },
        "Navara": {
            "first_year_global": 1985,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["pickup"],
            "generations": [
                {"gen": "D40 (3rd)", "years": "2004-2015"},
                {"gen": "D23 (4th)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 2298, "label": "2.3L diesel twin-turbo", "hp": 190, "torque_nm": 450, "trans": ["auto 7-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_100_000, "max": 2_500_000},
            "new_price_egp_2024": {"min": 1_850_000, "max": 2_200_000},
            "trims_egypt": ["SV", "SL"],
        },
        "Patrol": {
            "first_year_global": 1951,
            "egypt_from": 1985,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV", "full-size SUV"],
            "generations": [
                {"gen": "Y61", "years": "1997-2013"},
                {"gen": "Y62", "years": "2010-present", "facelift": "2014/2019"},
            ],
            "engines_egypt": [
                {"cc": 5552, "label": "5.6L V8 petrol", "hp": 400, "torque_nm": 560, "trans": ["auto 7-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 4_800_000, "max": 7_000_000},
            "trims_egypt": ["SE", "SL", "Platinum"],
            "notes": "Prestige 4x4; competes with Land Cruiser",
        },
        "March": {
            "first_year_global": 1982,
            "egypt_from": 2011,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "K13 (4th)", "years": "2010-present", "facelift": "2016"},
            ],
            "engines_egypt": [
                {"cc": 1198, "label": "1.2L 3-cyl", "hp": 80, "torque_nm": 107, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 480_000, "max": 620_000},
            "new_price_egp_2024": {"min": 415_000, "max": 540_000},
            "trims_egypt": ["S", "SV"],
            "notes": "Also known as Micra globally; budget city car",
        },
        "Kicks": {
            "first_year_global": 2016,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "P15 (1st)", "years": "2016-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1597, "label": "1.6L 4-cyl", "hp": 117, "torque_nm": 159, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_090_000},
            "trims_egypt": ["S", "SV"],
        },
        "Juke": {
            "first_year_global": 2010,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "F15 (1st)", "years": "2010-2019"},
                {"gen": "F16 (2nd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L DIG-T turbo", "hp": 117, "torque_nm": 180, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_180_000},
            "trims_egypt": ["SV", "SL"],
        },
        "Altima": {
            "first_year_global": 1992,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "L33 (5th)", "years": "2012-2018"},
                {"gen": "L34 (6th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 2488, "label": "2.5L 4-cyl", "hp": 188, "torque_nm": 244, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_350_000, "max": 1_650_000},
            "new_price_egp_2024": {"min": 1_180_000, "max": 1_440_000},
            "trims_egypt": ["SV", "SL", "Platinum"],
        },
        "Murano": {
            "first_year_global": 2002,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "Z52 (3rd)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 3498, "label": "3.5L V6", "hp": 260, "torque_nm": 340, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_100_000},
            "new_price_egp_2024": {"min": 2_200_000, "max": 2_700_000},
            "trims_egypt": ["SL", "Platinum"],
        },
        "Pathfinder": {
            "first_year_global": 1985,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "E-SUV"],
            "generations": [
                {"gen": "R52 (4th)", "years": "2012-2021"},
                {"gen": "R53 (5th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 3498, "label": "3.5L V6", "hp": 284, "torque_nm": 340, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 3_800_000},
            "new_price_egp_2024": {"min": 2_600_000, "max": 3_300_000},
            "trims_egypt": ["SV", "SL", "Platinum"],
        },
        "Armada": {
            "first_year_global": 2003,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8-seater"],
            "segments": ["F-SUV", "full-size SUV"],
            "generations": [
                {"gen": "WA60 (2nd)", "years": "2016-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 5552, "label": "5.6L V8", "hp": 400, "torque_nm": 560, "trans": ["auto 7-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 6_000_000},
            "new_price_egp_2024": {"min": 3_900_000, "max": 5_200_000},
            "trims_egypt": ["SL", "Platinum"],
        },
        "Titan": {
            "first_year_global": 2003,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["full-size pickup"],
            "generations": [
                {"gen": "A61 (2nd)", "years": "2015-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 5552, "label": "5.6L Endurance V8", "hp": 400, "torque_nm": 560, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 5_200_000},
            "new_price_egp_2024": {"min": 3_500_000, "max": 4_500_000},
            "trims_egypt": ["SV", "SL", "Platinum Reserve"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # VOLKSWAGEN
    # ════════════════════════════════════════════════════════════════════

    "Volkswagen": {
        "Polo": {
            "first_year_global": 1975,
            "egypt_from": 2009,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "Mk5 6R", "years": "2009-2017"},
                {"gen": "Mk6 AW", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TSI 95hp", "hp": 95, "torque_nm": 175, "trans": ["auto 6-spd DSG"]},
                {"cc": 999, "label": "1.0L TSI 110hp", "hp": 110, "torque_nm": 200, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 780_000, "max": 960_000},
            "trims_egypt": ["Comfortline", "Highline"],
        },
        "Golf": {
            "first_year_global": 1974,
            "egypt_from": 2005,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "Mk7 (7th)", "years": "2012-2019", "facelift": "2017"},
                {"gen": "Mk8 (8th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.4L TSI", "hp": 125, "torque_nm": 200, "trans": ["auto 7-spd DSG"]},
                {"cc": 1984, "label": "2.0L TSI GTI", "hp": 245, "torque_nm": 370, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_570_000},
            "trims_egypt": ["Comfortline", "Highline", "GTI"],
        },
        "Jetta": {
            "first_year_global": 1979,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment", "compact sedan"],
            "generations": [
                {"gen": "Mk6 (6th)", "years": "2010-2018"},
                {"gen": "Mk7 (7th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.4L TSI", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_130_000},
            "trims_egypt": ["Comfortline", "Highline"],
        },
        "Passat": {
            "first_year_global": 1973,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "B7 (7th)", "years": "2010-2014"},
                {"gen": "B8 (8th)", "years": "2014-2023", "facelift": "2019"},
                {"gen": "B9 (9th)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.4L TSI", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
                {"cc": 1984, "label": "2.0L TSI", "hp": 220, "torque_nm": 350, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_100_000},
            "new_price_egp_2024": {"min": 1_400_000, "max": 1_850_000},
            "trims_egypt": ["Comfortline", "Highline"],
        },
        "Tiguan": {
            "first_year_global": 2007,
            "egypt_from": 2009,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "Mk1 5N", "years": "2007-2016", "facelift": "2011"},
                {"gen": "Mk2 AD1", "years": "2016-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.4L TSI", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
                {"cc": 1984, "label": "2.0L TSI", "hp": 220, "torque_nm": 350, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_750_000, "max": 2_300_000},
            "trims_egypt": ["Comfortline", "Highline"],
        },
        "T-Roc": {
            "first_year_global": 2017,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "A11 (1st)", "years": "2017-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.4L TSI", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_650_000},
            "trims_egypt": ["Comfortline", "R-Line"],
        },
        "Touareg": {
            "first_year_global": 2002,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "premium SUV"],
            "generations": [
                {"gen": "CR (3rd)", "years": "2018-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 2996, "label": "3.0L V6 TSI", "hp": 340, "torque_nm": 450, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 2_600_000, "max": 3_500_000},
            "trims_egypt": ["Elegance", "R-Line"],
        },
        "Teramont": {
            "first_year_global": 2016,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV", "large SUV"],
            "generations": [
                {"gen": "1st gen CA1", "years": "2016-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "2.0L TSI turbo", "hp": 220, "torque_nm": 350, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 2_800_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 2_450_000, "max": 3_100_000},
            "trims_egypt": ["Comfortline", "Highline", "R-Line"],
        },
        "ID.4": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [
                {"gen": "1st gen E21", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 77kWh RWD", "hp": 204, "torque_nm": 310, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_500_000},
            "new_price_egp_2024": {"min": 1_750_000, "max": 2_200_000},
            "trims_egypt": ["Pro"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # MG (SAIC)
    # ════════════════════════════════════════════════════════════════════

    "MG": {
        "MG3": {
            "first_year_global": 2011,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "2nd gen", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L 4-cyl VTi", "hp": 106, "torque_nm": 150, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 450_000, "max": 600_000},
            "new_price_egp_2024": {"min": 390_000, "max": 520_000},
            "trims_egypt": ["Comfort", "Luxury"],
            "notes": "One of cheapest new cars in Egypt",
        },
        "MG5": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "1st gen", "years": "2019-2023"},
                {"gen": "2nd gen", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1490, "label": "1.5L 4-cyl", "hp": 106, "torque_nm": 150, "trans": ["auto CVT"]},
                {"cc": 1498, "label": "1.5L turbo", "hp": 162, "torque_nm": 250, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 600_000, "max": 800_000},
            "new_price_egp_2024": {"min": 520_000, "max": 700_000},
            "trims_egypt": ["Standard", "Luxury", "Trophy"],
            "notes": "Explosive growth in Egypt; excellent value",
        },
        "MG6": {
            "first_year_global": 2009,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["fastback sedan"],
            "segments": ["D-segment", "sports sedan"],
            "generations": [
                {"gen": "3rd gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 174, "torque_nm": 285, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 780_000, "max": 960_000},
            "trims_egypt": ["Trophy"],
        },
        "MG GT": {
            "first_year_global": 2014,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "2nd gen", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 169, "torque_nm": 250, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 900_000},
            "new_price_egp_2024": {"min": 610_000, "max": 785_000},
            "trims_egypt": ["Luxury", "Trophy"],
        },
        "ZS": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen EZS", "years": "2017-2021"},
                {"gen": "2nd gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1490, "label": "1.5L 4-cyl", "hp": 106, "torque_nm": 150, "trans": ["auto CVT"]},
                {"cc": 1498, "label": "1.5T turbo", "hp": 161, "torque_nm": 250, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 600_000, "max": 830_000},
            "trims_egypt": ["Comfort", "Luxury", "Trophy"],
        },
        "MG4 EV": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback EV"],
            "segments": ["C-segment", "electric"],
            "generations": [
                {"gen": "1st gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 51kWh", "hp": 170, "torque_nm": 250, "trans": ["single-speed"]},
                {"cc": 0, "label": "Electric 64kWh", "hp": 204, "torque_nm": 250, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 800_000, "max": 1_050_000},
            "trims_egypt": ["Standard", "Long Range"],
        },
        "RX5": {
            "first_year_global": 2016,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "2nd gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 169, "torque_nm": 275, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_100_000},
            "trims_egypt": ["Luxury", "Trophy"],
        },
        "HS": {
            "first_year_global": 2018,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "D-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2018-2023"},
                {"gen": "2nd gen", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 224, "torque_nm": 360, "trans": ["auto 8-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_150_000, "max": 1_400_000},
            "trims_egypt": ["Trophy", "Exclusive"],
        },
        "One": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 169, "torque_nm": 275, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_220_000},
            "trims_egypt": ["Luxury", "Trophy"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # CHERY
    # ════════════════════════════════════════════════════════════════════

    "Chery": {
        "Arrizo 5": {
            "first_year_global": 2015,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "1st gen", "years": "2015-2021"},
                {"gen": "2nd gen Pro", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 145, "torque_nm": 210, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 480_000, "max": 640_000},
            "new_price_egp_2024": {"min": 415_000, "max": 555_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "Arrizo 6 Pro": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 145, "torque_nm": 210, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 580_000, "max": 750_000},
            "new_price_egp_2024": {"min": 500_000, "max": 650_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "Tiggo 2 Pro": {
            "first_year_global": 2020,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["A-SUV", "B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 145, "torque_nm": 210, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 520_000, "max": 700_000},
            "new_price_egp_2024": {"min": 450_000, "max": 610_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "Tiggo 4 Pro": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 145, "torque_nm": 210, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 650_000, "max": 850_000},
            "new_price_egp_2024": {"min": 560_000, "max": 740_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "Tiggo 7 Pro": {
            "first_year_global": 2020,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 197, "torque_nm": 350, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 820_000, "max": 1_050_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
        "Tiggo 8 Pro": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 254, "torque_nm": 390, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_550_000},
            "new_price_egp_2024": {"min": 1_050_000, "max": 1_350_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # GEELY
    # ════════════════════════════════════════════════════════════════════

    "Geely": {
        "Emgrand": {
            "first_year_global": 2009,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "EC7 (1st)", "years": "2009-2016"},
                {"gen": "EC715 (2nd)", "years": "2016-2022"},
                {"gen": "EC715 (3rd)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L 4-cyl", "hp": 102, "torque_nm": 143, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 480_000, "max": 650_000},
            "new_price_egp_2024": {"min": 415_000, "max": 565_000},
            "trims_egypt": ["Comfort", "Premium"],
            "notes": "Budget Chinese sedan; very affordable entry point",
        },
        "Coolray": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "SX11", "years": "2019-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 177, "torque_nm": 255, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 900_000},
            "new_price_egp_2024": {"min": 600_000, "max": 780_000},
            "trims_egypt": ["Sport", "Premium"],
        },
        "Tugella": {
            "first_year_global": 2019,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "FY11", "years": "2019-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 218, "torque_nm": 325, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_130_000},
            "trims_egypt": ["Premium"],
        },
        "Okavango": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 218, "torque_nm": 325, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_550_000},
            "new_price_egp_2024": {"min": 1_050_000, "max": 1_350_000},
            "trims_egypt": ["Luxury", "Premium"],
        },
        "Atlas Pro": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "JL6 (2nd gen)", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 238, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_220_000},
            "trims_egypt": ["Premium"],
        },
        "Preface": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment"],
            "generations": [{"gen": "1st gen KD3", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 177, "torque_nm": 255, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 780_000, "max": 1_000_000},
            "new_price_egp_2024": {"min": 680_000, "max": 870_000},
            "trims_egypt": ["Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # BYD
    # ════════════════════════════════════════════════════════════════════

    "BYD": {
        "Dolphin": {
            "first_year_global": 2021,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback EV"],
            "segments": ["B-segment", "electric"],
            "generations": [{"gen": "EA1 (1st)", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 44.9kWh", "hp": 95, "torque_nm": 180, "trans": ["single-speed"]},
                {"cc": 0, "label": "Electric 60.4kWh", "hp": 177, "torque_nm": 310, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 620_000, "max": 830_000},
            "trims_egypt": ["Comfort", "Boost"],
        },
        "Atto 3": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 60kWh", "hp": 204, "torque_nm": 310, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_600_000},
            "trims_egypt": ["Standard Range", "Extended Range"],
        },
        "Han": {
            "first_year_global": 2020,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["D-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 85.4kWh RWD", "hp": 286, "torque_nm": 360, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_920_000, "max": 2_450_000},
            "trims_egypt": ["DM-i", "EV"],
        },
        "Seal": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["D-segment", "electric"],
            "generations": [{"gen": "1st gen EA1", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 82.56kWh RWD", "hp": 313, "torque_nm": 360, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_500_000},
            "new_price_egp_2024": {"min": 1_800_000, "max": 2_200_000},
            "trims_egypt": ["Dynamic", "Excellence"],
        },
        "Tang": {
            "first_year_global": 2015,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater", "PHEV"],
            "segments": ["D-SUV", "plug-in hybrid"],
            "generations": [{"gen": "2nd gen (DM)", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1494, "label": "1.5T PHEV DM-i", "hp": 505, "torque_nm": 650, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_750_000, "max": 2_270_000},
            "trims_egypt": ["DM-i 6-seater", "DM-i 7-seater"],
        },
        "Song Plus": {
            "first_year_global": 2021,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "PHEV"],
            "segments": ["C-SUV", "plug-in hybrid"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1494, "label": "1.5L + EV PHEV DM-i", "hp": 326, "torque_nm": 316, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_400_000, "max": 1_750_000},
            "trims_egypt": ["DM-i"],
        },
        "Sealion 6": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "PHEV"],
            "segments": ["C-SUV", "plug-in hybrid"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1494, "label": "1.5T PHEV DM-i", "hp": 316, "torque_nm": 500, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_660_000},
            "trims_egypt": ["DM-i"],
        },
        "Yuan Plus": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["B-SUV", "electric"],
            "generations": [{"gen": "1st gen BYD EV", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 60.48kWh", "hp": 204, "torque_nm": 310, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_220_000},
            "trims_egypt": ["Boost"],
        },
        "Shark 6": {
            "first_year_global": 2024,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck", "PHEV"],
            "segments": ["pickup", "hybrid"],
            "generations": [{"gen": "1st gen", "years": "2024-present"}],
            "engines_egypt": [
                {"cc": 1994, "label": "2.0T + EV PHEV", "hp": 433, "torque_nm": 650, "trans": ["auto 3-spd DHT"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_392_000, "max": 1_740_000},
            "trims_egypt": ["Standard", "Premium"],
            "notes": "First PHEV pickup in Egypt; competes with Hilux/Ranger",
        },
        "Sealion 5": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "PHEV"],
            "segments": ["C-SUV", "hybrid"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5T DM-i PHEV", "hp": 177, "torque_nm": 231, "trans": ["auto e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_220_000},
            "trims_egypt": ["DM-i Active", "DM-i Comfort"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # CHEVROLET
    # ════════════════════════════════════════════════════════════════════

    "Chevrolet": {
        "Lanos": {
            "first_year_global": 1997,
            "egypt_from": 1999,
            "assembled_in_egypt": True,
            "assembler": "GM Egypt / later United Car Industries",
            "body_types": ["sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "1st (T150)", "years": "1997-2004"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L 4-cyl", "hp": 86, "torque_nm": 128, "trans": ["manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued; budget entry used market staple",
        },
        "Aveo": {
            "first_year_global": 2002,
            "egypt_from": 2005,
            "assembled_in_egypt": True,
            "assembler": "GM Egypt",
            "body_types": ["sedan", "hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "T250 (1st)", "years": "2002-2011"},
                {"gen": "T300 (2nd)", "years": "2011-2015"},
            ],
            "engines_egypt": [
                {"cc": 1399, "label": "1.4L 4-cyl", "hp": 101, "torque_nm": 130, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued; still common in Egyptian market used",
        },
        "Optra": {
            "first_year_global": 2002,
            "egypt_from": 2004,
            "assembled_in_egypt": True,
            "assembler": "GM Egypt",
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "J200 (1st)", "years": "2002-2008"},
                {"gen": "J300/Cruze", "years": "2008-2015"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L 4-cyl", "hp": 113, "torque_nm": 150, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued new sales; iconic budget car in Egypt",
        },
        "Spark": {
            "first_year_global": 2009,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "M300 (2nd)", "years": "2009-2015"},
                {"gen": "M400 (3rd)", "years": "2015-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L 3-cyl", "hp": 65, "torque_nm": 90, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 420_000, "max": 570_000},
            "new_price_egp_2024": {"min": 365_000, "max": 495_000},
            "trims_egypt": ["LS", "LT"],
            "notes": "Entry-level Chevrolet; budget city car",
        },
        "Malibu": {
            "first_year_global": 1964,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "Mk8 (8th)", "years": "2012-2015"},
                {"gen": "Mk9 (9th)", "years": "2015-present"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "1.5L turbo", "hp": 163, "torque_nm": 245, "trans": ["auto 6-spd"]},
                {"cc": 1998, "label": "2.0L turbo", "hp": 250, "torque_nm": 353, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_500_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_310_000},
            "trims_egypt": ["LS", "LT", "Premier"],
        },
        "Equinox": {
            "first_year_global": 2004,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "3rd gen (2nd ME)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L turbo", "hp": 170, "torque_nm": 249, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_550_000},
            "new_price_egp_2024": {"min": 1_050_000, "max": 1_350_000},
            "trims_egypt": ["LS", "LT"],
        },
        "Captiva": {
            "first_year_global": 2006,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "C140 (1st)", "years": "2006-2018", "facelift": "2011"},
                {"gen": "2nd gen", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0L diesel turbo", "hp": 150, "torque_nm": 320, "trans": ["auto 6-spd"]},
                {"cc": 2384, "label": "2.4L petrol", "hp": 136, "torque_nm": 220, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 950_000, "max": 1_200_000},
            "trims_egypt": ["LS", "LT", "LTZ"],
        },
        "Colorado": {
            "first_year_global": 2004,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["mid-size pickup"],
            "generations": [
                {"gen": "2nd gen GMT31XX", "years": "2015-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 2781, "label": "2.8L Duramax diesel", "hp": 200, "torque_nm": 500, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_270_000},
            "trims_egypt": ["LT", "LTZ", "Z71"],
        },
        "Blazer": {
            "first_year_global": 2018,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2018-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0L turbo", "hp": 228, "torque_nm": 350, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_300_000, "max": 1_650_000},
            "trims_egypt": ["LT", "RS"],
        },
        "Tahoe": {
            "first_year_global": 1994,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8-seater"],
            "segments": ["F-SUV", "full-size SUV"],
            "generations": [
                {"gen": "K2 (4th)", "years": "2014-2020"},
                {"gen": "K2 (5th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 5328, "label": "5.3L EcoTec3 V8", "hp": 355, "torque_nm": 519, "trans": ["auto 10-spd"]},
                {"cc": 6162, "label": "6.2L EcoTec3 V8", "hp": 420, "torque_nm": 623, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 5_800_000},
            "new_price_egp_2024": {"min": 3_500_000, "max": 5_050_000},
            "trims_egypt": ["LS", "LT", "LTZ", "High Country"],
        },
        "Suburban": {
            "first_year_global": 1935,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8/9-seater"],
            "segments": ["F-SUV", "full-size SUV"],
            "generations": [
                {"gen": "K2 (11th)", "years": "2014-2020"},
                {"gen": "T1 (12th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 5328, "label": "5.3L EcoTec3 V8", "hp": 355, "torque_nm": 519, "trans": ["auto 10-spd"]},
                {"cc": 6162, "label": "6.2L EcoTec3 V8", "hp": 420, "torque_nm": 623, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 6_500_000},
            "new_price_egp_2024": {"min": 3_900_000, "max": 5_650_000},
            "trims_egypt": ["LS", "LT", "LTZ", "High Country"],
        },
        "Traverse": {
            "first_year_global": 2008,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV"],
            "generations": [
                {"gen": "C1 (2nd)", "years": "2017-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 3564, "label": "3.6L V6", "hp": 310, "torque_nm": 367, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_800_000, "max": 3_400_000},
            "new_price_egp_2024": {"min": 2_450_000, "max": 3_000_000},
            "trims_egypt": ["LS", "LT", "Premier"],
        },
        "Camaro": {
            "first_year_global": 1966,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe", "convertible"],
            "segments": ["sports car", "pony car"],
            "generations": [
                {"gen": "6th gen Alpha", "years": "2015-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0L turbo", "hp": 275, "torque_nm": 400, "trans": ["auto 8-spd"]},
                {"cc": 6162, "label": "6.2L V8 SS", "hp": 455, "torque_nm": 617, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_200_000},
            "new_price_egp_2024": {"min": 2_180_000, "max": 3_660_000},
            "trims_egypt": ["1LT", "2LT", "SS"],
        },
        "Silverado": {
            "first_year_global": 1998,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["full-size pickup"],
            "generations": [
                {"gen": "K2 (3rd)", "years": "2013-2018"},
                {"gen": "T1 (4th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 5328, "label": "5.3L V8 EcoTec3", "hp": 355, "torque_nm": 519, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 3_480_000, "max": 4_800_000},
            "trims_egypt": ["LT", "LTZ", "High Country"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # BMW
    # ════════════════════════════════════════════════════════════════════

    "BMW": {
        "1 Series": {
            "first_year_global": 2004,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment", "premium"],
            "generations": [
                {"gen": "F20 (2nd)", "years": "2011-2019"},
                {"gen": "F40 (3rd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "118i 1.5T 3-cyl", "hp": 140, "torque_nm": 220, "trans": ["auto 7-spd DCT"]},
                {"cc": 1998, "label": "120i 2.0T", "hp": 178, "torque_nm": 280, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_440_000},
            "trims_egypt": ["118i", "120i", "M Sport"],
        },
        "2 Series": {
            "first_year_global": 2014,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe", "convertible", "gran coupe"],
            "segments": ["D-segment", "premium coupe"],
            "generations": [
                {"gen": "F22 (1st coupe)", "years": "2013-2021"},
                {"gen": "G42 (2nd coupe)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "220i 2.0T", "hp": 184, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 2998, "label": "M240i 3.0T", "hp": 374, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_200_000},
            "new_price_egp_2024": {"min": 2_180_000, "max": 3_660_000},
            "trims_egypt": ["220i", "M240i", "M Sport"],
        },
        "3 Series": {
            "first_year_global": 1975,
            "egypt_from": 1990,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "touring"],
            "segments": ["D-segment", "sports sedan", "premium"],
            "generations": [
                {"gen": "F30 (6th)", "years": "2011-2019", "facelift": "2015"},
                {"gen": "G20 (7th)", "years": "2018-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "320i 2.0T", "hp": 184, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 1998, "label": "330i 2.0T", "hp": 258, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_800_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_400_000, "max": 3_900_000},
            "trims_egypt": ["320i", "330i", "M Sport"],
        },
        "4 Series": {
            "first_year_global": 2013,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe", "gran coupe", "convertible"],
            "segments": ["D-segment", "premium coupe"],
            "generations": [
                {"gen": "F32 (1st)", "years": "2013-2020"},
                {"gen": "G22 (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "420i 2.0T", "hp": 184, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 2998, "label": "M440i 3.0T", "hp": 374, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 2_600_000, "max": 4_800_000},
            "trims_egypt": ["420i", "430i", "M440i", "M Sport"],
        },
        "5 Series": {
            "first_year_global": 1972,
            "egypt_from": 1995,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["E-segment", "executive sedan", "premium"],
            "generations": [
                {"gen": "F10 (6th)", "years": "2009-2016", "facelift": "2013"},
                {"gen": "G30 (7th)", "years": "2016-2023", "facelift": "2020"},
                {"gen": "G60 (8th)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "520i 2.0T", "hp": 184, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 2998, "label": "530i 3.0T", "hp": 252, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 7_000_000},
            "new_price_egp_2024": {"min": 3_500_000, "max": 6_100_000},
            "trims_egypt": ["520i", "530i", "M Sport"],
        },
        "7 Series": {
            "first_year_global": 1977,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["F-segment", "luxury sedan"],
            "generations": [
                {"gen": "G11 (6th)", "years": "2015-2022", "facelift": "2019"},
                {"gen": "G70 (7th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 2998, "label": "740i 3.0T", "hp": 381, "torque_nm": 520, "trans": ["auto 8-spd"]},
                {"cc": 2998, "label": "750i 4.4L V8", "hp": 530, "torque_nm": 750, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 7_000_000, "max": 12_000_000},
            "new_price_egp_2024": {"min": 6_100_000, "max": 10_450_000},
            "trims_egypt": ["740i", "750i", "M Sport"],
        },
        "X1": {
            "first_year_global": 2009,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "premium"],
            "generations": [
                {"gen": "F48 (2nd)", "years": "2015-2022"},
                {"gen": "U11 (3rd)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "sDrive18i 1.5T", "hp": 136, "torque_nm": 220, "trans": ["auto 7-spd DCT"]},
                {"cc": 1998, "label": "sDrive20i 2.0T", "hp": 204, "torque_nm": 300, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_610_000},
            "trims_egypt": ["sDrive18i", "sDrive20i", "M Sport"],
        },
        "X2": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV coupe"],
            "segments": ["B-SUV", "premium"],
            "generations": [
                {"gen": "F39 (1st)", "years": "2017-2023"},
                {"gen": "U10 (2nd)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "sDrive20i 2.0T", "hp": 192, "torque_nm": 280, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 2_300_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_000_000, "max": 2_790_000},
            "trims_egypt": ["sDrive20i", "M Sport"],
        },
        "X3": {
            "first_year_global": 2003,
            "egypt_from": 2005,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "F25 (2nd)", "years": "2010-2017"},
                {"gen": "G01 (3rd)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "xDrive20i 2.0T", "hp": 184, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 2998, "label": "xDrive30i 3.0T", "hp": 272, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_200_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 2_780_000, "max": 4_790_000},
            "trims_egypt": ["xDrive20i", "xDrive30i", "M Sport"],
        },
        "X4": {
            "first_year_global": 2014,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV coupe"],
            "segments": ["C-SUV", "premium coupe"],
            "generations": [
                {"gen": "F26 (1st)", "years": "2014-2018"},
                {"gen": "G02 (2nd)", "years": "2018-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "xDrive20i 2.0T", "hp": 184, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 2998, "label": "xDrive30i 3.0T", "hp": 272, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 5_800_000},
            "new_price_egp_2024": {"min": 3_050_000, "max": 5_050_000},
            "trims_egypt": ["xDrive20i", "xDrive30i", "M Sport"],
        },
        "X5": {
            "first_year_global": 1999,
            "egypt_from": 2001,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "premium SUV"],
            "generations": [
                {"gen": "E70 (2nd)", "years": "2006-2013"},
                {"gen": "F15 (3rd)", "years": "2013-2018"},
                {"gen": "G05 (4th)", "years": "2018-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 2998, "label": "xDrive40i 3.0T", "hp": 340, "torque_nm": 450, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 6_960_000},
            "trims_egypt": ["xDrive40i", "M Sport"],
        },
        "X6": {
            "first_year_global": 2008,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV coupe"],
            "segments": ["D-SUV", "premium coupe SUV"],
            "generations": [
                {"gen": "E71 (1st)", "years": "2008-2014"},
                {"gen": "F16 (2nd)", "years": "2014-2019"},
                {"gen": "G06 (3rd)", "years": "2019-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 2998, "label": "xDrive40i 3.0T", "hp": 340, "torque_nm": 450, "trans": ["auto 8-spd"]},
                {"cc": 4395, "label": "M50i V8", "hp": 530, "torque_nm": 750, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 9_000_000},
            "new_price_egp_2024": {"min": 4_790_000, "max": 7_830_000},
            "trims_egypt": ["xDrive40i", "M50i", "M Sport"],
        },
        "X7": {
            "first_year_global": 2018,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["F-SUV", "luxury SUV"],
            "generations": [
                {"gen": "G07 (1st)", "years": "2018-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 2998, "label": "xDrive40i 3.0T", "hp": 381, "torque_nm": 520, "trans": ["auto 8-spd"]},
                {"cc": 4395, "label": "M60i V8", "hp": 530, "torque_nm": 750, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 7_000_000, "max": 12_000_000},
            "new_price_egp_2024": {"min": 6_090_000, "max": 10_440_000},
            "trims_egypt": ["xDrive40i", "M60i", "M Sport"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # MERCEDES-BENZ
    # ════════════════════════════════════════════════════════════════════

    "Mercedes-Benz": {
        "A-Class": {
            "first_year_global": 1997,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment", "premium"],
            "generations": [
                {"gen": "W177 (4th)", "years": "2018-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "A200 1.3T", "hp": 163, "torque_nm": 250, "trans": ["auto 7G-DCT"]},
                {"cc": 1991, "label": "A250 2.0T", "hp": 224, "torque_nm": 350, "trans": ["auto 7G-DCT"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_610_000},
            "trims_egypt": ["A200", "A250", "AMG Line"],
        },
        "CLA": {
            "first_year_global": 2013,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe sedan"],
            "segments": ["C-segment", "premium coupe"],
            "generations": [
                {"gen": "C117 (1st)", "years": "2013-2019"},
                {"gen": "C118 (2nd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "CLA200 1.3T", "hp": 163, "torque_nm": 250, "trans": ["auto 7G-DCT"]},
                {"cc": 1991, "label": "CLA250 2.0T", "hp": 224, "torque_nm": 350, "trans": ["auto 7G-DCT"]},
            ],
            "new_price_egp_2025": {"min": 2_300_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 2_000_000, "max": 3_050_000},
            "trims_egypt": ["CLA200", "CLA250", "AMG Line"],
        },
        "C-Class": {
            "first_year_global": 1993,
            "egypt_from": 1998,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "coupe", "estate"],
            "segments": ["D-segment", "premium"],
            "generations": [
                {"gen": "W204 (3rd)", "years": "2007-2014"},
                {"gen": "W205 (4th)", "years": "2014-2021"},
                {"gen": "W206 (5th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1991, "label": "C200 2.0T", "hp": 204, "torque_nm": 300, "trans": ["auto 9G-Tronic"]},
                {"cc": 1991, "label": "C300 2.0T", "hp": 258, "torque_nm": 400, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 3_200_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 2_780_000, "max": 4_790_000},
            "trims_egypt": ["C200", "C300", "AMG Line"],
        },
        "E-Class": {
            "first_year_global": 1953,
            "egypt_from": 1990,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "estate", "coupe"],
            "segments": ["E-segment", "executive sedan", "premium"],
            "generations": [
                {"gen": "W212 (5th)", "years": "2009-2016"},
                {"gen": "W213 (6th)", "years": "2016-2023"},
                {"gen": "W214 (7th)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1991, "label": "E200 2.0T", "hp": 204, "torque_nm": 300, "trans": ["auto 9G-Tronic"]},
                {"cc": 1991, "label": "E300 2.0T", "hp": 258, "torque_nm": 400, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 9_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 7_830_000},
            "trims_egypt": ["E200", "E300", "AMG Line"],
        },
        "GLA": {
            "first_year_global": 2013,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "premium"],
            "generations": [
                {"gen": "X156 (1st)", "years": "2013-2020"},
                {"gen": "H247 (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "GLA200 1.3T", "hp": 163, "torque_nm": 250, "trans": ["auto 7G-DCT"]},
                {"cc": 1991, "label": "GLA250 2.0T", "hp": 224, "torque_nm": 350, "trans": ["auto 7G-DCT"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_800_000},
            "new_price_egp_2024": {"min": 2_180_000, "max": 3_310_000},
            "trims_egypt": ["GLA200", "GLA250", "AMG Line"],
        },
        "GLB": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "X247 (1st)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "GLB200 1.3T", "hp": 163, "torque_nm": 250, "trans": ["auto 7G-DCT"]},
                {"cc": 1991, "label": "GLB250 2.0T", "hp": 224, "torque_nm": 350, "trans": ["auto 7G-DCT"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 3_920_000},
            "trims_egypt": ["GLB200", "GLB250", "AMG Line"],
        },
        "GLC": {
            "first_year_global": 2015,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "X253 (1st)", "years": "2015-2022"},
                {"gen": "X254 (2nd)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1991, "label": "GLC200 2.0T", "hp": 204, "torque_nm": 300, "trans": ["auto 9G-Tronic"]},
                {"cc": 1991, "label": "GLC300 2.0T", "hp": 258, "torque_nm": 400, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 6_000_000},
            "new_price_egp_2024": {"min": 3_050_000, "max": 5_220_000},
            "trims_egypt": ["GLC200", "GLC300", "AMG Line"],
        },
        "GLE": {
            "first_year_global": 1997,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "premium SUV"],
            "generations": [
                {"gen": "W166 (ML3)", "years": "2011-2019"},
                {"gen": "V167 (GLE)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1991, "label": "GLE300d diesel", "hp": 245, "torque_nm": 500, "trans": ["auto 9G-Tronic"]},
                {"cc": 2999, "label": "GLE450 3.0T", "hp": 367, "torque_nm": 500, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 10_000_000},
            "new_price_egp_2024": {"min": 4_790_000, "max": 8_700_000},
            "trims_egypt": ["GLE300d", "GLE450", "AMG Line"],
        },
        "GLS": {
            "first_year_global": 2012,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["F-SUV", "luxury SUV"],
            "generations": [
                {"gen": "X166 (2nd)", "years": "2012-2019"},
                {"gen": "X167 (3rd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 2999, "label": "GLS450 3.0T MHEV", "hp": 367, "torque_nm": 500, "trans": ["auto 9G-Tronic"]},
                {"cc": 3982, "label": "GLS580 V8 MHEV", "hp": 489, "torque_nm": 700, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 7_000_000, "max": 13_000_000},
            "new_price_egp_2024": {"min": 6_090_000, "max": 11_310_000},
            "trims_egypt": ["GLS450", "GLS580", "AMG Line"],
        },
        "G-Class": {
            "first_year_global": 1979,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["off-road SUV"],
            "segments": ["off-road", "luxury", "iconic"],
            "generations": [
                {"gen": "W463 (2nd)", "years": "1990-2018"},
                {"gen": "W463A (3rd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 3982, "label": "G500 V8 MHEV", "hp": 422, "torque_nm": 610, "trans": ["auto 9G-Tronic"]},
                {"cc": 3982, "label": "AMG G63 V8 bi-turbo", "hp": 585, "torque_nm": 850, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 10_000_000, "max": 18_000_000},
            "new_price_egp_2024": {"min": 8_700_000, "max": 15_660_000},
            "trims_egypt": ["G500", "AMG G63"],
            "notes": "Ultimate status symbol in Egypt; heavily customized market",
        },
        "S-Class": {
            "first_year_global": 1972,
            "egypt_from": 1995,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["F-segment", "luxury sedan"],
            "generations": [
                {"gen": "W222 (6th)", "years": "2013-2020"},
                {"gen": "W223 (7th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 2999, "label": "S450 3.0T MHEV", "hp": 367, "torque_nm": 500, "trans": ["auto 9G-Tronic"]},
                {"cc": 3982, "label": "S580 V8 MHEV", "hp": 503, "torque_nm": 700, "trans": ["auto 9G-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 9_000_000, "max": 18_000_000},
            "new_price_egp_2024": {"min": 7_830_000, "max": 15_660_000},
            "trims_egypt": ["S450", "S580", "Maybach"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # AUDI
    # ════════════════════════════════════════════════════════════════════

    "Audi": {
        "A3": {
            "first_year_global": 1996,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment", "premium"],
            "generations": [
                {"gen": "8V (3rd)", "years": "2012-2020"},
                {"gen": "8Y (4th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "35 TFSI 1.4T", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd S-Tronic"]},
                {"cc": 1984, "label": "40 TFSI 2.0T", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd S-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_610_000},
            "trims_egypt": ["35 TFSI", "40 TFSI", "S Line"],
        },
        "A4": {
            "first_year_global": 1994,
            "egypt_from": 2001,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "avant"],
            "segments": ["D-segment", "premium"],
            "generations": [
                {"gen": "B8 (4th)", "years": "2007-2015"},
                {"gen": "B9 (5th)", "years": "2015-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "35 TFSI 1.4T", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd S-Tronic"]},
                {"cc": 1984, "label": "40 TFSI 2.0T", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd S-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 3_920_000},
            "trims_egypt": ["35 TFSI", "40 TFSI", "S Line"],
        },
        "A5": {
            "first_year_global": 2007,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe", "sportback", "cabriolet"],
            "segments": ["D-segment", "premium coupe"],
            "generations": [
                {"gen": "8T (1st)", "years": "2007-2016"},
                {"gen": "F5 (2nd)", "years": "2016-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "40 TFSI 2.0T", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd S-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 5_200_000},
            "new_price_egp_2024": {"min": 3_050_000, "max": 4_530_000},
            "trims_egypt": ["40 TFSI", "S Line"],
        },
        "A6": {
            "first_year_global": 1994,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "avant"],
            "segments": ["E-segment", "premium"],
            "generations": [
                {"gen": "C7 (4th)", "years": "2011-2018", "facelift": "2014"},
                {"gen": "C8 (5th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "40 TFSI 2.0T", "hp": 204, "torque_nm": 340, "trans": ["auto 7-spd S-Tronic"]},
                {"cc": 2994, "label": "55 TFSI 3.0T V6", "hp": 340, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_200_000, "max": 7_000_000},
            "new_price_egp_2024": {"min": 3_660_000, "max": 6_090_000},
            "trims_egypt": ["40 TFSI", "45 TFSI", "55 TFSI", "S Line"],
        },
        "A7": {
            "first_year_global": 2010,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sportback"],
            "segments": ["E-segment", "premium coupe"],
            "generations": [
                {"gen": "4G (1st)", "years": "2010-2018"},
                {"gen": "4K8 (2nd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 2994, "label": "55 TFSI 3.0T", "hp": 340, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 8_500_000},
            "new_price_egp_2024": {"min": 4_790_000, "max": 7_400_000},
            "trims_egypt": ["55 TFSI", "S Line"],
        },
        "A8": {
            "first_year_global": 1994,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["F-segment", "luxury sedan"],
            "generations": [
                {"gen": "D4 (3rd)", "years": "2009-2017"},
                {"gen": "D5 (4th)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 2994, "label": "55 TFSI 3.0T", "hp": 340, "torque_nm": 500, "trans": ["auto 8-spd"]},
                {"cc": 3996, "label": "60 TFSI V8", "hp": 460, "torque_nm": 660, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 7_000_000, "max": 14_000_000},
            "new_price_egp_2024": {"min": 6_090_000, "max": 12_180_000},
            "trims_egypt": ["55 TFSI", "60 TFSI L"],
        },
        "Q3": {
            "first_year_global": 2011,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "premium"],
            "generations": [
                {"gen": "8U (1st)", "years": "2011-2018"},
                {"gen": "F3 (2nd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "35 TFSI 1.4T", "hp": 150, "torque_nm": 250, "trans": ["auto 6-spd S-Tronic"]},
                {"cc": 1984, "label": "40 TFSI 2.0T", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd S-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_800_000},
            "new_price_egp_2024": {"min": 2_180_000, "max": 3_310_000},
            "trims_egypt": ["35 TFSI", "40 TFSI", "S Line"],
        },
        "Q5": {
            "first_year_global": 2008,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "8R (1st)", "years": "2008-2016"},
                {"gen": "FY (2nd)", "years": "2016-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "40 TFSI 2.0T", "hp": 204, "torque_nm": 320, "trans": ["auto 7-spd S-Tronic"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 6_000_000},
            "new_price_egp_2024": {"min": 3_480_000, "max": 5_220_000},
            "trims_egypt": ["40 TFSI", "45 TFSI", "S Line"],
        },
        "Q7": {
            "first_year_global": 2005,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "premium"],
            "generations": [
                {"gen": "4L (1st)", "years": "2005-2015"},
                {"gen": "4M (2nd)", "years": "2015-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "45 TFSI 2.0T", "hp": 245, "torque_nm": 370, "trans": ["auto 8-spd"]},
                {"cc": 2994, "label": "55 TFSI 3.0T V6", "hp": 340, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 9_000_000},
            "new_price_egp_2024": {"min": 4_790_000, "max": 7_830_000},
            "trims_egypt": ["45 TFSI", "55 TFSI", "S Line"],
        },
        "Q8": {
            "first_year_global": 2018,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV coupe"],
            "segments": ["D-SUV", "premium coupe SUV"],
            "generations": [
                {"gen": "4M8 (1st)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 2994, "label": "55 TFSI 3.0T V6", "hp": 340, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 6_500_000, "max": 11_000_000},
            "new_price_egp_2024": {"min": 5_660_000, "max": 9_570_000},
            "trims_egypt": ["55 TFSI", "S Line"],
        },
        "e-tron": {
            "first_year_global": 2018,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["D-SUV", "electric", "premium"],
            "generations": [
                {"gen": "GE (1st)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 95kWh AWD", "hp": 408, "torque_nm": 664, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 7_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 6_090_000},
            "trims_egypt": ["55 quattro"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # MITSUBISHI
    # ════════════════════════════════════════════════════════════════════

    "Mitsubishi": {
        "Lancer": {
            "first_year_global": 1973,
            "egypt_from": 1990,
            "assembled_in_egypt": True,
            "assembler": "EIM (El Nasr Automotive Manufacturing)",
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "CS (8th)", "years": "2003-2007"},
                {"gen": "CY (9th)", "years": "2007-2017", "facelift": "2011"},
            ],
            "engines_egypt": [
                {"cc": 1587, "label": "1.6L MIVEC", "hp": 117, "torque_nm": 154, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued globally; huge used stock in Egypt",
        },
        "Eclipse Cross": {
            "first_year_global": 2017,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen GK0W", "years": "2017-present", "facelift": "2021"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 150, "torque_nm": 250, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_220_000, "max": 1_480_000},
            "trims_egypt": ["GLX", "GLS"],
        },
        "Outlander": {
            "first_year_global": 2001,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV", "D-SUV"],
            "generations": [
                {"gen": "CW0 (2nd)", "years": "2006-2012"},
                {"gen": "GF0W (3rd)", "years": "2012-2021", "facelift": "2015"},
                {"gen": "4th gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 2359, "label": "2.4L MIVEC", "hp": 167, "torque_nm": 222, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_500_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_180_000},
            "trims_egypt": ["GLX", "GLS"],
        },
        "Pajero": {
            "first_year_global": 1981,
            "egypt_from": 1990,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "4x4"],
            "segments": ["D-SUV", "body-on-frame"],
            "generations": [
                {"gen": "V93/97 (4th)", "years": "2006-present", "facelift": "2011/2015"},
            ],
            "engines_egypt": [
                {"cc": 3828, "label": "3.8L V6 SOHC", "hp": 250, "torque_nm": 329, "trans": ["auto 5-spd"]},
                {"cc": 3200, "label": "3.2L diesel turbo", "hp": 200, "torque_nm": 441, "trans": ["auto 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_200_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 2_780_000, "max": 3_480_000},
            "trims_egypt": ["GLS", "GLS Sport"],
            "notes": "Iconic 4x4; large loyal following",
        },
        "ASX": {
            "first_year_global": 2010,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "GA0W (1st)", "years": "2010-2022"},
                {"gen": "2nd gen (based on Clio)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1590, "label": "1.6L MIVEC", "hp": 117, "torque_nm": 154, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 830_000, "max": 1_050_000},
            "trims_egypt": ["GLX", "GLS"],
        },
        "L200": {
            "first_year_global": 1978,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["mid-size pickup"],
            "generations": [
                {"gen": "KB (5th)", "years": "2014-present", "facelift": "2018"},
            ],
            "engines_egypt": [
                {"cc": 2442, "label": "2.4L MIVEC diesel turbo", "hp": 181, "torque_nm": 430, "trans": ["auto 6-spd", "manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_300_000},
            "new_price_egp_2024": {"min": 1_570_000, "max": 2_000_000},
            "trims_egypt": ["GLX", "GLS"],
        },
        "Xpander": {
            "first_year_global": 2017,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["MPV", "7-seater"],
            "segments": ["MPV"],
            "generations": [
                {"gen": "1st gen", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "1.5L MIVEC", "hp": 105, "torque_nm": 141, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 830_000, "max": 1_050_000},
            "trims_egypt": ["GL", "GLS"],
        },
        "Colt": {
            "first_year_global": 2002,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "3rd gen Z30", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2T 3-cyl", "hp": 96, "torque_nm": 180, "trans": ["auto 7-spd CVT"]},
            ],
            "new_price_egp_2025": {"min": 750_000, "max": 950_000},
            "new_price_egp_2024": {"min": 655_000, "max": 828_000},
            "trims_egypt": ["Intro Edition", "Invite"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SUZUKI
    # ════════════════════════════════════════════════════════════════════

    "Suzuki": {
        "Celerio": {
            "first_year_global": 2014,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "1st gen LF", "years": "2014-2021"},
                {"gen": "2nd gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 998, "label": "1.0L 3-cyl", "hp": 67, "torque_nm": 90, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 430_000, "max": 580_000},
            "new_price_egp_2024": {"min": 375_000, "max": 505_000},
            "trims_egypt": ["GL", "GLX"],
            "notes": "Cheapest new car in Egypt",
        },
        "Alto": {
            "first_year_global": 1979,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "HA47S (9th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 660, "label": "0.66L 3-cyl", "hp": 46, "torque_nm": 57, "trans": ["auto AGS", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 380_000, "max": 500_000},
            "new_price_egp_2024": {"min": 330_000, "max": 435_000},
            "trims_egypt": ["GL"],
        },
        "Swift": {
            "first_year_global": 2004,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "ZC83S (4th)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1197, "label": "1.2L DualJet 4-cyl", "hp": 83, "torque_nm": 107, "trans": ["auto AGS", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 580_000, "max": 750_000},
            "new_price_egp_2024": {"min": 505_000, "max": 653_000},
            "trims_egypt": ["GL", "GLX"],
        },
        "Baleno": {
            "first_year_global": 2015,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "2nd gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1197, "label": "1.2L DualJet", "hp": 90, "torque_nm": 113, "trans": ["auto 5-AMT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 550_000, "max": 720_000},
            "new_price_egp_2024": {"min": 479_000, "max": 627_000},
            "trims_egypt": ["GL", "GLX"],
        },
        "Dzire": {
            "first_year_global": 2008,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["B-segment", "subcompact sedan"],
            "generations": [
                {"gen": "3rd gen (Swift-based)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1197, "label": "1.2L DualJet", "hp": 83, "torque_nm": 107, "trans": ["auto AGS", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 560_000, "max": 730_000},
            "new_price_egp_2024": {"min": 488_000, "max": 636_000},
            "trims_egypt": ["GL", "GLX"],
        },
        "Ertiga": {
            "first_year_global": 2012,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["MPV", "7-seater"],
            "segments": ["MPV"],
            "generations": [
                {"gen": "1st gen RZ", "years": "2012-2018"},
                {"gen": "2nd gen RZ", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1462, "label": "1.5L 4-cyl", "hp": 104, "torque_nm": 138, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 600_000, "max": 780_000},
            "new_price_egp_2024": {"min": 522_000, "max": 679_000},
            "trims_egypt": ["GL", "GLX"],
        },
        "S-Cross": {
            "first_year_global": 2013,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "JY (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1373, "label": "1.4L Boosterjet turbo", "hp": 129, "torque_nm": 235, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 740_000, "max": 958_000},
            "trims_egypt": ["GL", "GLX"],
        },
        "Vitara": {
            "first_year_global": 1988,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "4th gen LY", "years": "2015-present", "facelift": "2018"},
            ],
            "engines_egypt": [
                {"cc": 1373, "label": "1.4L Boosterjet turbo", "hp": 140, "torque_nm": 230, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 784_000, "max": 958_000},
            "trims_egypt": ["GLX"],
        },
        "Grand Vitara": {
            "first_year_global": 1997,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "3rd gen (2nd series)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1462, "label": "1.5L mild hybrid", "hp": 103, "torque_nm": 137, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_218_000},
            "trims_egypt": ["GL", "GLX"],
        },
        "Jimny": {
            "first_year_global": 1970,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["mini SUV", "4x4"],
            "segments": ["micro SUV"],
            "generations": [
                {"gen": "JB74 (4th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1462, "label": "1.5L 4-cyl", "hp": 102, "torque_nm": 130, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_175_000},
            "trims_egypt": ["GL"],
            "notes": "Cult following; limited supply keeps resale strong",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # BAIC
    # ════════════════════════════════════════════════════════════════════

    "BAIC": {
        "X35": {
            "first_year_global": 2019,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2019-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 147, "torque_nm": 226, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 500_000, "max": 680_000},
            "new_price_egp_2024": {"min": 435_000, "max": 592_000},
            "trims_egypt": ["Comfort", "Luxury"],
            "notes": "Ultra-budget Chinese SUV",
        },
        "X55 II": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "2nd gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 680_000, "max": 880_000},
            "new_price_egp_2024": {"min": 592_000, "max": 766_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "D50": {
            "first_year_global": 2017,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [{"gen": "2nd gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 150, "torque_nm": 225, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 480_000, "max": 640_000},
            "new_price_egp_2024": {"min": 418_000, "max": 557_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "BJ40": {
            "first_year_global": 2009,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["off-road SUV"],
            "segments": ["off-road", "4x4"],
            "generations": [{"gen": "2nd gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0T turbo", "hp": 228, "torque_nm": 380, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_392_000},
            "trims_egypt": ["Plus", "Landmark"],
            "notes": "Land Rover Defender-inspired styling; niche off-road market",
        },
        "BJ80": {
            "first_year_global": 2017,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["off-road SUV", "7-seater"],
            "segments": ["D-SUV", "off-road"],
            "generations": [{"gen": "1st gen", "years": "2017-present"}],
            "engines_egypt": [
                {"cc": 2999, "label": "3.0L diesel", "hp": 220, "torque_nm": 480, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_700_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_349_000},
            "trims_egypt": ["Luxury", "Explorer"],
        },
        "BJ30": {
            "first_year_global": 2022,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["off-road SUV", "compact"],
            "segments": ["off-road", "B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 147, "torque_nm": 220, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 560_000, "max": 750_000},
            "new_price_egp_2024": {"min": 487_000, "max": 653_000},
            "trims_egypt": ["Standard", "Luxury"],
            "notes": "Compact off-road SUV; rugged styling",
        },
        "X7": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 224, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_392_000},
            "trims_egypt": ["Luxury", "Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # PEUGEOT
    # ════════════════════════════════════════════════════════════════════

    "Peugeot": {
        "208": {
            "first_year_global": 2012,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "A9 (1st)", "years": "2012-2019"},
                {"gen": "UB3 (2nd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 3-cyl", "hp": 100, "torque_nm": 205, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 750_000, "max": 950_000},
            "new_price_egp_2024": {"min": 653_000, "max": 827_000},
            "trims_egypt": ["Active", "Allure"],
        },
        "301": {
            "first_year_global": 2012,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["B-segment", "C-segment"],
            "generations": [
                {"gen": "1st gen", "years": "2012-present", "facelift": "2017"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech", "hp": 82, "torque_nm": 118, "trans": ["manual 5-spd"]},
                {"cc": 1598, "label": "1.6L VTi", "hp": 115, "torque_nm": 150, "trans": ["auto 4-spd"]},
            ],
            "new_price_egp_2025": {"min": 620_000, "max": 820_000},
            "new_price_egp_2024": {"min": 540_000, "max": 714_000},
            "trims_egypt": ["Active", "Allure"],
            "notes": "Budget Peugeot sedan popular in Egypt fleet",
        },
        "308": {
            "first_year_global": 2007,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "T9 (2nd)", "years": "2013-2021"},
                {"gen": "P51 (3rd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 130hp", "hp": 130, "torque_nm": 230, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 784_000, "max": 1_044_000},
            "trims_egypt": ["Active", "Allure"],
        },
        "2008": {
            "first_year_global": 2013,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "A94 (1st)", "years": "2013-2019"},
                {"gen": "P24 (2nd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech turbo", "hp": 130, "torque_nm": 230, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 827_000, "max": 1_044_000},
            "trims_egypt": ["Active", "Allure", "GT"],
        },
        "408": {
            "first_year_global": 2022,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["fastback SUV"],
            "segments": ["C-segment", "D-segment"],
            "generations": [
                {"gen": "1st gen X74", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 130hp", "hp": 130, "torque_nm": 230, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_450_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_262_000},
            "trims_egypt": ["Allure", "GT"],
        },
        "3008": {
            "first_year_global": 2008,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "T84 (2nd)", "years": "2016-2023", "facelift": "2020"},
                {"gen": "B4 (3rd)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L PureTech turbo", "hp": 180, "torque_nm": 250, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_750_000},
            "new_price_egp_2024": {"min": 1_218_000, "max": 1_523_000},
            "trims_egypt": ["Active", "Allure", "GT"],
        },
        "508": {
            "first_year_global": 2010,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "fastback"],
            "segments": ["D-segment"],
            "generations": [
                {"gen": "W23 (1st)", "years": "2010-2018"},
                {"gen": "R83 (2nd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L PureTech 180hp", "hp": 180, "torque_nm": 250, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_131_000, "max": 1_479_000},
            "trims_egypt": ["Allure", "GT"],
        },
        "5008": {
            "first_year_global": 2009,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "P87 (2nd)", "years": "2017-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L PureTech turbo", "hp": 180, "torque_nm": 250, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_650_000, "max": 2_050_000},
            "new_price_egp_2024": {"min": 1_436_000, "max": 1_784_000},
            "trims_egypt": ["Allure", "GT"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # RENAULT
    # ════════════════════════════════════════════════════════════════════

    "Renault": {
        "Logan": {
            "first_year_global": 2004,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "L90 (1st)", "years": "2004-2013"},
                {"gen": "L52 (2nd)", "years": "2013-present", "facelift": "2016"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L 8V", "hp": 82, "torque_nm": 140, "trans": ["auto 4-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 530_000, "max": 680_000},
            "new_price_egp_2024": {"min": 461_000, "max": 592_000},
            "trims_egypt": ["Expression", "Dynamique"],
            "notes": "Budget segment; popular taxi/fleet car",
        },
        "Symbol": {
            "first_year_global": 1999,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "LB (3rd)", "years": "2012-present", "facelift": "2017"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L SCe", "hp": 115, "torque_nm": 156, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 560_000, "max": 720_000},
            "new_price_egp_2024": {"min": 487_000, "max": 627_000},
            "trims_egypt": ["Expression", "Privilege"],
        },
        "Sandero": {
            "first_year_global": 2008,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "B52 (2nd)", "years": "2012-2020"},
                {"gen": "BJI (3rd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L SCe 3-cyl", "hp": 65, "torque_nm": 91, "trans": ["manual 5-spd"]},
                {"cc": 999, "label": "1.0L TCe turbo", "hp": 90, "torque_nm": 160, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 500_000, "max": 680_000},
            "new_price_egp_2024": {"min": 435_000, "max": 592_000},
            "trims_egypt": ["Access", "Comfort"],
        },
        "Clio": {
            "first_year_global": 1990,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "X98 (4th)", "years": "2012-2019"},
                {"gen": "BJA (5th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TCe 90hp", "hp": 90, "torque_nm": 160, "trans": ["auto CVT", "manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 650_000, "max": 850_000},
            "new_price_egp_2024": {"min": 566_000, "max": 740_000},
            "trims_egypt": ["Zen", "Intens"],
        },
        "Duster": {
            "first_year_global": 2010,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "HS (1st)", "years": "2010-2017", "facelift": "2014"},
                {"gen": "HM (2nd)", "years": "2017-2023"},
                {"gen": "3rd gen", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L 4-cyl", "hp": 114, "torque_nm": 156, "trans": ["manual 6-spd"]},
                {"cc": 1330, "label": "1.3L TCe turbo", "hp": 130, "torque_nm": 240, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 609_000, "max": 827_000},
            "trims_egypt": ["Expression", "Dynamique", "Privilege"],
        },
        "Megane": {
            "first_year_global": 1995,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "X84 (3rd)", "years": "2008-2015"},
                {"gen": "BFB (4th)", "years": "2015-present"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "1.3L TCe 140hp", "hp": 140, "torque_nm": 240, "trans": ["auto EDC"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 740_000, "max": 958_000},
            "trims_egypt": ["Zen", "Intens"],
        },
        "Fluence": {
            "first_year_global": 2009,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment", "D-segment"],
            "generations": [
                {"gen": "L38 (1st)", "years": "2009-2017", "facelift": "2013"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6L 16V", "hp": 110, "torque_nm": 148, "trans": ["auto 6-spd EDC"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued; strong used stock in Egypt",
        },
        "Koleos": {
            "first_year_global": 2008,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "H45 (2nd)", "years": "2016-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0L dCi diesel", "hp": 177, "torque_nm": 380, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_392_000},
            "trims_egypt": ["Privilege", "Exclusive"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SKODA
    # ════════════════════════════════════════════════════════════════════

    "Skoda": {
        "Fabia": {
            "first_year_global": 1999,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "Mk3 NJ", "years": "2014-2021"},
                {"gen": "Mk4 PJ", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TSI 95hp", "hp": 95, "torque_nm": 175, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 750_000, "max": 950_000},
            "new_price_egp_2024": {"min": 653_000, "max": 827_000},
            "trims_egypt": ["Active", "Style"],
        },
        "Scala": {
            "first_year_global": 2018,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "NW2 (1st)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TSI 115hp", "hp": 115, "torque_nm": 200, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_150_000},
            "new_price_egp_2024": {"min": 784_000, "max": 1_001_000},
            "trims_egypt": ["Ambition", "Style"],
        },
        "Octavia": {
            "first_year_global": 1959,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "estate"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "Mk3 5E", "years": "2013-2020", "facelift": "2017"},
                {"gen": "Mk4 NX", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.4L TSI", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
                {"cc": 1984, "label": "2.0L TSI", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_131_000, "max": 1_479_000},
            "trims_egypt": ["Ambition", "Style"],
        },
        "Superb": {
            "first_year_global": 2001,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "estate"],
            "segments": ["D-segment"],
            "generations": [
                {"gen": "Mk3 3V", "years": "2015-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "2.0L TSI 190hp", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_700_000, "max": 2_200_000},
            "new_price_egp_2024": {"min": 1_479_000, "max": 1_914_000},
            "trims_egypt": ["Style", "L&K"],
        },
        "Kamiq": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "NW3 (1st)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TSI 115hp", "hp": 115, "torque_nm": 200, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_131_000},
            "trims_egypt": ["Ambition", "Style"],
        },
        "Karoq": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "NU7 (1st)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1395, "label": "1.5L TSI ACT", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_218_000, "max": 1_566_000},
            "trims_egypt": ["Ambition", "Style"],
        },
        "Kodiaq": {
            "first_year_global": 2016,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "NS7 (1st)", "years": "2016-2023"},
                {"gen": "NS7 (2nd)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "2.0L TSI", "hp": 190, "torque_nm": 320, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_500_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_175_000},
            "trims_egypt": ["Ambition", "Style"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # JEEP
    # ════════════════════════════════════════════════════════════════════

    "Jeep": {
        "Wrangler": {
            "first_year_global": 1987,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["off-road SUV"],
            "segments": ["off-road", "4x4"],
            "generations": [
                {"gen": "JK (3rd)", "years": "2006-2018"},
                {"gen": "JL (4th)", "years": "2018-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0L turbo", "hp": 272, "torque_nm": 400, "trans": ["auto 8-spd"]},
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 285, "torque_nm": 353, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 3_045_000, "max": 4_785_000},
            "trims_egypt": ["Sport", "Sahara", "Rubicon"],
        },
        "Grand Cherokee": {
            "first_year_global": 1992,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "premium SUV"],
            "generations": [
                {"gen": "WK2 (4th)", "years": "2010-2021", "facelift": "2014"},
                {"gen": "WL (5th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 293, "torque_nm": 353, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_200_000, "max": 4_800_000},
            "new_price_egp_2024": {"min": 2_784_000, "max": 4_176_000},
            "trims_egypt": ["Laredo", "Limited", "Trailhawk"],
        },
        "Compass": {
            "first_year_global": 2006,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "MP (2nd)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.3T GSE turbo", "hp": 150, "torque_nm": 270, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_653_000},
            "trims_egypt": ["Sport", "Limited"],
        },
        "Renegade": {
            "first_year_global": 2014,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "BU (1st)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1332, "label": "1.3T GSE turbo", "hp": 150, "torque_nm": 270, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_450_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_262_000},
            "trims_egypt": ["Sport", "Limited", "Trailhawk"],
        },
        "Cherokee": {
            "first_year_global": 1974,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "KL (5th)", "years": "2013-2023", "facelift": "2018"},
            ],
            "engines_egypt": [
                {"cc": 2360, "label": "2.4L Tigershark", "hp": 184, "torque_nm": 237, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_088_000},
            "trims_egypt": ["Sport", "Limited", "Trailhawk"],
        },
        "Gladiator": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck", "off-road"],
            "segments": ["mid-size pickup", "off-road"],
            "generations": [
                {"gen": "JT (1st)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 285, "torque_nm": 353, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 3_480_000},
            "trims_egypt": ["Sport", "Overland", "Rubicon"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # FORD
    # ════════════════════════════════════════════════════════════════════

    "Ford": {
        "Focus": {
            "first_year_global": 1998,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "Mk2", "years": "2004-2011"},
                {"gen": "Mk3", "years": "2011-2018"},
                {"gen": "Mk4", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L EcoBoost", "hp": 182, "torque_nm": 240, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_218_000},
            "trims_egypt": ["ST-Line"],
        },
        "Ranger": {
            "first_year_global": 1983,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["mid-size pickup"],
            "generations": [
                {"gen": "T6 (3rd)", "years": "2011-2022", "facelift": "2015/2019"},
                {"gen": "P703 (4th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1996, "label": "2.0L EcoBlue diesel", "hp": 170, "torque_nm": 405, "trans": ["auto 10-spd"]},
                {"cc": 3198, "label": "3.2L TDCi diesel", "hp": 200, "torque_nm": 470, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_700_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_349_000},
            "trims_egypt": ["XL", "XLT", "Wildtrak", "Raptor"],
        },
        "EcoSport": {
            "first_year_global": 2003,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "B515 (2nd)", "years": "2012-2022", "facelift": "2018"},
            ],
            "engines_egypt": [
                {"cc": 998, "label": "1.0L EcoBoost", "hp": 125, "torque_nm": 170, "trans": ["auto 6-spd"]},
                {"cc": 1498, "label": "1.5L Ti-VCT", "hp": 112, "torque_nm": 136, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 827_000, "max": 1_088_000},
            "trims_egypt": ["Trend", "Titanium"],
        },
        "Explorer": {
            "first_year_global": 1990,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV"],
            "generations": [
                {"gen": "U502 (5th)", "years": "2010-2019"},
                {"gen": "P702 (6th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 2300, "label": "2.3L EcoBoost", "hp": 300, "torque_nm": 420, "trans": ["auto 10-spd"]},
                {"cc": 3000, "label": "3.0L ST EcoBoost", "hp": 400, "torque_nm": 542, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_200_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_784_000, "max": 4_350_000},
            "trims_egypt": ["Limited", "Platinum", "ST"],
        },
        "Edge": {
            "first_year_global": 2006,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "CD539 (2nd)", "years": "2014-present", "facelift": "2018"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0L EcoBoost", "hp": 245, "torque_nm": 373, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_088_000},
            "trims_egypt": ["SEL", "Titanium"],
        },
        "Mustang": {
            "first_year_global": 1964,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe", "convertible"],
            "segments": ["sports car", "pony car"],
            "generations": [
                {"gen": "S550 (6th)", "years": "2014-present", "facelift": "2018/2022"},
            ],
            "engines_egypt": [
                {"cc": 2261, "label": "2.3L EcoBoost", "hp": 310, "torque_nm": 440, "trans": ["auto 10-spd"]},
                {"cc": 5038, "label": "5.0L Coyote V8", "hp": 450, "torque_nm": 529, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 4_350_000},
            "trims_egypt": ["EcoBoost", "GT", "GT Premium"],
        },
        "Bronco": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["off-road SUV"],
            "segments": ["off-road", "4x4"],
            "generations": [{"gen": "U725 (6th)", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 2300, "label": "2.3L EcoBoost", "hp": 300, "torque_nm": 420, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_800_000, "max": 3_800_000},
            "new_price_egp_2024": {"min": 2_436_000, "max": 3_306_000},
            "trims_egypt": ["Big Bend", "Outer Banks", "Badlands"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # HONDA
    # ════════════════════════════════════════════════════════════════════

    "Honda": {
        "City": {
            "first_year_global": 1981,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["B-segment", "subcompact sedan"],
            "generations": [
                {"gen": "GM6 (5th)", "years": "2014-2020"},
                {"gen": "GN2 (6th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L i-VTEC", "hp": 121, "torque_nm": 145, "trans": ["auto CVT", "manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 900_000},
            "new_price_egp_2024": {"min": 609_000, "max": 783_000},
            "trims_egypt": ["LX", "EX"],
        },
        "Civic": {
            "first_year_global": 1972,
            "egypt_from": 1995,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "FC (10th)", "years": "2015-2021"},
                {"gen": "FE (11th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L VTEC Turbo", "hp": 182, "torque_nm": 240, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_450_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_262_000},
            "trims_egypt": ["LX", "Sport", "EX"],
        },
        "Accord": {
            "first_year_global": 1976,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "mid-size sedan"],
            "generations": [
                {"gen": "CR (9th)", "years": "2012-2017"},
                {"gen": "CV (10th)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L VTEC Turbo", "hp": 192, "torque_nm": 260, "trans": ["auto CVT"]},
                {"cc": 1995, "label": "2.0L i-VTEC hybrid", "hp": 215, "torque_nm": 315, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 2_100_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_827_000},
            "trims_egypt": ["EX", "Sport", "Touring"],
        },
        "Jazz": {
            "first_year_global": 2001,
            "egypt_from": 2009,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "GK (3rd)", "years": "2013-2020"},
                {"gen": "GR (4th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1318, "label": "1.3L i-VTEC", "hp": 102, "torque_nm": 123, "trans": ["auto CVT", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 900_000},
            "new_price_egp_2024": {"min": 609_000, "max": 783_000},
            "trims_egypt": ["EX"],
            "notes": "Also known as Fit in some markets",
        },
        "HR-V": {
            "first_year_global": 1998,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "RU (2nd)", "years": "2014-2021"},
                {"gen": "RV (3rd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L VTEC Turbo", "hp": 182, "torque_nm": 240, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_250_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_088_000, "max": 1_392_000},
            "trims_egypt": ["LX", "EX"],
        },
        "CR-V": {
            "first_year_global": 1995,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "RW (5th)", "years": "2016-2022"},
                {"gen": "RS (6th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5L VTEC Turbo", "hp": 193, "torque_nm": 243, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_300_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_001_000},
            "trims_egypt": ["LX", "EX"],
        },
        "Pilot": {
            "first_year_global": 2002,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8-seater"],
            "segments": ["D-SUV", "E-SUV"],
            "generations": [
                {"gen": "YF2 (3rd)", "years": "2015-2022"},
                {"gen": "YF4 (4th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 3471, "label": "3.5L V6 i-VTEC", "hp": 285, "torque_nm": 355, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_045_000},
            "trims_egypt": ["EX-L", "Touring", "Elite"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # LAND ROVER
    # ════════════════════════════════════════════════════════════════════

    "Land Rover": {
        "Range Rover": {
            "first_year_global": 1969,
            "egypt_from": 1998,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["luxury SUV"],
            "segments": ["F-SUV", "luxury"],
            "generations": [
                {"gen": "L405 (4th)", "years": "2012-2022"},
                {"gen": "L460 (5th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 2996, "label": "P400 3.0T MHEV", "hp": 400, "torque_nm": 550, "trans": ["auto 8-spd"]},
                {"cc": 4395, "label": "P530 V8", "hp": 530, "torque_nm": 750, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 8_000_000, "max": 20_000_000},
            "new_price_egp_2024": {"min": 6_960_000, "max": 17_400_000},
            "trims_egypt": ["SE", "HSE", "Autobiography"],
        },
        "Range Rover Sport": {
            "first_year_global": 2005,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "luxury"],
            "generations": [
                {"gen": "L494 (2nd)", "years": "2013-2022"},
                {"gen": "L461 (3rd)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 2996, "label": "P400 3.0T MHEV", "hp": 400, "torque_nm": 550, "trans": ["auto 8-spd"]},
                {"cc": 4395, "label": "P530 V8", "hp": 530, "torque_nm": 750, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 12_000_000},
            "new_price_egp_2024": {"min": 4_785_000, "max": 10_440_000},
            "trims_egypt": ["SE", "HSE", "Autobiography Dynamic"],
        },
        "Velar": {
            "first_year_global": 2017,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV coupe"],
            "segments": ["D-SUV", "luxury"],
            "generations": [
                {"gen": "L560 (1st)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "P250 2.0T", "hp": 250, "torque_nm": 365, "trans": ["auto 8-spd"]},
                {"cc": 2996, "label": "P400 3.0T MHEV", "hp": 400, "torque_nm": 550, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 3_915_000, "max": 6_960_000},
            "trims_egypt": ["S", "SE", "HSE"],
        },
        "Discovery": {
            "first_year_global": 1989,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV"],
            "generations": [
                {"gen": "L462 (5th)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "P300 2.0T", "hp": 300, "torque_nm": 400, "trans": ["auto 8-spd"]},
                {"cc": 2996, "label": "P360 3.0T MHEV", "hp": 360, "torque_nm": 500, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 9_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 7_830_000},
            "trims_egypt": ["S", "SE", "HSE"],
        },
        "Discovery Sport": {
            "first_year_global": 2014,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "L550 (1st)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "P200 2.0T", "hp": 200, "torque_nm": 320, "trans": ["auto 9-spd"]},
                {"cc": 1997, "label": "P250 2.0T", "hp": 250, "torque_nm": 365, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 4_350_000},
            "trims_egypt": ["S", "SE", "HSE"],
        },
        "Defender": {
            "first_year_global": 1983,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "off-road"],
            "segments": ["D-SUV", "off-road"],
            "generations": [
                {"gen": "L663 (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1999, "label": "P300 2.0T", "hp": 300, "torque_nm": 400, "trans": ["auto 8-spd"]},
                {"cc": 2996, "label": "P400 3.0T MHEV", "hp": 400, "torque_nm": 550, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 3_915_000, "max": 6_960_000},
            "trims_egypt": ["S", "SE", "HSE", "X"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SUBARU
    # ════════════════════════════════════════════════════════════════════

    "Subaru": {
        "Impreza": {
            "first_year_global": 1992,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment", "AWD"],
            "generations": [
                {"gen": "G5 (5th)", "years": "2016-present"},
            ],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0L Boxer", "hp": 156, "torque_nm": 196, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_131_000},
            "trims_egypt": ["2.0i", "Sport"],
        },
        "XV": {
            "first_year_global": 2011,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "GT (2nd)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0L Boxer", "hp": 156, "torque_nm": 196, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_550_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_349_000},
            "trims_egypt": ["2.0i", "2.0i-S"],
            "notes": "Also sold as Crosstrek globally",
        },
        "Outback": {
            "first_year_global": 1994,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover", "estate"],
            "segments": ["C-SUV", "AWD"],
            "generations": [
                {"gen": "BN (6th)", "years": "2014-2019"},
                {"gen": "BT (7th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 2498, "label": "2.5L Boxer", "hp": 175, "torque_nm": 235, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_300_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_001_000},
            "trims_egypt": ["2.5i", "Premium"],
        },
        "Forester": {
            "first_year_global": 1997,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "SK (5th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0L Boxer", "hp": 156, "torque_nm": 196, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_392_000, "max": 1_740_000},
            "trims_egypt": ["2.0i", "2.0i-S"],
        },
        "Legacy": {
            "first_year_global": 1989,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "AWD"],
            "generations": [
                {"gen": "BN (7th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 2498, "label": "2.5L Boxer", "hp": 182, "torque_nm": 239, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_653_000},
            "trims_egypt": ["2.5i", "Sport"],
        },
        "WRX": {
            "first_year_global": 1992,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment", "sports", "AWD"],
            "generations": [
                {"gen": "VA (4th STi)", "years": "2014-2021"},
                {"gen": "VB (5th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1795, "label": "1.8L turbo DIT", "hp": 271, "torque_nm": 350, "trans": ["auto Lineartronic CVT"]},
                {"cc": 2457, "label": "2.5L turbo STI", "hp": 310, "torque_nm": 422, "trans": ["manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_610_000},
            "trims_egypt": ["WRX", "WRX STI"],
            "notes": "Niche enthusiast car; limited supply in Egypt",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # FIAT
    # ════════════════════════════════════════════════════════════════════

    "Fiat": {
        "Punto": {
            "first_year_global": 1993,
            "egypt_from": 2004,
            "assembled_in_egypt": True,
            "assembler": "Arab American Vehicles (AAV)",
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "Mk2 (2nd)", "years": "1999-2010"},
                {"gen": "Mk3 (3rd)", "years": "2005-2018"},
            ],
            "engines_egypt": [
                {"cc": 1242, "label": "1.2L 8V Fire", "hp": 69, "torque_nm": 102, "trans": ["manual 5-spd"]},
                {"cc": 1368, "label": "1.4L 8V Fire", "hp": 77, "torque_nm": 115, "trans": ["manual 5-spd", "auto"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued new sales; large used fleet; was assembled locally",
        },
        "Tipo": {
            "first_year_global": 1988,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "352 (2nd)", "years": "2015-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4L Turbo T-Jet", "hp": 120, "torque_nm": 206, "trans": ["auto 6-spd DCT"]},
                {"cc": 1598, "label": "1.6L E-Torq", "hp": 110, "torque_nm": 152, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 680_000, "max": 900_000},
            "new_price_egp_2024": {"min": 592_000, "max": 784_000},
            "trims_egypt": ["Pop", "Lounge"],
        },
        "500": {
            "first_year_global": 2007,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "convertible"],
            "segments": ["A-segment", "city car"],
            "generations": [
                {"gen": "312 (2nd)", "years": "2007-present"},
            ],
            "engines_egypt": [
                {"cc": 875, "label": "0.9L TwinAir turbo", "hp": 85, "torque_nm": 145, "trans": ["manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 750_000, "max": 1_000_000},
            "new_price_egp_2024": {"min": 653_000, "max": 870_000},
            "trims_egypt": ["Pop", "Lounge"],
            "notes": "Iconic retro styling; niche lifestyle car in Egypt",
        },
        "500X": {
            "first_year_global": 2014,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "334 (1st)", "years": "2014-present", "facelift": "2018"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4L Turbo T-Jet", "hp": 140, "torque_nm": 230, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 784_000, "max": 1_044_000},
            "trims_egypt": ["Pop", "Sport"],
        },
        "Bravo": {
            "first_year_global": 1995,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "198 (2nd)", "years": "2007-2015"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4L T-Jet turbo", "hp": 120, "torque_nm": 206, "trans": ["manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued; limited used stock",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # OPEL
    # ════════════════════════════════════════════════════════════════════

    "Opel": {
        "Corsa": {
            "first_year_global": 1982,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "F (5th)", "years": "2014-2019"},
                {"gen": "P2JO (6th)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 100hp", "hp": 100, "torque_nm": 205, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 750_000, "max": 1_000_000},
            "new_price_egp_2024": {"min": 653_000, "max": 870_000},
            "trims_egypt": ["Edition", "GS"],
        },
        "Astra": {
            "first_year_global": 1991,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "K (6th)", "years": "2015-2021"},
                {"gen": "L (7th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L Turbo 110hp", "hp": 110, "torque_nm": 205, "trans": ["auto 8-spd"]},
                {"cc": 1395, "label": "1.4L Turbo", "hp": 145, "torque_nm": 225, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 827_000, "max": 1_131_000},
            "trims_egypt": ["Edition", "GS"],
        },
        "Mokka": {
            "first_year_global": 2012,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "B (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 130hp", "hp": 130, "torque_nm": 230, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_175_000},
            "trims_egypt": ["Edition", "GS"],
        },
        "Grandland": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "A18 (1st)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 130hp", "hp": 130, "torque_nm": 230, "trans": ["auto 8-spd"]},
                {"cc": 1598, "label": "1.6L PureTech 180hp", "hp": 180, "torque_nm": 250, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_131_000, "max": 1_479_000},
            "trims_egypt": ["Edition", "GS Line"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # LEXUS
    # ════════════════════════════════════════════════════════════════════

    "Lexus": {
        "IS": {
            "first_year_global": 1998,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "premium"],
            "generations": [
                {"gen": "XE30 (3rd)", "years": "2013-present", "facelift": "2016/2020"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "IS300 2.0T", "hp": 241, "torque_nm": 350, "trans": ["auto 8-spd"]},
                {"cc": 3456, "label": "IS350 3.5L V6", "hp": 311, "torque_nm": 380, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_480_000},
            "trims_egypt": ["IS300", "IS350", "F Sport"],
        },
        "ES": {
            "first_year_global": 1989,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "E-segment", "luxury"],
            "generations": [
                {"gen": "AXZH10 (7th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 2487, "label": "ES300h hybrid", "hp": 218, "torque_nm": 221, "trans": ["e-CVT"]},
                {"cc": 3456, "label": "ES350 3.5L V6", "hp": 302, "torque_nm": 363, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 4_350_000},
            "trims_egypt": ["ES300h", "ES350", "F Sport"],
        },
        "GS": {
            "first_year_global": 1993,
            "egypt_from": 2006,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["E-segment", "luxury"],
            "generations": [
                {"gen": "L10 (4th)", "years": "2011-2020"},
            ],
            "engines_egypt": [
                {"cc": 3456, "label": "GS350 3.5L V6", "hp": 311, "torque_nm": 380, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued globally 2020; used stock remains in Egypt",
        },
        "LS": {
            "first_year_global": 1989,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["F-segment", "ultra-luxury"],
            "generations": [
                {"gen": "XF50 (5th)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 3445, "label": "LS500 twin-turbo V6", "hp": 416, "torque_nm": 600, "trans": ["auto 10-spd"]},
                {"cc": 3456, "label": "LS500h hybrid V6", "hp": 354, "torque_nm": 354, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 7_000_000, "max": 14_000_000},
            "new_price_egp_2024": {"min": 6_090_000, "max": 12_180_000},
            "trims_egypt": ["LS500", "LS500h", "Executive"],
        },
        "UX": {
            "first_year_global": 2018,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "premium"],
            "generations": [
                {"gen": "ZA10 (1st)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1987, "label": "UX250h 2.0L hybrid", "hp": 181, "torque_nm": 188, "trans": ["e-CVT"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_088_000},
            "trims_egypt": ["UX250h", "F Sport"],
        },
        "NX": {
            "first_year_global": 2014,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "AZ10 (1st)", "years": "2014-2021"},
                {"gen": "AZ20 (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 2487, "label": "NX350h hybrid", "hp": 239, "torque_nm": 239, "trans": ["e-CVT"]},
                {"cc": 1987, "label": "NX250 2.0T", "hp": 203, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 4_350_000},
            "trims_egypt": ["NX250", "NX350h", "F Sport"],
        },
        "RX": {
            "first_year_global": 1998,
            "egypt_from": 2002,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "premium"],
            "generations": [
                {"gen": "AL20 (4th)", "years": "2015-2022"},
                {"gen": "AL30 (5th)", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 2487, "label": "RX350h hybrid", "hp": 246, "torque_nm": 235, "trans": ["e-CVT"]},
                {"cc": 3456, "label": "RX350 3.5L V6", "hp": 295, "torque_nm": 363, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 7_000_000},
            "new_price_egp_2024": {"min": 3_915_000, "max": 6_090_000},
            "trims_egypt": ["RX350", "RX350h", "F Sport"],
        },
        "GX": {
            "first_year_global": 2002,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "premium", "body-on-frame"],
            "generations": [
                {"gen": "J150 (2nd)", "years": "2009-2023"},
                {"gen": "J250 (3rd)", "years": "2024-present"},
            ],
            "engines_egypt": [
                {"cc": 3956, "label": "GX460 4.6L V8", "hp": 301, "torque_nm": 439, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 6_960_000},
            "trims_egypt": ["Sport", "Luxury", "Premium"],
        },
        "LX": {
            "first_year_global": 1996,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["F-SUV", "luxury"],
            "generations": [
                {"gen": "J200 (3rd)", "years": "2007-2021"},
                {"gen": "J300 (4th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 3346, "label": "LX600 3.4L twin-turbo V6", "hp": 409, "torque_nm": 650, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 9_000_000, "max": 15_000_000},
            "new_price_egp_2024": {"min": 7_830_000, "max": 13_050_000},
            "trims_egypt": ["Premium", "Luxury", "Ultra Luxury"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # INFINITI
    # ════════════════════════════════════════════════════════════════════

    "Infiniti": {
        "Q50": {
            "first_year_global": 2013,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "premium"],
            "generations": [
                {"gen": "V37 (1st)", "years": "2013-present", "facelift": "2016"},
            ],
            "engines_egypt": [
                {"cc": 1991, "label": "2.0T 208hp", "hp": 208, "torque_nm": 350, "trans": ["auto 7-spd"]},
                {"cc": 2998, "label": "3.0T twin-turbo 400hp", "hp": 400, "torque_nm": 475, "trans": ["auto 7-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 3_480_000},
            "trims_egypt": ["Pure", "Luxe", "Red Sport 400"],
        },
        "Q60": {
            "first_year_global": 2016,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe"],
            "segments": ["D-segment", "premium coupe"],
            "generations": [
                {"gen": "V37 (2nd)", "years": "2016-present"},
            ],
            "engines_egypt": [
                {"cc": 1991, "label": "2.0T 208hp", "hp": 208, "torque_nm": 350, "trans": ["auto 7-spd"]},
                {"cc": 2998, "label": "3.0T 400hp", "hp": 400, "torque_nm": 475, "trans": ["auto 7-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_915_000},
            "trims_egypt": ["Pure", "Luxe", "Red Sport 400"],
        },
        "QX50": {
            "first_year_global": 2007,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "J55 (2nd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T VC-Turbo", "hp": 268, "torque_nm": 380, "trans": ["auto CVT"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_045_000},
            "trims_egypt": ["Pure", "Luxe", "ProACTIVE"],
        },
        "QX60": {
            "first_year_global": 2012,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "premium"],
            "generations": [
                {"gen": "L50 (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 3498, "label": "3.5L V6", "hp": 295, "torque_nm": 340, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 6_000_000},
            "new_price_egp_2024": {"min": 3_480_000, "max": 5_220_000},
            "trims_egypt": ["Pure", "Luxe", "Autograph"],
        },
        "QX80": {
            "first_year_global": 2010,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8-seater"],
            "segments": ["F-SUV", "luxury"],
            "generations": [
                {"gen": "Z62 (2nd)", "years": "2010-present", "facelift": "2014/2018/2022"},
            ],
            "engines_egypt": [
                {"cc": 5552, "label": "5.6L V8", "hp": 400, "torque_nm": 560, "trans": ["auto 7-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 9_000_000},
            "new_price_egp_2024": {"min": 4_785_000, "max": 7_830_000},
            "trims_egypt": ["Luxe", "Sensory", "Autograph"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # MAZDA
    # ════════════════════════════════════════════════════════════════════

    "Mazda": {
        "Mazda2": {
            "first_year_global": 2002,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "DJ (3rd)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1496, "label": "1.5L SKYACTIV-G", "hp": 111, "torque_nm": 139, "trans": ["auto 6-spd", "manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 900_000},
            "new_price_egp_2024": {"min": 609_000, "max": 783_000},
            "trims_egypt": ["Active", "Signature"],
        },
        "Mazda3": {
            "first_year_global": 2003,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "hatchback"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "BP (4th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0L SKYACTIV-G", "hp": 155, "torque_nm": 200, "trans": ["auto 6-spd"]},
                {"cc": 2488, "label": "2.5L SKYACTIV-G", "hp": 186, "torque_nm": 252, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_500_000},
            "new_price_egp_2024": {"min": 958_000, "max": 1_305_000},
            "trims_egypt": ["Active", "Luxury", "Signature"],
        },
        "Mazda6": {
            "first_year_global": 2002,
            "egypt_from": 2008,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "estate"],
            "segments": ["D-segment"],
            "generations": [
                {"gen": "GJ (3rd)", "years": "2012-present", "facelift": "2015/2018"},
            ],
            "engines_egypt": [
                {"cc": 2488, "label": "2.5L SKYACTIV-G", "hp": 192, "torque_nm": 252, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_218_000, "max": 1_566_000},
            "trims_egypt": ["Active", "Luxury", "Signature"],
        },
        "CX-3": {
            "first_year_global": 2015,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["A-SUV", "B-SUV"],
            "generations": [
                {"gen": "DK (1st)", "years": "2015-present"},
            ],
            "engines_egypt": [
                {"cc": 1496, "label": "1.5L SKYACTIV-G", "hp": 111, "torque_nm": 141, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 827_000, "max": 1_044_000},
            "trims_egypt": ["Active", "Luxury"],
        },
        "CX-5": {
            "first_year_global": 2012,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "KF (2nd)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0L SKYACTIV-G", "hp": 155, "torque_nm": 200, "trans": ["auto 6-spd"]},
                {"cc": 2488, "label": "2.5L SKYACTIV-G Turbo", "hp": 256, "torque_nm": 420, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 2_100_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_827_000},
            "trims_egypt": ["Active", "Luxury", "Signature"],
        },
        "CX-9": {
            "first_year_global": 2006,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "E-SUV"],
            "generations": [
                {"gen": "TC (2nd)", "years": "2015-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 2488, "label": "2.5L Turbo SKYACTIV-G", "hp": 250, "torque_nm": 420, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_300_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 2_871_000},
            "trims_egypt": ["Active", "Luxury", "Signature"],
        },
        "BT-50": {
            "first_year_global": 2006,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["mid-size pickup"],
            "generations": [
                {"gen": "TF (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1996, "label": "2.0L diesel turbo", "hp": 150, "torque_nm": 350, "trans": ["auto 6-spd"]},
                {"cc": 3198, "label": "3.2L diesel", "hp": 197, "torque_nm": 470, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_088_000},
            "trims_egypt": ["Active", "Freestyle"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # PORSCHE
    # ════════════════════════════════════════════════════════════════════

    "Porsche": {
        "911": {
            "first_year_global": 1963,
            "egypt_from": 2000,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe", "convertible", "targa"],
            "segments": ["sports car", "supercar"],
            "generations": [
                {"gen": "992 (8th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 2981, "label": "Carrera 3.0T flat-6", "hp": 385, "torque_nm": 450, "trans": ["auto 8-spd PDK"]},
                {"cc": 2981, "label": "Carrera 4S 3.0T", "hp": 450, "torque_nm": 530, "trans": ["auto 8-spd PDK"]},
            ],
            "new_price_egp_2025": {"min": 8_000_000, "max": 20_000_000},
            "new_price_egp_2024": {"min": 6_960_000, "max": 17_400_000},
            "trims_egypt": ["Carrera", "Carrera S", "Carrera 4S", "Targa"],
        },
        "Cayenne": {
            "first_year_global": 2002,
            "egypt_from": 2004,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV", "luxury"],
            "generations": [
                {"gen": "E3 (3rd)", "years": "2017-present", "facelift": "2023"},
            ],
            "engines_egypt": [
                {"cc": 2894, "label": "Cayenne 2.9T V6", "hp": 335, "torque_nm": 450, "trans": ["auto 8-spd PDK"]},
                {"cc": 2894, "label": "Cayenne S 2.9T V6", "hp": 440, "torque_nm": 550, "trans": ["auto 8-spd PDK"]},
                {"cc": 3996, "label": "Cayenne Turbo V8", "hp": 550, "torque_nm": 770, "trans": ["auto 8-spd PDK"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 15_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 13_050_000},
            "trims_egypt": ["Cayenne", "Cayenne S", "Cayenne Turbo"],
        },
        "Macan": {
            "first_year_global": 2014,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "luxury"],
            "generations": [
                {"gen": "95B (1st)", "years": "2014-2023"},
                {"gen": "EV (2nd)", "years": "2024-present"},
            ],
            "engines_egypt": [
                {"cc": 1984, "label": "Macan 2.0T", "hp": 265, "torque_nm": 400, "trans": ["auto 7-spd PDK"]},
                {"cc": 2894, "label": "Macan S 2.9T", "hp": 380, "torque_nm": 520, "trans": ["auto 7-spd PDK"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 7_000_000},
            "new_price_egp_2024": {"min": 3_045_000, "max": 6_090_000},
            "trims_egypt": ["Macan", "Macan S", "Macan GTS"],
        },
        "Panamera": {
            "first_year_global": 2009,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["fastback", "sport turismo"],
            "segments": ["F-segment", "luxury", "sports"],
            "generations": [
                {"gen": "G2 (2nd)", "years": "2016-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 2894, "label": "Panamera 4 2.9T V6", "hp": 330, "torque_nm": 450, "trans": ["auto 8-spd PDK"]},
                {"cc": 2894, "label": "Panamera 4S 2.9T V6", "hp": 440, "torque_nm": 550, "trans": ["auto 8-spd PDK"]},
            ],
            "new_price_egp_2025": {"min": 6_000_000, "max": 15_000_000},
            "new_price_egp_2024": {"min": 5_220_000, "max": 13_050_000},
            "trims_egypt": ["Panamera 4", "Panamera 4S", "Turbo"],
        },
        "Taycan": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV", "sport turismo EV"],
            "segments": ["F-segment", "electric", "luxury"],
            "generations": [
                {"gen": "Y1A (1st)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric RWD 300kW", "hp": 408, "torque_nm": 650, "trans": ["2-speed"]},
                {"cc": 0, "label": "Turbo S AWD", "hp": 761, "torque_nm": 1050, "trans": ["2-speed"]},
            ],
            "new_price_egp_2025": {"min": 6_000_000, "max": 18_000_000},
            "new_price_egp_2024": {"min": 5_220_000, "max": 15_660_000},
            "trims_egypt": ["Standard", "4S", "Turbo", "Turbo S"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # VOLVO
    # ════════════════════════════════════════════════════════════════════

    "Volvo": {
        "S60": {
            "first_year_global": 2000,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "premium"],
            "generations": [
                {"gen": "Z (3rd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1969, "label": "B4 2.0T mild hybrid 197hp", "hp": 197, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 1969, "label": "B5 2.0T mild hybrid 250hp", "hp": 250, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_784_000},
            "trims_egypt": ["Momentum", "R-Design"],
        },
        "S90": {
            "first_year_global": 2016,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["E-segment", "luxury"],
            "generations": [
                {"gen": "P238 (2nd)", "years": "2016-present"},
            ],
            "engines_egypt": [
                {"cc": 1969, "label": "B5 2.0T 249hp", "hp": 249, "torque_nm": 350, "trans": ["auto 8-spd"]},
                {"cc": 1969, "label": "B6 2.0T 300hp", "hp": 300, "torque_nm": 420, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 3_045_000, "max": 4_785_000},
            "trims_egypt": ["Momentum", "Inscription"],
        },
        "XC40": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV", "premium"],
            "generations": [
                {"gen": "536 (1st)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1969, "label": "B4 2.0T 197hp", "hp": 197, "torque_nm": 300, "trans": ["auto 8-spd"]},
                {"cc": 1969, "label": "B5 2.0T 250hp", "hp": 250, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 1_914_000, "max": 3_045_000},
            "trims_egypt": ["Momentum", "R-Design"],
        },
        "XC60": {
            "first_year_global": 2008,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "246 (2nd)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1969, "label": "B5 2.0T 250hp", "hp": 250, "torque_nm": 350, "trans": ["auto 8-spd"]},
                {"cc": 1969, "label": "B6 2.0T 300hp", "hp": 300, "torque_nm": 420, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 4_350_000},
            "trims_egypt": ["Momentum", "R-Design", "Inscription"],
        },
        "XC90": {
            "first_year_global": 2002,
            "egypt_from": 2005,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV", "luxury"],
            "generations": [
                {"gen": "256 (2nd)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1969, "label": "B5 AWD 2.0T 250hp", "hp": 250, "torque_nm": 350, "trans": ["auto 8-spd"]},
                {"cc": 1969, "label": "B6 AWD 2.0T 300hp", "hp": 300, "torque_nm": 420, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 7_500_000},
            "new_price_egp_2024": {"min": 3_915_000, "max": 6_525_000},
            "trims_egypt": ["Momentum", "R-Design", "Inscription"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # DODGE
    # ════════════════════════════════════════════════════════════════════

    "Dodge": {
        "Charger": {
            "first_year_global": 1966,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "muscle car"],
            "generations": [
                {"gen": "LD (7th)", "years": "2010-2023", "facelift": "2015"},
            ],
            "engines_egypt": [
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 292, "torque_nm": 353, "trans": ["auto 8-spd"]},
                {"cc": 5654, "label": "5.7L HEMI V8", "hp": 370, "torque_nm": 529, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 4_350_000},
            "trims_egypt": ["SXT", "GT", "R/T", "Scat Pack"],
        },
        "Challenger": {
            "first_year_global": 2008,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe"],
            "segments": ["sports car", "muscle car"],
            "generations": [
                {"gen": "LC (3rd)", "years": "2008-2023"},
            ],
            "engines_egypt": [
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 303, "torque_nm": 363, "trans": ["auto 8-spd"]},
                {"cc": 5654, "label": "5.7L HEMI V8", "hp": 375, "torque_nm": 529, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 5_500_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 4_785_000},
            "trims_egypt": ["SXT", "GT", "R/T", "Scat Pack"],
        },
        "Durango": {
            "first_year_global": 1997,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "E-SUV"],
            "generations": [
                {"gen": "WD (3rd)", "years": "2011-present", "facelift": "2014/2021"},
            ],
            "engines_egypt": [
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 293, "torque_nm": 353, "trans": ["auto 8-spd"]},
                {"cc": 5654, "label": "5.7L HEMI V8", "hp": 360, "torque_nm": 529, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_915_000},
            "trims_egypt": ["SXT", "GT", "R/T"],
        },
        "RAM 1500": {
            "first_year_global": 1981,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["full-size pickup"],
            "generations": [
                {"gen": "DT (5th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 3604, "label": "3.6L Pentastar V6", "hp": 305, "torque_nm": 363, "trans": ["auto 8-spd"]},
                {"cc": 5654, "label": "5.7L HEMI V8 eTorque", "hp": 395, "torque_nm": 556, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 4_350_000},
            "trims_egypt": ["Tradesman", "Big Horn", "Laramie", "Limited"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # ISUZU
    # ════════════════════════════════════════════════════════════════════

    "Isuzu": {
        "D-Max": {
            "first_year_global": 2002,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["mid-size pickup"],
            "generations": [
                {"gen": "TFR/TFS (3rd)", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1898, "label": "1.9L RZ4E diesel", "hp": 163, "torque_nm": 360, "trans": ["auto 6-spd", "manual 6-spd"]},
                {"cc": 2999, "label": "3.0L 4JJ3 diesel", "hp": 190, "torque_nm": 450, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_700_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_479_000, "max": 2_088_000},
            "trims_egypt": ["LS", "V-Cross", "X-Terrain"],
        },
        "MU-X": {
            "first_year_global": 2013,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "TF (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1898, "label": "1.9L diesel", "hp": 163, "torque_nm": 360, "trans": ["auto 6-spd"]},
                {"cc": 2999, "label": "3.0L diesel", "hp": 190, "torque_nm": 450, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_436_000},
            "trims_egypt": ["LS", "LX"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # HAVAL (Great Wall)
    # ════════════════════════════════════════════════════════════════════

    "Haval": {
        "Jolion": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 147, "torque_nm": 220, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 650_000, "max": 850_000},
            "new_price_egp_2024": {"min": 566_000, "max": 740_000},
            "trims_egypt": ["Standard", "Luxury"],
        },
        "H6": {
            "first_year_global": 2011,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "3rd gen (HEV)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 169, "torque_nm": 285, "trans": ["auto 7-spd DCT"]},
                {"cc": 2000, "label": "2.0T turbo", "hp": 224, "torque_nm": 340, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 784_000, "max": 1_088_000},
            "trims_egypt": ["Standard", "Luxury", "Ultra"],
        },
        "Dargo": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 2000, "label": "2.0T turbo", "hp": 237, "torque_nm": 375, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_392_000},
            "trims_egypt": ["Luxury", "Ultra"],
        },
        "H9": {
            "first_year_global": 2014,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV", "E-SUV"],
            "generations": [
                {"gen": "P06 (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 2000, "label": "2.0T turbo", "hp": 224, "torque_nm": 340, "trans": ["auto 8-spd"]},
                {"cc": 3000, "label": "3.0T turbo V6", "hp": 354, "torque_nm": 500, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_610_000},
            "trims_egypt": ["Luxury", "Ultra"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # JAC
    # ════════════════════════════════════════════════════════════════════

    "JAC": {
        "JS3": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["A-SUV", "B-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 143, "torque_nm": 210, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 430_000, "max": 580_000},
            "new_price_egp_2024": {"min": 374_000, "max": 505_000},
            "trims_egypt": ["Comfort", "Luxury"],
            "notes": "One of cheapest SUVs in Egypt",
        },
        "JS4": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 520_000, "max": 700_000},
            "new_price_egp_2024": {"min": 452_000, "max": 609_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "J7": {
            "first_year_global": 2020,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment"],
            "generations": [
                {"gen": "1st gen", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 174, "torque_nm": 275, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 550_000, "max": 730_000},
            "new_price_egp_2024": {"min": 479_000, "max": 635_000},
            "trims_egypt": ["Luxury", "Elite"],
        },
        "T8": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["pickup"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo diesel", "hp": 190, "torque_nm": 400, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 783_000, "max": 1_044_000},
            "trims_egypt": ["Sport", "Luxury"],
            "notes": "Chinese pickup; competes with Hilux in price",
        },
        "T9": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["pickup"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 224, "torque_nm": 380, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_050_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 914_000, "max": 1_175_000},
            "trims_egypt": ["Premium", "Flagship"],
        },
        "Sei 7": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV", "7-seater"],
            "segments": ["C-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 75kWh", "hp": 218, "torque_nm": 340, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_220_000},
            "trims_egypt": ["Standard Range", "Long Range"],
            "notes": "JAC electric SUV entering Egypt market 2024",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # JETOUR
    # ════════════════════════════════════════════════════════════════════

    "JETOUR": {
        "X70": {
            "first_year_global": 2018,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2018-present", "facelift": "2022"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 650_000, "max": 880_000},
            "new_price_egp_2024": {"min": 566_000, "max": 766_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "X90": {
            "first_year_global": 2019,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2019-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 254, "torque_nm": 390, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 827_000, "max": 1_131_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
        "X95": {
            "first_year_global": 2022,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 268, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_392_000},
            "trims_egypt": ["Luxury", "Flagship"],
            "notes": "Flagship 7-seat SUV; competes with Palisade/Fortuner",
        },
        "Dashing": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 181, "torque_nm": 290, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 750_000, "max": 1_000_000},
            "new_price_egp_2024": {"min": 653_000, "max": 870_000},
            "trims_egypt": ["Sport", "Elite"],
            "notes": "Sporty fastback SUV styling; among newer JETOUR entries",
        },
        "T2": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 580_000, "max": 780_000},
            "new_price_egp_2024": {"min": 505_000, "max": 679_000},
            "trims_egypt": ["Comfort", "Luxury"],
            "notes": "Entry-level JETOUR; budget-friendly B-segment",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # ALFA ROMEO
    # ════════════════════════════════════════════════════════════════════

    "Alfa Romeo": {
        "Giulia": {
            "first_year_global": 2015,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "premium sports"],
            "generations": [
                {"gen": "952 (1st)", "years": "2015-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0T 200hp", "hp": 200, "torque_nm": 330, "trans": ["auto 8-spd"]},
                {"cc": 1995, "label": "2.0T 280hp", "hp": 280, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_800_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 3_306_000},
            "trims_egypt": ["Veloce", "Super", "Quadrifoglio"],
        },
        "Stelvio": {
            "first_year_global": 2016,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "D-SUV", "premium"],
            "generations": [
                {"gen": "949 (1st)", "years": "2016-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1995, "label": "2.0T 200hp", "hp": 200, "torque_nm": 330, "trans": ["auto 8-spd"]},
                {"cc": 1995, "label": "2.0T 280hp", "hp": 280, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_915_000},
            "trims_egypt": ["Veloce", "Ti", "Quadrifoglio"],
        },
        "Giulietta": {
            "first_year_global": 2010,
            "egypt_from": 2013,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["C-segment", "premium"],
            "generations": [
                {"gen": "940 (1st)", "years": "2010-2020"},
            ],
            "engines_egypt": [
                {"cc": 1368, "label": "1.4T MultiAir 170hp", "hp": 170, "torque_nm": 250, "trans": ["auto TCT"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued; used stock available",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # CADILLAC
    # ════════════════════════════════════════════════════════════════════

    "Cadillac": {
        "Escalade": {
            "first_year_global": 1999,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8-seater"],
            "segments": ["F-SUV", "luxury"],
            "generations": [
                {"gen": "GMT K2 (4th)", "years": "2014-2020"},
                {"gen": "GMT RKD (5th)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 6162, "label": "6.2L V8 EcoTec3", "hp": 420, "torque_nm": 623, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 5_000_000, "max": 9_000_000},
            "new_price_egp_2024": {"min": 4_350_000, "max": 7_830_000},
            "trims_egypt": ["Luxury", "Premium Luxury", "Sport Platinum"],
        },
        "CT6": {
            "first_year_global": 2015,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["F-segment", "luxury"],
            "generations": [
                {"gen": "1st gen", "years": "2015-2020"},
            ],
            "engines_egypt": [
                {"cc": 2997, "label": "3.0T twin-turbo V6", "hp": 404, "torque_nm": 553, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": None, "max": None},
            "new_price_egp_2024": {"min": None, "max": None},
            "notes": "Discontinued globally 2020; residual used stock",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # GMC
    # ════════════════════════════════════════════════════════════════════

    "GMC": {
        "Yukon": {
            "first_year_global": 1991,
            "egypt_from": 2003,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "8/9-seater"],
            "segments": ["F-SUV", "luxury"],
            "generations": [
                {"gen": "K2 (4th)", "years": "2014-2020"},
                {"gen": "T1 (5th)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 5328, "label": "5.3L EcoTec3 V8", "hp": 355, "torque_nm": 519, "trans": ["auto 10-spd"]},
                {"cc": 6162, "label": "6.2L EcoTec3 V8", "hp": 420, "torque_nm": 623, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_500_000, "max": 7_500_000},
            "new_price_egp_2024": {"min": 3_915_000, "max": 6_525_000},
            "trims_egypt": ["SLE", "SLT", "AT4", "Denali"],
        },
        "Sierra": {
            "first_year_global": 1988,
            "egypt_from": 2014,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["full-size pickup"],
            "generations": [
                {"gen": "K2 (4th)", "years": "2013-2018"},
                {"gen": "T1 (5th)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 5328, "label": "5.3L V8 EcoTec3", "hp": 355, "torque_nm": 519, "trans": ["auto 8-spd"]},
                {"cc": 6162, "label": "6.2L V8 EcoTec3", "hp": 420, "torque_nm": 623, "trans": ["auto 10-spd"]},
            ],
            "new_price_egp_2025": {"min": 4_000_000, "max": 6_500_000},
            "new_price_egp_2024": {"min": 3_480_000, "max": 5_655_000},
            "trims_egypt": ["SLE", "SLT", "AT4", "Denali"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # JAGUAR
    # ════════════════════════════════════════════════════════════════════

    "Jaguar": {
        "XE": {
            "first_year_global": 2014,
            "egypt_from": 2016,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["D-segment", "premium"],
            "generations": [
                {"gen": "X760 (1st)", "years": "2014-present", "facelift": "2019"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "P250 2.0T 250hp", "hp": 250, "torque_nm": 365, "trans": ["auto 8-spd"]},
                {"cc": 1997, "label": "P300 2.0T 300hp", "hp": 300, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 3_500_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 3_045_000},
            "trims_egypt": ["SE", "HSE", "R-Dynamic"],
        },
        "XF": {
            "first_year_global": 2007,
            "egypt_from": 2010,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["E-segment", "premium"],
            "generations": [
                {"gen": "X260 (2nd)", "years": "2015-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "P250 2.0T 250hp", "hp": 250, "torque_nm": 365, "trans": ["auto 8-spd"]},
                {"cc": 1997, "label": "P300 2.0T 300hp", "hp": 300, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_800_000, "max": 4_800_000},
            "new_price_egp_2024": {"min": 2_436_000, "max": 4_176_000},
            "trims_egypt": ["SE", "HSE", "R-Dynamic"],
        },
        "E-Pace": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "X540 (1st)", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1497, "label": "P200 1.5T 3-cyl 200hp", "hp": 200, "torque_nm": 320, "trans": ["auto 9-spd"]},
                {"cc": 1997, "label": "P250 2.0T 249hp", "hp": 249, "torque_nm": 365, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 4_000_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 3_480_000},
            "trims_egypt": ["SE", "HSE", "R-Dynamic"],
        },
        "F-Pace": {
            "first_year_global": 2016,
            "egypt_from": 2017,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "D-SUV", "premium"],
            "generations": [
                {"gen": "X761 (1st)", "years": "2016-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "P250 2.0T 250hp", "hp": 250, "torque_nm": 365, "trans": ["auto 8-spd"]},
                {"cc": 1997, "label": "P400e PHEV 404hp", "hp": 404, "torque_nm": 640, "trans": ["auto 8-spd"]},
                {"cc": 2995, "label": "P550 SVR 3.0T V6", "hp": 550, "torque_nm": 700, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 3_045_000, "max": 6_960_000},
            "trims_egypt": ["SE", "HSE", "R-Dynamic", "SVR"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # DONGFENG / DFSK
    # ════════════════════════════════════════════════════════════════════

    "Dongfeng": {
        "AX7": {
            "first_year_global": 2014,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2014-2020"},
                {"gen": "AX7 Pro (2nd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 190, "torque_nm": 310, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 740_000, "max": 960_000},
            "trims_egypt": ["Luxury", "Premium"],
        },
        "AX4": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2017-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 143, "torque_nm": 230, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 580_000, "max": 750_000},
            "new_price_egp_2024": {"min": 500_000, "max": 650_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
        "Glory 500": {
            "first_year_global": 2018,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2018-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 147, "torque_nm": 230, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 680_000, "max": 900_000},
            "new_price_egp_2024": {"min": 590_000, "max": 780_000},
            "trims_egypt": ["Luxury"],
        },
        "Glory 580 Pro": {
            "first_year_global": 2019,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2019-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 190, "torque_nm": 310, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_150_000},
            "new_price_egp_2024": {"min": 780_000, "max": 1_000_000},
            "trims_egypt": ["Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # GAC (GUANGZHOU AUTO / TRUMPCHI)
    # ════════════════════════════════════════════════════════════════════

    "GAC": {
        "GS3": {
            "first_year_global": 2016,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2016-2021"},
                {"gen": "2nd gen Emzoom", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 150, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 680_000, "max": 880_000},
            "new_price_egp_2024": {"min": 590_000, "max": 765_000},
            "trims_egypt": ["Standard", "Luxury"],
        },
        "GS4": {
            "first_year_global": 2015,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2015-2020"},
                {"gen": "2nd gen Plus", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "1.5T turbo", "hp": 169, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 740_000, "max": 960_000},
            "trims_egypt": ["Standard", "Luxury", "Sport"],
        },
        "GS5": {
            "first_year_global": 2019,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "2nd gen", "years": "2019-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 252, "torque_nm": 370, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_220_000},
            "trims_egypt": ["Luxury", "Sport"],
        },
        "GS8": {
            "first_year_global": 2016,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2016-2021"},
                {"gen": "2nd gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 252, "torque_nm": 400, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_220_000, "max": 1_570_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
        "GA4": {
            "first_year_global": 2017,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "1st gen", "years": "2017-2022"},
                {"gen": "2nd gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 150, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 620_000, "max": 800_000},
            "new_price_egp_2024": {"min": 540_000, "max": 695_000},
            "trims_egypt": ["Standard", "Luxury"],
        },
        "Emkoo": {
            "first_year_global": 2022,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 169, "torque_nm": 265, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 830_000, "max": 1_090_000},
            "trims_egypt": ["Luxury", "Sport"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # CHANGAN
    # ════════════════════════════════════════════════════════════════════

    "Changan": {
        "CS35 Plus": {
            "first_year_global": 2018,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "2nd gen", "years": "2018-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T Blue Whale turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 650_000, "max": 850_000},
            "new_price_egp_2024": {"min": 565_000, "max": 740_000},
            "trims_egypt": ["Luxury", "Premium"],
        },
        "CS55 Plus": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "2nd gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T Blue Whale turbo", "hp": 181, "torque_nm": 300, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 740_000, "max": 960_000},
            "trims_egypt": ["Luxury", "Premium", "Flagship"],
        },
        "CS75 Plus": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV", "D-SUV"],
            "generations": [{"gen": "2nd gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T Blue Whale turbo", "hp": 233, "torque_nm": 390, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_450_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_265_000},
            "trims_egypt": ["Premium", "Flagship"],
        },
        "Uni-T": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T Blue Whale turbo", "hp": 181, "torque_nm": 300, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 830_000, "max": 1_045_000},
            "trims_egypt": ["Premium", "Flagship"],
        },
        "Uni-K": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T Blue Whale turbo", "hp": 233, "torque_nm": 390, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_130_000, "max": 1_480_000},
            "trims_egypt": ["Premium", "Flagship"],
        },
        "Hunter": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["pickup"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T Blue Whale turbo", "hp": 245, "torque_nm": 390, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_045_000, "max": 1_395_000},
            "trims_egypt": ["Premium", "Flagship"],
        },
        "Lamore": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 181, "torque_nm": 300, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 780_000, "max": 1_000_000},
            "new_price_egp_2024": {"min": 680_000, "max": 870_000},
            "trims_egypt": ["Luxury", "Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # OMODA (CHERY SUB-BRAND)
    # ════════════════════════════════════════════════════════════════════

    "Omoda": {
        "Omoda 5": {
            "first_year_global": 2022,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6T TGDI turbo", "hp": 197, "torque_nm": 290, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 830_000, "max": 1_090_000},
            "trims_egypt": ["Comfort", "Luxury", "Sport"],
            "notes": "Chery premium sub-brand; strong styling; gaining fast in Egypt",
        },
        "Omoda C5": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 145, "torque_nm": 210, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 720_000, "max": 950_000},
            "new_price_egp_2024": {"min": 625_000, "max": 830_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # EXEED (CHERY PREMIUM SUB-BRAND)
    # ════════════════════════════════════════════════════════════════════

    "Exeed": {
        "TXL": {
            "first_year_global": 2018,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2018-present", "facelift": "2021"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T TGDI turbo", "hp": 254, "torque_nm": 390, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_220_000, "max": 1_570_000},
            "trims_egypt": ["Luxury", "Flagship"],
            "notes": "Chery's luxury sub-brand; positioned above Tiggo line",
        },
        "RX": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6T TGDI turbo", "hp": 197, "torque_nm": 290, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_050_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 915_000, "max": 1_175_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
        "LX": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T TGDI turbo", "hp": 254, "torque_nm": 390, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_100_000},
            "new_price_egp_2024": {"min": 1_395_000, "max": 1_830_000},
            "trims_egypt": ["Flagship"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # TANK (GWM SUB-BRAND)
    # ════════════════════════════════════════════════════════════════════

    "Tank": {
        "Tank 300": {
            "first_year_global": 2021,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "off-road"],
            "segments": ["C-SUV", "off-road"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T turbo", "hp": 220, "torque_nm": 387, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_100_000},
            "new_price_egp_2024": {"min": 1_395_000, "max": 1_830_000},
            "trims_egypt": ["Off-Road", "City"],
            "notes": "GWM's off-road oriented brand; Wrangler competitor at lower price",
        },
        "Tank 500": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater", "off-road"],
            "segments": ["D-SUV", "off-road"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 2998, "label": "3.0T V6 twin-turbo", "hp": 354, "torque_nm": 500, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_300_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 2_875_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
        "Tank 700": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["E-SUV", "luxury off-road"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 2998, "label": "3.0T V6 twin-turbo Hi4-T PHEV", "hp": 540, "torque_nm": 800, "trans": ["auto 9-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_800_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 3_310_000, "max": 4_350_000},
            "trims_egypt": ["Flagship"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # ORA (GWM EV SUB-BRAND)
    # ════════════════════════════════════════════════════════════════════

    "Ora": {
        "Good Cat": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback EV"],
            "segments": ["B-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 63kWh", "hp": 143, "torque_nm": 210, "trans": ["single-speed"], "range_km": 401},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_150_000},
            "new_price_egp_2024": {"min": 785_000, "max": 1_000_000},
            "trims_egypt": ["Standard", "Premium"],
            "notes": "Retro-styled EV; also sold as Ora Funky Cat in some markets",
        },
        "Lightning Cat": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["D-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 83kWh", "hp": 268, "torque_nm": 430, "trans": ["single-speed"], "range_km": 500},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_655_000},
            "trims_egypt": ["Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # CITROËN
    # ════════════════════════════════════════════════════════════════════

    "Citroën": {
        "C3": {
            "first_year_global": 2002,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "B618 (3rd)", "years": "2016-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 3-cyl", "hp": 83, "torque_nm": 118, "trans": ["auto 6-spd", "manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 580_000, "max": 750_000},
            "new_price_egp_2024": {"min": 505_000, "max": 655_000},
            "trims_egypt": ["Feel", "Shine"],
        },
        "C3 Aircross": {
            "first_year_global": 2017,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "U34 (1st)", "years": "2017-present", "facelift": "2021"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech turbo", "hp": 130, "torque_nm": 230, "trans": ["auto 6-spd EAT6"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_100_000},
            "new_price_egp_2024": {"min": 740_000, "max": 960_000},
            "trims_egypt": ["Feel", "Shine"],
        },
        "C5 Aircross": {
            "first_year_global": 2017,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [
                {"gen": "A51 (2nd)", "years": "2017-present", "facelift": "2020"},
            ],
            "engines_egypt": [
                {"cc": 1598, "label": "1.6T PureTech", "hp": 180, "torque_nm": 250, "trans": ["auto 8-spd EAT8"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_045_000, "max": 1_395_000},
            "trims_egypt": ["Feel", "Shine", "Shine Pack"],
        },
        "Berlingo": {
            "first_year_global": 1996,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["MPV", "7-seater"],
            "segments": ["MPV", "compact van"],
            "generations": [
                {"gen": "K9 (3rd)", "years": "2018-present"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "1.5L BlueHDi diesel", "hp": 102, "torque_nm": 250, "trans": ["manual 6-spd", "auto 8-spd EAT8"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 785_000, "max": 1_045_000},
            "trims_egypt": ["Feel"],
            "notes": "Popular family MPV / light commercial hybrid",
        },
        "C4": {
            "first_year_global": 2004,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "SUV coupe"],
            "segments": ["C-segment"],
            "generations": [
                {"gen": "B41 (3rd ë-C4)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2L PureTech 130hp", "hp": 130, "torque_nm": 230, "trans": ["auto 8-spd EAT8"]},
            ],
            "new_price_egp_2025": {"min": 1_050_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 915_000, "max": 1_175_000},
            "trims_egypt": ["Feel Pack", "Shine Pack"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # DACIA
    # ════════════════════════════════════════════════════════════════════

    "Dacia": {
        "Logan": {
            "first_year_global": 2004,
            "egypt_from": 2007,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "L90 (1st)", "years": "2004-2013"},
                {"gen": "L52 (2nd)", "years": "2013-2020"},
                {"gen": "L52 facelift (3rd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TCe 90hp", "hp": 90, "torque_nm": 160, "trans": ["manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 490_000, "max": 650_000},
            "new_price_egp_2024": {"min": 426_000, "max": 565_000},
            "trims_egypt": ["Essential", "Expression", "Extreme"],
            "notes": "Sold as both Dacia and Renault Logan in Egypt; budget segment staple",
        },
        "Sandero": {
            "first_year_global": 2008,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [
                {"gen": "B52 (2nd)", "years": "2012-2020"},
                {"gen": "BJI (3rd)", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 999, "label": "1.0L TCe 90hp", "hp": 90, "torque_nm": 160, "trans": ["manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 480_000, "max": 620_000},
            "new_price_egp_2024": {"min": 418_000, "max": 540_000},
            "trims_egypt": ["Essential", "Expression"],
        },
        "Duster": {
            "first_year_global": 2010,
            "egypt_from": 2012,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [
                {"gen": "HS (1st)", "years": "2010-2017", "facelift": "2014"},
                {"gen": "HM (2nd)", "years": "2017-2023"},
                {"gen": "3rd gen", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 1330, "label": "1.3L TCe turbo", "hp": 130, "torque_nm": 240, "trans": ["auto CVT", "manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 720_000, "max": 980_000},
            "new_price_egp_2024": {"min": 626_000, "max": 855_000},
            "trims_egypt": ["Essential", "Expression", "Extreme"],
            "notes": "Sometimes sold under Renault Duster brand in Egypt — same vehicle",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # LYNK & CO (GEELY PREMIUM SUB-BRAND)
    # ════════════════════════════════════════════════════════════════════

    "Lynk & Co": {
        "01": {
            "first_year_global": 2017,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2017-present", "facelift": "2021"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 254, "torque_nm": 350, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_130_000, "max": 1_480_000},
            "trims_egypt": ["Flagship"],
            "notes": "Geely premium sub-brand sharing Volvo CMA platform",
        },
        "05": {
            "first_year_global": 2020,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV coupe"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 254, "torque_nm": 350, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 1_950_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_700_000},
            "trims_egypt": ["Flagship"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # TESLA
    # ════════════════════════════════════════════════════════════════════

    "Tesla": {
        "Model 3": {
            "first_year_global": 2017,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["D-segment", "electric"],
            "generations": [
                {"gen": "1st gen", "years": "2017-2023"},
                {"gen": "Highland (2nd)", "years": "2023-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "LR AWD dual motor", "hp": 346, "torque_nm": 510, "trans": ["single-speed"], "range_km": 602},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_915_000, "max": 2_435_000},
            "trims_egypt": ["Standard Range", "Long Range", "Performance"],
            "notes": "Imported privately / grey market; limited official presence in Egypt",
        },
        "Model Y": {
            "first_year_global": 2020,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [
                {"gen": "1st gen", "years": "2020-present", "facelift": "2024 Juniper"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "LR AWD dual motor", "hp": 384, "torque_nm": 493, "trans": ["single-speed"], "range_km": 533},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 2_785_000},
            "trims_egypt": ["Standard Range", "Long Range", "Performance"],
            "notes": "Growing used market via personal imports; no official dealer yet",
        },
        "Model S": {
            "first_year_global": 2012,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV", "fastback"],
            "segments": ["E-segment", "luxury electric"],
            "generations": [
                {"gen": "1st gen", "years": "2012-2021"},
                {"gen": "Refresh (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Dual motor LR", "hp": 670, "torque_nm": 1050, "trans": ["single-speed"], "range_km": 652},
            ],
            "new_price_egp_2025": {"min": 5_500_000, "max": 8_000_000},
            "new_price_egp_2024": {"min": 4_785_000, "max": 6_960_000},
            "trims_egypt": ["Long Range", "Plaid"],
            "notes": "Grey market only; very limited numbers",
        },
        "Model X": {
            "first_year_global": 2015,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV", "7-seater"],
            "segments": ["D-SUV", "luxury electric"],
            "generations": [
                {"gen": "1st gen", "years": "2015-2021"},
                {"gen": "Refresh (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Dual motor LR", "hp": 670, "torque_nm": 1050, "trans": ["single-speed"], "range_km": 560},
            ],
            "new_price_egp_2025": {"min": 6_500_000, "max": 10_000_000},
            "new_price_egp_2024": {"min": 5_655_000, "max": 8_700_000},
            "trims_egypt": ["Long Range", "Plaid"],
            "notes": "Falcon-wing doors; ultra-luxury segment; grey market only",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # KAIYI (CHERY × FAW JOINT VENTURE — SOLD IN EGYPT)
    # ════════════════════════════════════════════════════════════════════

    "Kaiyi": {
        "E5": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 550_000, "max": 720_000},
            "new_price_egp_2024": {"min": 478_000, "max": 626_000},
            "trims_egypt": ["Comfort", "Luxury"],
            "notes": "Chery-related brand; budget compact sedan",
        },
        "X3": {
            "first_year_global": 2022,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 145, "torque_nm": 210, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 620_000, "max": 800_000},
            "new_price_egp_2024": {"min": 540_000, "max": 695_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # FAW (FIRST AUTO WORKS)
    # ════════════════════════════════════════════════════════════════════

    "FAW": {
        "Bestune T77": {
            "first_year_global": 2018,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2018-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 167, "torque_nm": 285, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 680_000, "max": 880_000},
            "new_price_egp_2024": {"min": 592_000, "max": 765_000},
            "trims_egypt": ["Luxury", "Sport"],
        },
        "Bestune T99": {
            "first_year_global": 2019,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2019-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 252, "torque_nm": 390, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_050_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 915_000, "max": 1_220_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
        "Oley A60": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 156, "torque_nm": 230, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 530_000, "max": 700_000},
            "new_price_egp_2024": {"min": 460_000, "max": 610_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # FOTON (COMMERCIAL / PICKUP — POPULAR IN EGYPT)
    # ════════════════════════════════════════════════════════════════════

    "Foton": {
        "Tunland": {
            "first_year_global": 2012,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["pickup truck"],
            "segments": ["pickup", "light commercial"],
            "generations": [
                {"gen": "E (1st)", "years": "2012-2021"},
                {"gen": "G (2nd)", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T diesel turbo", "hp": 150, "torque_nm": 350, "trans": ["manual 6-spd", "auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_200_000},
            "new_price_egp_2024": {"min": 785_000, "max": 1_045_000},
            "trims_egypt": ["Standard", "Luxury"],
            "notes": "Popular budget pickup; competes with Navara/Hilux at lower price",
        },
        "Sauvana": {
            "first_year_global": 2016,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2016-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T diesel turbo", "hp": 160, "torque_nm": 360, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_450_000},
            "new_price_egp_2024": {"min": 960_000, "max": 1_265_000},
            "trims_egypt": ["Luxury", "Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SERES (HUAWEI AITO — GROWING IN EGYPT)
    # ════════════════════════════════════════════════════════════════════

    "Seres": {
        "SF5": {
            "first_year_global": 2021,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV PHEV"],
            "segments": ["C-SUV", "plug-in hybrid"],
            "generations": [{"gen": "1st gen Huawei HI", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T + EV PHEV", "hp": 551, "torque_nm": 820, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_400_000},
            "new_price_egp_2024": {"min": 1_565_000, "max": 2_090_000},
            "trims_egypt": ["Premium"],
            "notes": "Developed with Huawei; growing premium EV brand in Egypt",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # ROX (independent Chinese EV — JV with El Sewedy / ESI in Egypt)
    # ════════════════════════════════════════════════════════════════════

    "ROX": {
        "ROX 01": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": "ESI (El Sewedy Industrial, future assembly planned 2027)",
            "body_types": ["SUV", "REEV"],
            "segments": ["C-SUV", "extended-range EV"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2T REEV range extender + EV", "hp": 326, "torque_nm": 500, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_300_000, "max": 1_700_000},
            "new_price_egp_2024": {"min": 1_131_000, "max": 1_479_000},
            "trims_egypt": ["Standard", "Premium"],
            "notes": "Range-extended EV; distributed via Nour ElDin ElSherif Group; JV factory planned for 6th October City 2027",
        },
        "Adamas": {
            "first_year_global": 2024,
            "egypt_from": 2025,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "REEV", "7-seater"],
            "segments": ["D-SUV", "extended-range EV"],
            "generations": [{"gen": "1st gen", "years": "2024-present"}],
            "engines_egypt": [
                {"cc": 1199, "label": "1.2T REEV + dual motor EV AWD", "hp": 476, "torque_nm": 750, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_262_000},
            "trims_egypt": ["Flagship"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # XIAOMI (grey market only — no official importer in Egypt)
    # ════════════════════════════════════════════════════════════════════

    "Xiaomi": {
        "SU7": {
            "first_year_global": 2024,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan", "EV"],
            "segments": ["D-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2024-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 73.6kWh RWD", "hp": 299, "torque_nm": 400, "trans": ["single-speed"]},
                {"cc": 0, "label": "Electric 101kWh AWD Ultra", "hp": 673, "torque_nm": 838, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_300_000, "max": 3_000_000},
            "new_price_egp_2024": {"min": 2_000_000, "max": 2_610_000},
            "trims_egypt": ["Standard", "Pro", "Ultra"],
            "notes": "Grey market / parallel import only; no official dealer in Egypt as of 2025",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SOUEAST (major volume brand — distributed via AHC group)
    # ════════════════════════════════════════════════════════════════════

    "Soueast": {
        "DX5": {
            "first_year_global": 2016,
            "egypt_from": 2019,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["B-SUV", "C-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2016-2021"},
                {"gen": "2nd gen", "years": "2021-present"},
            ],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 150, "torque_nm": 230, "trans": ["auto 6-spd DCT"]},
                {"cc": 1997, "label": "2.0T turbo", "hp": 200, "torque_nm": 330, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 550_000, "max": 750_000},
            "new_price_egp_2024": {"min": 479_000, "max": 653_000},
            "trims_egypt": ["Comfort", "Luxury", "Elite"],
            "notes": "High-volume brand; one of fastest-selling Chinese SUVs in Egypt",
        },
        "DX7": {
            "first_year_global": 2017,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV", "D-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2017-2022"},
                {"gen": "2nd gen DX7S", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 218, "torque_nm": 350, "trans": ["auto 6-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 609_000, "max": 826_000},
            "trims_egypt": ["Luxury", "Elite"],
        },
        "A5": {
            "first_year_global": 2018,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["C-segment"],
            "generations": [{"gen": "1st gen", "years": "2018-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 143, "torque_nm": 210, "trans": ["auto 6-spd CVT"]},
            ],
            "new_price_egp_2025": {"min": 480_000, "max": 650_000},
            "new_price_egp_2024": {"min": 418_000, "max": 566_000},
            "trims_egypt": ["Comfort", "Luxury"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # DEEPAL (Changan EV sub-brand — entered Egypt 2024)
    # ════════════════════════════════════════════════════════════════════

    "Deepal": {
        "S7": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 66.8kWh", "hp": 218, "torque_nm": 320, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_350_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_175_000},
            "trims_egypt": ["Standard Range", "Long Range"],
        },
        "L07": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["C-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 66.8kWh", "hp": 218, "torque_nm": 320, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 827_000, "max": 1_088_000},
            "trims_egypt": ["Standard", "Long Range"],
        },
        "SL03": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["coupe sedan EV/REEV"],
            "segments": ["D-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 77.4kWh / REEV PHEV", "hp": 249, "torque_nm": 360, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_600_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_392_000},
            "trims_egypt": ["EV", "REEV"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # ZEEKR (Geely premium EV — entered Egypt 2024/25)
    # ════════════════════════════════════════════════════════════════════

    "Zeekr": {
        "001": {
            "first_year_global": 2021,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["shooting brake EV"],
            "segments": ["D-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 100kWh AWD", "hp": 544, "torque_nm": 768, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 2_784_000},
            "trims_egypt": ["WE", "YOU"],
        },
        "X": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV", "compact"],
            "segments": ["B-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 66kWh AWD", "hp": 422, "torque_nm": 543, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_740_000},
            "trims_egypt": ["Premium", "Premium Pro"],
        },
        "7X": {
            "first_year_global": 2024,
            "egypt_from": 2025,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2024-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 100kWh AWD", "hp": 641, "torque_nm": 710, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_914_000, "max": 2_436_000},
            "trims_egypt": ["Long Range", "Ultra"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # XPENG (entered Egypt via parallel/grey-market channels)
    # ════════════════════════════════════════════════════════════════════

    "XPeng": {
        "G9": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["D-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 98kWh AWD", "hp": 551, "torque_nm": 717, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_000_000, "max": 2_600_000},
            "new_price_egp_2024": {"min": 1_740_000, "max": 2_262_000},
            "trims_egypt": ["Standard", "Pro"],
        },
        "P7": {
            "first_year_global": 2020,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["D-segment", "electric"],
            "generations": [
                {"gen": "1st gen", "years": "2020-2022"},
                {"gen": "2nd gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 80.7kWh RWD", "hp": 310, "torque_nm": 430, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_600_000, "max": 2_100_000},
            "new_price_egp_2024": {"min": 1_392_000, "max": 1_827_000},
            "trims_egypt": ["Standard Range", "Long Range"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # IM MOTORS (SAIC premium EV — entered Egypt 2024)
    # ════════════════════════════════════════════════════════════════════

    "IM Motors": {
        "L7": {
            "first_year_global": 2022,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["E-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2022-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 90kWh AWD", "hp": 536, "torque_nm": 725, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_200_000, "max": 2_800_000},
            "new_price_egp_2024": {"min": 1_914_000, "max": 2_436_000},
            "trims_egypt": ["Premium", "Performance"],
        },
        "LS7": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["D-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 93kWh AWD", "hp": 582, "torque_nm": 725, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 2_500_000, "max": 3_200_000},
            "new_price_egp_2024": {"min": 2_175_000, "max": 2_784_000},
            "trims_egypt": ["Premium", "Top"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # JAECOO (Chery off-road sub-brand — launched Egypt 2024)
    # ════════════════════════════════════════════════════════════════════

    "JAECOO": {
        "J7": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "off-road"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo", "hp": 147, "torque_nm": 220, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 609_000, "max": 826_000},
            "trims_egypt": ["Standard", "Luxury"],
            "notes": "Positioned as rugged off-road alternative; Chery off-road sub-brand",
        },
        "J8": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV", "7-seater", "off-road"],
            "segments": ["D-SUV"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 1997, "label": "2.0T turbo", "hp": 268, "torque_nm": 390, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 826_000, "max": 1_131_000},
            "trims_egypt": ["Luxury", "Flagship"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # WULING (SAIC-GM-Wuling — budget mini EV segment)
    # ════════════════════════════════════════════════════════════════════

    "Wuling": {
        "Mini EV": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["city car EV"],
            "segments": ["A-segment", "electric"],
            "generations": [{"gen": "1st gen Hongguang Mini", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 9.2kWh / 26.5kWh", "hp": 26, "torque_nm": 85, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 200_000, "max": 350_000},
            "new_price_egp_2024": {"min": 174_000, "max": 305_000},
            "trims_egypt": ["Base", "Macaron"],
            "notes": "Ultra-budget 4-seat city EV; most affordable EV in Egypt",
        },
        "Yep": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["mini SUV EV"],
            "segments": ["A-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 30kWh", "hp": 68, "torque_nm": 130, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 350_000, "max": 500_000},
            "new_price_egp_2024": {"min": 305_000, "max": 435_000},
            "trims_egypt": ["Standard"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # LEAPMOTOR (Stellantis-partnered Chinese EV — Egypt 2024)
    # ════════════════════════════════════════════════════════════════════

    "Leapmotor": {
        "C10": {
            "first_year_global": 2023,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV"],
            "segments": ["C-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2023-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 69.9kWh RWD", "hp": 218, "torque_nm": 320, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 950_000, "max": 1_300_000},
            "new_price_egp_2024": {"min": 826_000, "max": 1_131_000},
            "trims_egypt": ["Standard Range", "Extended Range"],
            "notes": "Stellantis partnership helps with global distribution including Egypt",
        },
        "C11": {
            "first_year_global": 2021,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV/PHEV"],
            "segments": ["C-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2021-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 90kWh AWD EREV", "hp": 422, "torque_nm": 720, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_100_000, "max": 1_500_000},
            "new_price_egp_2024": {"min": 957_000, "max": 1_305_000},
            "trims_egypt": ["Pure EV", "EREV"],
        },
        "T03": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback EV", "city car"],
            "segments": ["A-segment", "electric"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 41kWh", "hp": 95, "torque_nm": 158, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 380_000, "max": 530_000},
            "new_price_egp_2024": {"min": 331_000, "max": 461_000},
            "trims_egypt": ["Standard"],
        },
        "C16": {
            "first_year_global": 2024,
            "egypt_from": 2025,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV", "7-seater"],
            "segments": ["D-SUV", "electric"],
            "generations": [{"gen": "1st gen", "years": "2024-present"}],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 100kWh AWD EREV", "hp": 544, "torque_nm": 710, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_400_000, "max": 1_900_000},
            "new_price_egp_2024": {"min": 1_218_000, "max": 1_653_000},
            "trims_egypt": ["Standard", "Performance"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # GAC AION (GAC pure-EV sub-brand — fast-growing in Egypt)
    # ════════════════════════════════════════════════════════════════════

    "GAC Aion": {
        "Y": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV EV", "compact"],
            "segments": ["B-SUV", "electric"],
            "generations": [
                {"gen": "1st gen", "years": "2020-2022"},
                {"gen": "2nd gen Y Plus", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 70.8kWh", "hp": 201, "torque_nm": 350, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 900_000, "max": 1_250_000},
            "new_price_egp_2024": {"min": 783_000, "max": 1_088_000},
            "trims_egypt": ["Standard", "Long Range Plus"],
            "notes": "One of best-selling Chinese EVs in Egypt",
        },
        "V": {
            "first_year_global": 2019,
            "egypt_from": 2024,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan EV"],
            "segments": ["D-segment", "electric"],
            "generations": [
                {"gen": "1st gen", "years": "2019-2022"},
                {"gen": "2nd gen V Plus", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 0, "label": "Electric 80kWh", "hp": 245, "torque_nm": 430, "trans": ["single-speed"]},
            ],
            "new_price_egp_2025": {"min": 1_000_000, "max": 1_400_000},
            "new_price_egp_2024": {"min": 870_000, "max": 1_218_000},
            "trims_egypt": ["Standard", "Long Range"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SEAT (Volkswagen Group — distributed via Arabiat Egypt)
    # ════════════════════════════════════════════════════════════════════

    "SEAT": {
        "Ibiza": {
            "first_year_global": 1984,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment"],
            "generations": [{"gen": "5th gen KJ", "years": "2017-present"}],
            "engines_egypt": [
                {"cc": 999, "label": "1.0 TSI 95hp", "hp": 95, "torque_nm": 175, "trans": ["manual 5-spd", "auto 7-spd DSG"]},
                {"cc": 999, "label": "1.0 TSI 115hp", "hp": 115, "torque_nm": 200, "trans": ["manual 6-spd", "auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 500_000, "max": 700_000},
            "new_price_egp_2024": {"min": 435_000, "max": 609_000},
            "trims_egypt": ["Reference", "Style", "FR"],
        },
        "Leon": {
            "first_year_global": 1998,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback", "estate"],
            "segments": ["C-segment"],
            "generations": [{"gen": "4th gen KL8", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5 TSI 150hp", "hp": 150, "torque_nm": 250, "trans": ["manual 6-spd", "auto 7-spd DSG"]},
                {"cc": 1984, "label": "2.0 TDI 150hp diesel", "hp": 150, "torque_nm": 360, "trans": ["manual 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 609_000, "max": 826_000},
            "trims_egypt": ["Reference", "Style", "FR"],
        },
        "Ateca": {
            "first_year_global": 2016,
            "egypt_from": 2021,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["C-SUV"],
            "generations": [{"gen": "1st gen KH7", "years": "2016-present", "facelift": "2020"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5 TSI 150hp", "hp": 150, "torque_nm": 250, "trans": ["auto 7-spd DSG"]},
                {"cc": 1984, "label": "2.0 TDI 150hp diesel", "hp": 150, "torque_nm": 340, "trans": ["auto 7-spd DSG"]},
            ],
            "new_price_egp_2025": {"min": 850_000, "max": 1_150_000},
            "new_price_egp_2024": {"min": 740_000, "max": 1_001_000},
            "trims_egypt": ["Style", "Xperience"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # MINI (BMW Group — Global Auto Group Egypt)
    # ════════════════════════════════════════════════════════════════════

    "MINI": {
        "Cooper": {
            "first_year_global": 1959,
            "egypt_from": 2015,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["hatchback"],
            "segments": ["B-segment", "premium"],
            "generations": [
                {"gen": "3rd gen F55/F56", "years": "2014-2024"},
                {"gen": "4th gen J01", "years": "2024-present"},
            ],
            "engines_egypt": [
                {"cc": 1499, "label": "1.5T 3-cyl 136hp", "hp": 136, "torque_nm": 220, "trans": ["auto 7-spd DCT"]},
                {"cc": 1998, "label": "2.0T 178hp Cooper S", "hp": 178, "torque_nm": 280, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 1_200_000, "max": 1_800_000},
            "new_price_egp_2024": {"min": 1_044_000, "max": 1_566_000},
            "trims_egypt": ["Cooper", "Cooper S", "JCW"],
        },
        "Countryman": {
            "first_year_global": 2010,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV crossover"],
            "segments": ["C-SUV", "premium"],
            "generations": [
                {"gen": "2nd gen F60", "years": "2017-2024"},
                {"gen": "3rd gen U25", "years": "2024-present"},
            ],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T 178hp", "hp": 178, "torque_nm": 280, "trans": ["auto 7-spd DCT"]},
                {"cc": 1998, "label": "2.0T 231hp Cooper S ALL4", "hp": 231, "torque_nm": 350, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_800_000, "max": 2_500_000},
            "new_price_egp_2024": {"min": 1_566_000, "max": 2_175_000},
            "trims_egypt": ["Countryman", "Countryman S", "JCW"],
        },
        "Clubman": {
            "first_year_global": 2007,
            "egypt_from": 2018,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["estate"],
            "segments": ["C-segment", "premium"],
            "generations": [{"gen": "2nd gen F54", "years": "2015-2024"}],
            "engines_egypt": [
                {"cc": 1998, "label": "2.0T 192hp Cooper S", "hp": 192, "torque_nm": 280, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 1_500_000, "max": 2_000_000},
            "new_price_egp_2024": {"min": 1_305_000, "max": 1_740_000},
            "trims_egypt": ["Cooper S", "JCW"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # PROTON (Malaysia — SMG Engineering Egypt)
    # ════════════════════════════════════════════════════════════════════

    "Proton": {
        "X50": {
            "first_year_global": 2020,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": "SMG Engineering",
            "body_types": ["SUV crossover"],
            "segments": ["B-SUV"],
            "generations": [{"gen": "1st gen", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 1498, "label": "1.5T turbo 150hp (Geely-derived)", "hp": 150, "torque_nm": 226, "trans": ["auto 7-spd DCT"]},
            ],
            "new_price_egp_2025": {"min": 550_000, "max": 750_000},
            "new_price_egp_2024": {"min": 479_000, "max": 653_000},
            "trims_egypt": ["Standard", "Executive", "Flagship"],
            "notes": "Uses Geely BMA platform; Geely subsidiary brand",
        },
        "X70": {
            "first_year_global": 2018,
            "egypt_from": 2022,
            "assembled_in_egypt": False,
            "assembler": "SMG Engineering",
            "body_types": ["SUV", "7-seater"],
            "segments": ["C-SUV", "D-SUV"],
            "generations": [
                {"gen": "1st gen", "years": "2018-2022"},
                {"gen": "2nd gen", "years": "2022-present"},
            ],
            "engines_egypt": [
                {"cc": 1799, "label": "1.8T turbo 184hp", "hp": 184, "torque_nm": 300, "trans": ["auto 6-spd"]},
            ],
            "new_price_egp_2025": {"min": 700_000, "max": 950_000},
            "new_price_egp_2024": {"min": 609_000, "max": 826_000},
            "trims_egypt": ["Executive", "Premium"],
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # SHINERAY (Chinese utility — vans/minivans, commercial use)
    # ════════════════════════════════════════════════════════════════════

    "Shineray": {
        "X30": {
            "first_year_global": 2013,
            "egypt_from": 2020,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["MPV", "van"],
            "segments": ["commercial", "van"],
            "generations": [{"gen": "1st gen", "years": "2013-present"}],
            "engines_egypt": [
                {"cc": 1497, "label": "1.5L naturally aspirated", "hp": 102, "torque_nm": 138, "trans": ["manual 5-spd"]},
            ],
            "new_price_egp_2025": {"min": 250_000, "max": 380_000},
            "new_price_egp_2024": {"min": 218_000, "max": 331_000},
            "trims_egypt": ["Cargo", "Passenger"],
            "notes": "Popular budget commercial MPV/van in Egyptian micro-business segment",
        },
    },

    # ════════════════════════════════════════════════════════════════════
    # GENESIS (Hyundai luxury — limited presence in Egypt)
    # ════════════════════════════════════════════════════════════════════

    "Genesis": {
        "GV80": {
            "first_year_global": 2020,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["SUV"],
            "segments": ["E-SUV", "luxury"],
            "generations": [{"gen": "1st gen JX1", "years": "2020-present"}],
            "engines_egypt": [
                {"cc": 2497, "label": "2.5T inline-6 300hp", "hp": 300, "torque_nm": 422, "trans": ["auto 8-spd"]},
                {"cc": 2999, "label": "3.5T V6 375hp", "hp": 375, "torque_nm": 530, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_500_000, "max": 5_000_000},
            "new_price_egp_2024": {"min": 3_045_000, "max": 4_350_000},
            "trims_egypt": ["2.5T Advanced", "3.5T Prestige"],
            "notes": "Hyundai's ultra-premium brand; limited dealership presence in Egypt",
        },
        "G80": {
            "first_year_global": 2016,
            "egypt_from": 2023,
            "assembled_in_egypt": False,
            "assembler": None,
            "body_types": ["sedan"],
            "segments": ["E-segment", "luxury"],
            "generations": [
                {"gen": "1st gen DH", "years": "2016-2020"},
                {"gen": "2nd gen RG3", "years": "2020-present"},
            ],
            "engines_egypt": [
                {"cc": 2497, "label": "2.5T inline-6 300hp", "hp": 300, "torque_nm": 422, "trans": ["auto 8-spd"]},
                {"cc": 3497, "label": "3.5T V6 375hp", "hp": 375, "torque_nm": 530, "trans": ["auto 8-spd"]},
            ],
            "new_price_egp_2025": {"min": 3_000_000, "max": 4_500_000},
            "new_price_egp_2024": {"min": 2_610_000, "max": 3_915_000},
            "trims_egypt": ["2.5T", "3.5T"],
        },
    },
}


# ─── Quick-lookup helpers ──────────────────────────────────────────────────────

def get_model_info(make: str, model: str) -> dict | None:
    """Return full catalog entry for (make, model) or None."""
    return CATALOG.get(make, {}).get(model)


def get_new_price_range(make: str, model: str, year: int = 2025) -> tuple[int | None, int | None]:
    """Return (min_egp, max_egp) for new car price. year = 2024 or 2025."""
    info = get_model_info(make, model)
    if not info:
        return None, None
    key = f"new_price_egp_{year}"
    p = info.get(key, {})
    return p.get("min"), p.get("max")


def get_all_makes() -> list[str]:
    return sorted(CATALOG.keys())


def get_models_for_make(make: str) -> list[str]:
    return sorted(CATALOG.get(make, {}).keys())


def get_generation_for_year(make: str, model: str, year: int) -> dict | None:
    """Return the generation dict that covers the given year."""
    info = get_model_info(make, model)
    if not info:
        return None
    for gen in info.get("generations", []):
        start_str = gen["years"].split("-")[0].strip()
        end_str   = gen["years"].split("-")[-1].strip()
        try:
            start = int(start_str)
            end   = 2099 if end_str == "present" else int(end_str)
            if start <= year <= end:
                return gen
        except ValueError:
            continue
    return None


def is_assembled_in_egypt(make: str, model: str) -> bool:
    info = get_model_info(make, model)
    return bool(info and info.get("assembled_in_egypt"))
