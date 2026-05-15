# Concrete mix design data — KDS 14 20 10 / KCS 14 20 10 / ACI 318

BUILDING_BASE = {
    "residential": {"name": "Residential Building",          "base_fck": 21},
    "commercial":  {"name": "Commercial / Office Building",  "base_fck": 27},
    "industrial":  {"name": "Industrial Facility",           "base_fck": 27},
    "bridge":      {"name": "Bridge",                        "base_fck": 30},
    "retaining":   {"name": "Retaining Wall",                "base_fck": 21},
    "pavement":    {"name": "Road Pavement",                 "base_fck": 27},
    "dam":         {"name": "Dam / Hydraulic Structure",     "base_fck": 24},
}

# Use-case replaces exposure — maps to an internal exposure key
USE_CASES = {
    "general_indoor":  {
        "name":     "General Indoor Structure",
        "exposure": "normal",
        "hint":     "Offices, residential interiors, shopping malls, protected spaces",
    },
    "general_outdoor": {
        "name":     "Outdoor / Exposed Structure",
        "exposure": "normal",
        "hint":     "Exterior walls, driveways, parking lots, uncovered slabs",
    },
    "coastal_marine":  {
        "name":     "Coastal / Marine Structure",
        "exposure": "marine",
        "hint":     "Seawalls, piers, coastal buildings within ~1 mile of ocean",
    },
    "underground":     {
        "name":     "Underground / Below Grade",
        "exposure": "sulfate",
        "hint":     "Foundations in sulfate-rich soil, basements, retaining walls",
    },
    "bridge_highway":  {
        "name":     "Bridge / Highway Structure",
        "exposure": "freeze",
        "hint":     "Bridges, overpasses, highway pavements, transportation infrastructure",
    },
    "industrial_chem": {
        "name":     "Industrial / Chemical Facility",
        "exposure": "sulfate",
        "hint":     "Chemical plants, wastewater treatment, industrial floors",
    },
    "water_retaining": {
        "name":     "Water-Retaining Structure",
        "exposure": "marine",
        "hint":     "Swimming pools, water tanks, reservoirs, irrigation canals",
    },
    "high_rise":       {
        "name":     "High-Rise Building",
        "exposure": "normal",
        "hint":     "Multi-story buildings requiring high pump pressure and special mix design",
    },
}

MEMBER_NAMES = {
    "foundation": "Foundation",
    "column":     "Column",
    "beam":       "Beam",
    "slab":       "Slab",
    "wall":       "Wall",
}

# Region-based material unit prices (USD/kg) — 2025 estimates
REGIONS = {
    "fl_south":  {
        "name":   "South Florida (Miami / Fort Lauderdale / Palm Beach)",
        "prices": {"cement": 0.175, "slag": 0.105, "flyash": 0.070,
                   "water": 0.001, "superplasticizer": 3.80,
                   "coarseagg": 0.018, "fineagg": 0.016},
    },
    "fl_central": {
        "name":   "Central Florida (Orlando / Kissimmee)",
        "prices": {"cement": 0.155, "slag": 0.092, "flyash": 0.062,
                   "water": 0.001, "superplasticizer": 3.60,
                   "coarseagg": 0.016, "fineagg": 0.013},
    },
    "fl_tampa":  {
        "name":   "Tampa Bay (Tampa / St. Petersburg / Sarasota)",
        "prices": {"cement": 0.160, "slag": 0.096, "flyash": 0.060,
                   "water": 0.001, "superplasticizer": 3.65,
                   "coarseagg": 0.016, "fineagg": 0.013},
    },
    "fl_north":  {
        "name":   "North Florida (Jacksonville / Tallahassee)",
        "prices": {"cement": 0.148, "slag": 0.088, "flyash": 0.055,
                   "water": 0.001, "superplasticizer": 3.40,
                   "coarseagg": 0.014, "fineagg": 0.011},
    },
    "ga":        {
        "name":   "Georgia (Atlanta area)",
        "prices": {"cement": 0.145, "slag": 0.085, "flyash": 0.050,
                   "water": 0.001, "superplasticizer": 3.30,
                   "coarseagg": 0.013, "fineagg": 0.011},
    },
    "tx":        {
        "name":   "Texas (Houston / Dallas)",
        "prices": {"cement": 0.140, "slag": 0.082, "flyash": 0.048,
                   "water": 0.001, "superplasticizer": 3.20,
                   "coarseagg": 0.012, "fineagg": 0.010},
    },
    "ne":        {
        "name":   "Northeast US (New York / Boston)",
        "prices": {"cement": 0.180, "slag": 0.108, "flyash": 0.070,
                   "water": 0.001, "superplasticizer": 3.90,
                   "coarseagg": 0.022, "fineagg": 0.019},
    },
    "mw":        {
        "name":   "Midwest US (Chicago / Detroit)",
        "prices": {"cement": 0.150, "slag": 0.088, "flyash": 0.055,
                   "water": 0.001, "superplasticizer": 3.45,
                   "coarseagg": 0.014, "fineagg": 0.012},
    },
    "ca":        {
        "name":   "California (Los Angeles / Bay Area)",
        "prices": {"cement": 0.185, "slag": 0.110, "flyash": 0.075,
                   "water": 0.002, "superplasticizer": 4.00,
                   "coarseagg": 0.020, "fineagg": 0.018},
    },
}

# Default prices — Central Florida
MATERIAL_PRICES = REGIONS["fl_central"]["prices"]

# Max W/C ratio by exposure condition (%)
EXPOSURE_MAX_WC = {
    "normal":  65,
    "freeze":  45,
    "sulfate": 40,
    "marine":  40,
}

EXPOSURE_NAMES = {
    "normal":  "Normal (Indoor / Dry)",
    "freeze":  "Freeze-Thaw (Outdoor Exposure)",
    "sulfate": "Sulfate Exposure",
    "marine":  "Marine / Chloride Exposure",
}

# Mix design data per fck grade (unit quantities in kg/m³)
MIX_DATA = {
    18: {"wc_max": 65, "cement": 270, "water": 175, "mix": "1 : 2.6 : 4.6", "coarseagg": 1130, "fineagg": 780, "sp": 0},
    21: {"wc_max": 60, "cement": 295, "water": 175, "mix": "1 : 2.2 : 4.0", "coarseagg": 1100, "fineagg": 750, "sp": 0},
    24: {"wc_max": 55, "cement": 320, "water": 175, "mix": "1 : 1.9 : 3.5", "coarseagg": 1070, "fineagg": 720, "sp": 0},
    27: {"wc_max": 50, "cement": 355, "water": 175, "mix": "1 : 1.7 : 3.0", "coarseagg": 1050, "fineagg": 700, "sp": 2},
    30: {"wc_max": 47, "cement": 375, "water": 175, "mix": "1 : 1.5 : 2.7", "coarseagg": 1020, "fineagg": 680, "sp": 4},
    35: {"wc_max": 43, "cement": 410, "water": 175, "mix": "1 : 1.3 : 2.3", "coarseagg": 990,  "fineagg": 650, "sp": 6},
    40: {"wc_max": 40, "cement": 445, "water": 178, "mix": "1 : 1.1 : 2.0", "coarseagg": 970,  "fineagg": 620, "sp": 10},
    50: {"wc_max": 35, "cement": 500, "water": 175, "mix": "1 : 0.9 : 1.6", "coarseagg": 940,  "fineagg": 580, "sp": 15},
}

FCK_GRADES = [18, 21, 24, 27, 30, 35, 40, 50]

# Material guide cards
MATERIAL_INFO = [
    {
        "key": "cement", "name": "Cement", "name_en": "Ordinary Portland Cement",
        "role": "Primary binder — essential in all concrete",
        "used_in": "All concrete structures without exception",
        "effect": "More cement → higher strength, higher cost, more heat of hydration → cracking risk",
        "price_per_ton": 155, "color": "#2563eb", "icon": "🔵",
    },
    {
        "key": "slag", "name": "Blast Furnace Slag", "name_en": "Ground Granulated Blast-Furnace Slag (GGBS)",
        "role": "Cement substitute — pozzolanic reaction",
        "used_in": "Marine structures, underground structures, sulfate-exposed environments",
        "effect": "Durability↑, long-term strength↑, heat of hydration↓, ~40% cheaper than cement",
        "price_per_ton": 92, "color": "#7c3aed", "icon": "🟣",
    },
    {
        "key": "flyash", "name": "Fly Ash", "name_en": "Coal Combustion By-product",
        "role": "Cement substitute — recycled coal power plant by-product",
        "used_in": "Mass concrete (dams, large foundations), heat-of-hydration control",
        "effect": "Long-term strength↑, heat of hydration↓↓, workability↑, most economical SCM",
        "price_per_ton": 62, "color": "#64748b", "icon": "⚫",
    },
    {
        "key": "water", "name": "Water", "name_en": "Mixing Water",
        "role": "Hydration medium",
        "used_in": "All concrete",
        "effect": "W/C ratio is the key driver of strength — less water = higher strength (workability↓)",
        "price_per_ton": 1, "color": "#0ea5e9", "icon": "💧",
    },
    {
        "key": "superplasticizer", "name": "Superplasticizer", "name_en": "High-Range Water Reducer (HRWR)",
        "role": "Chemical admixture — workability without extra water",
        "used_in": "High-strength concrete (fck ≥ 35 MPa), super high-rise, self-compacting concrete",
        "effect": "Increases workability without raising W/C → maintains strength. Highest unit cost",
        "price_per_ton": 3600, "color": "#dc2626", "icon": "🔴",
    },
    {
        "key": "coarseagg", "name": "Coarse Aggregate", "name_en": "Gravel / Crushed Stone",
        "role": "Structural skeleton aggregate",
        "used_in": "General concrete structures",
        "effect": "Economical volume filler, reduces drying shrinkage. Max size set by member dimensions",
        "price_per_ton": 16, "color": "#92400e", "icon": "🟤",
    },
    {
        "key": "fineagg", "name": "Fine Aggregate", "name_en": "Sand",
        "role": "Filler aggregate",
        "used_in": "All concrete",
        "effect": "Workability↑, surface finish↑, void filling. Higher ratio → more unit water needed",
        "price_per_ton": 13, "color": "#d97706", "icon": "🟡",
    },
]


# ── Internal helpers ──────────────────────────────────────────

def _floor_adjusted_fck(base_fck, floors):
    if floors <= 5:   return base_fck
    if floors <= 15:  return max(base_fck, 27)
    if floors <= 30:  return max(base_fck, 35)
    return max(base_fck, 40)


def _nearest_grade(target):
    for g in FCK_GRADES:
        if g >= target:
            return g
    return 50


def _cement_type(fck, exposure):
    if exposure == "sulfate":
        return "Sulfate-Resistant Cement (ASTM C150 Type V)"
    if exposure == "marine":
        return "Slag Cement (ASTM C989) or Fly Ash Blended Cement (ASTM C595)"
    if fck >= 40:
        return "Type I/II Portland Cement + Silica Fume (SF) 5~10%"
    if fck >= 35:
        return "Type I/II Portland Cement + supplementary cementitious material recommended"
    return "Type I/II Portland Cement (ASTM C150)"


def _slump(member):
    return {
        "foundation": "2 ~ 3 in  (50 ~ 80 mm)",
        "column":     "4 ~ 6 in  (100 ~ 150 mm)",
        "beam":       "4 ~ 7 in  (100 ~ 180 mm)",
        "slab":       "4 ~ 7 in  (100 ~ 180 mm)",
        "wall":       "4 ~ 6 in  (100 ~ 150 mm)",
    }.get(member, "4 ~ 6 in  (100 ~ 150 mm)")


def calculate_cost(cement, slag, flyash, water, sp, coarseagg, fineagg, prices=None):
    p = prices if prices else MATERIAL_PRICES
    bd = {
        "cement":           round(cement    * p["cement"],           2),
        "slag":             round(slag      * p["slag"],             2),
        "flyash":           round(flyash    * p["flyash"],           2),
        "water":            round(water     * p["water"],            2),
        "superplasticizer": round(sp        * p["superplasticizer"], 2),
        "coarseagg":        round(coarseagg * p["coarseagg"],        2),
        "fineagg":          round(fineagg   * p["fineagg"],          2),
    }
    bd["total"] = round(sum(bd.values()), 2)
    return bd


# ── Main recommendation function ──────────────────────────────

def get_recommendation(building_type, floors, use_case, member, custom_prices=None):
    building  = BUILDING_BASE.get(building_type, BUILDING_BASE["residential"])
    uc        = USE_CASES.get(use_case, USE_CASES["general_indoor"])
    exposure  = uc["exposure"]
    base_fck  = building["base_fck"]

    if building_type in ("residential", "commercial", "industrial"):
        base_fck = _floor_adjusted_fck(base_fck, floors)

    max_wc = EXPOSURE_MAX_WC.get(exposure, 65)

    fck = _nearest_grade(base_fck)
    for g in FCK_GRADES:
        if g >= base_fck and MIX_DATA[g]["wc_max"] <= max_wc:
            fck = g
            break

    mix          = MIX_DATA[fck]
    actual_wc    = min(mix["wc_max"], max_wc)
    actual_water = int(mix["cement"] * actual_wc / 100)
    slag_kg      = 0
    flyash_kg    = 0
    sp_kg        = mix["sp"]
    coarseagg_kg = mix["coarseagg"]
    fineagg_kg   = mix["fineagg"]

    prices = custom_prices if custom_prices else MATERIAL_PRICES
    cost   = calculate_cost(mix["cement"], slag_kg, flyash_kg,
                            actual_water, sp_kg, coarseagg_kg, fineagg_kg,
                            prices=prices)

    notes = []
    if exposure == "freeze":
        notes.append("Use air-entraining admixture (AEA) — target air content 4~7% in hardened concrete")
        notes.append("Strictly maintain W/C ratio ≤ 0.45")
    if exposure == "marine":
        notes.append("Minimum concrete cover ≥ 2 in (50 mm) required (ACI 318 Table 20.6.1)")
        notes.append("Total chloride content ≤ 0.30 kg/m³")
    if exposure == "sulfate":
        notes.append("Use sulfate-resistant cement or slag / pozzolan blended cement")
    if fck >= 40:
        notes.append("High-strength concrete: strict early-age temperature curing (wet cure ≥ 7 days)")
        notes.append("Use superplasticizer (SP) to ensure pumpability")
    if floors > 30:
        notes.append("Super high-rise: account for high pump pressure — adjust water content and fine aggregate ratio")

    return {
        "building_name":  building["name"],
        "use_case_name":  uc["name"],
        "exposure_name":  EXPOSURE_NAMES.get(exposure, "Normal"),
        "member_name":    MEMBER_NAMES.get(member, member),
        "floors":         floors,
        "fck":            fck,
        "wc_ratio":       actual_wc,
        "mix_ratio":      mix["mix"],
        "cement_kg":      mix["cement"],
        "water_kg":       actual_water,
        "slag_kg":        slag_kg,
        "flyash_kg":      flyash_kg,
        "sp_kg":          sp_kg,
        "coarseagg_kg":   coarseagg_kg,
        "fineagg_kg":     fineagg_kg,
        "slump":          _slump(member),
        "cement_type":    _cement_type(fck, exposure),
        "notes":          notes,
        "cost_breakdown": cost,
        "total_cost":     cost["total"],
    }
