import requests
import re
import warnings
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Optional

warnings.filterwarnings("ignore", message="Unverified HTTPS")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}


@dataclass
class Listing:
    source: str
    title: str
    price_egp: int
    area_m2: Optional[float]
    price_per_m2: Optional[float]
    location: str
    bedrooms: Optional[int]
    finishing: Optional[str]   # detected from title/text
    floor: Optional[str]
    compound: Optional[str]
    url: str
    property_type: str

    def __post_init__(self):
        if self.price_egp and self.area_m2 and self.area_m2 > 0:
            self.price_per_m2 = round(self.price_egp / self.area_m2)


# ─── Slug helpers ─────────────────────────────────────────────────────────────

AREA_SLUG_OVERRIDES = {
    "new cairo":        "new-cairo",
    "sheikh zayed":     "sheikh-zayed",
    "6th october":      "6th-of-october",
    "6 october":        "6th-of-october",
    "sixth october":    "6th-of-october",
    "october":          "6th-of-october",
    "maadi":            "el-maadi",
    "el maadi":         "el-maadi",
    "zamalek":          "zamalek",
    "heliopolis":       "heliopolis",
    "nasr city":        "nasr-city",
    "obour":            "el-obour",
    "shorouk":          "el-shorouk-city",
    "rehab":            "el-rehab-city",
    "mostakbal":        "mostakbal-city",
    "new administrative capital": "new-administrative-capital",
    "nac":              "new-administrative-capital",
    "el gouna":         "el-gouna",
    "north coast":      "north-coast",
    "sahel":            "north-coast",
    "ain sokhna":       "ain-sokhna",
    "sokhna":           "ain-sokhna",
    "new heliopolis":   "new-heliopolis",
    "badr city":        "badr-city",
    "katameya":         "new-cairo",
    "fifth settlement": "new-cairo",
    "garden city":      "garden-city",
    "downtown cairo":   "downtown-cairo",
    "mohandessin":      "mohandessin",
    "dokki":            "dokki",
    "giza":             "giza",
    "6th of october":   "6th-of-october",
}

AQARMAP_PTYPES = {
    "apartment":  "apartments",
    "penthouse":  "apartments",        # Aqarmap has no separate penthouse category
    "duplex":     "apartments",        # duplex listed under apartments on Aqarmap
    "i_villa":    "apartments",        # i-villa = ground-floor 2-floor+roof apartment unit
    "villa":      "villas",
    "townhouse":  "townhouses",
    "twin_house": "twin-houses",
    "house":      "houses",
    "land":       "lands",
}

DUBIZZLE_PTYPES = {
    "apartment":  "apartments-duplex",
    "penthouse":  "apartments-duplex",
    "duplex":     "apartments-duplex",
    "i_villa":    "apartments-duplex",  # i-villa listed under apartments-duplex on Dubizzle
    "villa":      "villas",
    "townhouse":  "villas",
    "twin_house": "villas",
    "house":      "villas",
    "land":       "buildings-lands-other",
}


def _to_slug(text: str) -> str:
    key = text.lower().strip()
    if key in AREA_SLUG_OVERRIDES:
        return AREA_SLUG_OVERRIDES[key]
    return re.sub(r"[^a-z0-9]+", "-", key).strip("-")


def _get(url: str, **kwargs) -> requests.Response:
    return requests.get(url, headers=HEADERS, verify=False, timeout=15, **kwargs)


def _detect_ptype(text: str) -> Optional[str]:
    """
    Detect property sub-type from a listing title/description.

    i-villa: a compound apartment unit spanning 2 full floors + rooftop room.
             NOT a villa — it's an apartment product sold by compound developers.
             Common names: i-villa, ivilla, garden apartment (ground floor + roof),
             'شاليه ارضي', 'وحدة ارضية دورين', 'روف', ground duplex with roof.
    """
    t = text.lower()
    if any(w in t for w in ["penthouse", "pent house", "بنتهاوس"]):
        return "penthouse"
    if any(w in t for w in ["duplex", "دوبليكس", "دوبلكس", "دوبليس"]):
        return "duplex"
    if any(w in t for w in [
        "i-villa", "i villa", "ivilla", "آي فيلا", "آي‌فيلا",
        "garden apartment", "ground floor villa", "garden villa",
        "villa apartment", "villa unit",
    ]):
        return "i_villa"
    return None


def _match_ptype(listing_text: str, target_type: str) -> bool:
    """
    Return True if this listing matches the requested property type.

    - apartment : exclude penthouse / duplex / i_villa hits
    - penthouse : must contain penthouse keyword
    - duplex    : must contain duplex keyword
    - i_villa   : must contain i-villa keyword (ground-floor 2-floor+roof apartment)
    - villa / townhouse / twin_house : URL-level filter is sufficient
    """
    if target_type == "apartment":
        detected = _detect_ptype(listing_text)
        return detected not in ("penthouse", "duplex", "i_villa")
    if target_type in ("penthouse", "duplex", "i_villa"):
        detected = _detect_ptype(listing_text)
        return detected == target_type
    # villa, townhouse, house — accept all (URL already scoped)
    return True


def _detect_finishing(text: str) -> Optional[str]:
    t = text.lower()
    if any(w in t for w in ["furnished", "fully furnished"]):
        return "furnished"
    if any(w in t for w in ["fully finished", "full finish", "super lux", "ultra lux", "lux finish"]):
        return "fully_finished"
    if any(w in t for w in ["semi finish", "semi-finish"]):
        return "semi_finished"
    if any(w in t for w in ["core", "shell", "unfinished", "not finished"]):
        return "core_shell"
    if "finish" in t:
        return "fully_finished"
    return None


# ─── Aqarmap ──────────────────────────────────────────────────────────────────

def scrape_aqarmap(area: str, property_type: str,
                   min_area: int = 0, max_area: int = 0,
                   compound: str = "",
                   area_slug_override: str = "",
                   compound_slug_override: str = "",
                   pages: int = 1) -> list[Listing]:
    ptype = AQARMAP_PTYPES.get(property_type, "apartments")
    area_slug = area_slug_override or _to_slug(area)

    cslug = compound_slug_override or (_to_slug(compound) if compound else "")
    if cslug:
        base_url = f"https://www.aqarmap.com.eg/en/for-sale/{ptype}/egypt/{area_slug}/compounds/{cslug}/"
    else:
        base_url = f"https://www.aqarmap.com.eg/en/for-sale/{ptype}/egypt/{area_slug}/"

    listings = []
    for page in range(1, pages + 1):
        url = base_url if page == 1 else f"{base_url}?page={page}"
        try:
            resp = _get(url)
            if resp.status_code == 404 and compound and page == 1:
                base_url = f"https://www.aqarmap.com.eg/en/for-sale/{ptype}/egypt/{area_slug}/"
                resp = _get(base_url)
            if resp.status_code != 200:
                break
        except Exception as e:
            print(f"[Aqarmap] request error: {e}")
            break

        soup = BeautifulSoup(resp.text, "lxml")
        cards = soup.select("article.listing-card")
        if not cards:
            break

        for card in cards:
            try:
                price_el = card.select_one("data[value]")
                if not price_el:
                    continue
                price = int(str(price_el["value"]).replace(",", ""))
                if price <= 0:
                    continue

                title_el = card.select_one("h2")
                title = title_el.get_text(strip=True) if title_el else "Property"

                link_el = card.select_one("a[href]")
                href = link_el["href"] if link_el else ""
                full_url = href if href.startswith("http") else f"https://www.aqarmap.com.eg{href}"

                area_val = None
                for li in card.select("li"):
                    m = re.search(r"([\d,]+)\s*m²", li.get_text())
                    if m:
                        area_val = float(m.group(1).replace(",", ""))
                        break

                if min_area > 0 and area_val and area_val < min_area:
                    continue
                if max_area > 0 and area_val and area_val > max_area:
                    continue

                bedrooms = None
                for li in card.select("li"):
                    txt = li.get_text()
                    if "bedroom" in txt.lower() or re.search(r"\d+\s*bed", txt, re.I):
                        m = re.search(r"(\d+)", txt)
                        if m:
                            bedrooms = int(m.group(1))
                            break

                loc_links = card.select(".listing-card-details a[href*='/for-sale/']")
                location = loc_links[-1].get_text(strip=True) if loc_links else area
                compound_name = None
                if len(loc_links) >= 2:
                    compound_name = loc_links[-1].get_text(strip=True)

                if not _match_ptype(title, property_type):
                    continue
                listings.append(Listing(
                    source="Aqarmap",
                    title=title[:120],
                    price_egp=price,
                    area_m2=area_val,
                    price_per_m2=None,
                    location=location,
                    bedrooms=bedrooms,
                    finishing=_detect_finishing(title),
                    floor=None,
                    compound=compound_name,
                    url=full_url,
                    property_type=property_type,
                ))
            except (ValueError, TypeError, KeyError):
                continue

    return listings


# ─── Dubizzle ─────────────────────────────────────────────────────────────────

def scrape_dubizzle(area: str, property_type: str,
                    min_area: int = 0, max_area: int = 0,
                    compound: str = "",
                    area_slug_override: str = "",
                    compound_text_override: str = "",
                    pages: int = 1) -> list[Listing]:
    ptype = DUBIZZLE_PTYPES.get(property_type, "apartments-duplex")
    area_slug = area_slug_override or _to_slug(area)

    base_url = f"https://www.dubizzle.com.eg/en/properties/{ptype}-for-sale/{area_slug}/"
    compound_lower = (compound_text_override or compound).lower().strip()

    listings = []
    for page in range(1, pages + 1):
        url = base_url if page == 1 else f"{base_url}?page={page}"
        try:
            resp = _get(url)
            if resp.status_code == 404 and page == 1:
                resp = _get(f"https://www.dubizzle.com.eg/en/properties/{ptype}-for-sale/")
            if resp.status_code != 200:
                break
        except Exception as e:
            print(f"[Dubizzle] request error: {e}")
            break

        soup = BeautifulSoup(resp.text, "lxml")
        cards = soup.select("article")
        if not cards:
            break

        for card in cards:
            try:
                text = card.get_text(" ", strip=True)
                if "EGP" not in text:
                    continue

                if compound_lower and compound_lower not in text.lower():
                    continue

                pm = re.search(r"EGP\s*([\d,]+)", text)
                if not pm:
                    continue
                price = int(pm.group(1).replace(",", ""))
                if price <= 0:
                    continue

                am = re.search(r"([\d,]+)\s*m²", text)
                area_val = float(am.group(1).replace(",", "")) if am else None

                if min_area > 0 and area_val and area_val < min_area:
                    continue
                if max_area > 0 and area_val and area_val > max_area:
                    continue

                bm = re.search(r"(\d+)\s*beds?", text, re.I)
                bedrooms = int(bm.group(1)) if bm else None

                title_el = card.select_one("img[alt]")
                title = str(title_el["alt"]) if title_el else text[:80]

                link_el = card.select_one("a[href*='/en/ad/']")
                href = link_el["href"] if link_el else ""
                full_url = f"https://www.dubizzle.com.eg{href}" if href.startswith("/") else href

                loc_m = re.search(r"([^•\n]{4,60})\s*•\s*\d+\s*(?:day|hour|week|month)", text)
                if loc_m:
                    raw = re.sub(r"\s*(Completion Status|Ownership|Resale|Off-Plan|Primary|Ready|New)\s*.*$", "", loc_m.group(1), flags=re.I).strip()
                    location = raw if len(raw) > 3 else area
                else:
                    location = area

                if not _match_ptype(title, property_type):
                    continue
                listings.append(Listing(
                    source="Dubizzle",
                    title=title[:120],
                    price_egp=price,
                    area_m2=area_val,
                    price_per_m2=None,
                    location=location,
                    bedrooms=bedrooms,
                    finishing=_detect_finishing(title),
                    floor=None,
                    compound=None,
                    url=full_url,
                    property_type=property_type,
                ))
            except (ValueError, TypeError, KeyError):
                continue

    return listings


# ─── Finishing & floor adjustment factors ────────────────────────────────────
# All relative to "fully_finished" = 1.0
FINISHING_FACTORS = {
    "furnished":      1.18,
    "fully_finished": 1.00,
    "semi_finished":  0.88,
    "core_shell":     0.78,
    None:             1.00,   # unknown → assume market average
}

FLOOR_FACTORS = {
    "ground":     0.95,
    "1-3":        1.00,
    "4-7":        1.03,
    "8-12":       1.06,
    "penthouse":  1.12,
    None:         1.00,
}


def normalize_price(price: int, area_m2: Optional[float],
                    src_finishing: Optional[str],
                    target_finishing: str) -> Optional[float]:
    """Adjust a comparable's price to be equivalent to target_finishing."""
    if not area_m2 or area_m2 <= 0:
        return None
    src_factor = FINISHING_FACTORS.get(src_finishing, 1.0)
    tgt_factor = FINISHING_FACTORS.get(target_finishing, 1.0)
    # price_per_m2 normalized to target finishing
    raw_ppm2 = price / area_m2
    normalized_ppm2 = raw_ppm2 * (tgt_factor / src_factor)
    return normalized_ppm2


# ─── Property Finder Egypt ────────────────────────────────────────────────────

PF_PTYPES = {
    "apartment":  "apartments",
    "penthouse":  "penthouse",
    "duplex":     "duplex",
    "i_villa":    "apartments",         # i-villa = apartment type on PF (ground-floor 2-floor+roof)
    "villa":      "villas",
    "townhouse":  "townhouses",
    "twin_house": "villas",
    "house":      "villas",
    "land":       "land",
}


def scrape_propertyfinder(area: str, property_type: str,
                          min_area: int = 0, max_area: int = 0,
                          compound: str = "",
                          pf_city: str = "cairo",
                          pf_area: str = "",
                          pages: int = 1) -> list[Listing]:
    ptype = PF_PTYPES.get(property_type, "apartments")
    base_url = f"https://www.propertyfinder.eg/en/buy/{pf_city}/{ptype}-for-sale{pf_area}.html"
    fallback_url = f"https://www.propertyfinder.eg/en/buy/{pf_city}/{ptype}-for-sale.html"

    compound_lower = compound.lower().strip()
    listings = []

    for page in range(1, pages + 1):
        url = base_url if page == 1 else f"{base_url}?page={page}"
        try:
            resp = _get(url)
            if resp.status_code == 404 and page == 1:
                resp = _get(fallback_url)
                if resp.status_code == 404:
                    resp = _get(f"{fallback_url}?page={page}" if page > 1 else fallback_url)
            if resp.status_code != 200:
                break
        except Exception as e:
            print(f"[PropertyFinder] request error: {e}")
            break

        soup = BeautifulSoup(resp.text, "lxml")
        cards = soup.select('article[data-testid="property-card"]')
        if not cards:
            break

        for card in cards:
            try:
                text = card.get_text(" ", strip=True)

                if compound_lower and compound_lower not in text.lower():
                    continue

                price_el = card.select_one('[data-testid="property-card-price"]')
                if not price_el:
                    continue
                price_text = re.sub(r"[^\d]", "", price_el.get_text())
                if not price_text:
                    continue
                price = int(price_text)
                if price <= 0:
                    continue

                am = re.search(r"([\d,]+)\s*sqm", text)
                area_val = float(am.group(1).replace(",", "")) if am else None

                if min_area > 0 and area_val and area_val < min_area:
                    continue
                if max_area > 0 and area_val and area_val > max_area:
                    continue

                pre_sqm = text.split("sqm")[0] if "sqm" in text else ""
                nums = re.findall(r"\b(\d+)\b", pre_sqm[-30:]) if pre_sqm else []
                bedrooms = int(nums[0]) if len(nums) >= 2 else None

                title_el = card.select_one("img[alt]")
                title = str(title_el["alt"]) if title_el else text[:80]

                link_el = card.select_one('a[data-testid="property-card-link"]')
                url_out = link_el["href"] if link_el else "https://www.propertyfinder.eg"

                # Extract compound from PF location data-testid elements
                loc_compound = None
                for el in card.select('[data-testid]'):
                    t = el.get_text(strip=True)
                    if ', 6 October' in t or ', New Cairo' in t or ', Sheikh Zayed' in t or ', Giza' in t or ', Cairo' in t:
                        loc_compound = t.split(',')[0].strip()
                        break

                loc_m = re.search(r"EGP\s+(.+?)\s+\d+\s+\d+\s+[\d,]+\s+sqm", text)
                if not loc_m:
                    loc_m = re.search(r"EGP\s+.+?\s+(.+?)\s+\d+\s+[\d,]+\s+sqm", text)
                location = loc_m.group(1).strip() if loc_m else area

                if not _match_ptype(title, property_type):
                    continue
                listings.append(Listing(
                    source="PropertyFinder",
                    title=title[:120],
                    price_egp=price,
                    area_m2=area_val,
                    price_per_m2=None,
                    location=location,
                    bedrooms=bedrooms,
                    finishing=_detect_finishing(title),
                    floor=None,
                    compound=loc_compound,
                    url=url_out,
                    property_type=property_type,
                ))
            except (ValueError, TypeError, KeyError):
                continue

    return listings


# ─── Analysis ─────────────────────────────────────────────────────────────────

def analyze_listings(listings: list[Listing],
                     target_finishing: str = "fully_finished",
                     target_floor: str = None,
                     target_area_m2: float = None) -> dict:
    if not listings:
        return {"error": "No listings found. Try a broader area, or remove the compound filter."}

    prices = sorted(l.price_egp for l in listings if l.price_egp > 0)

    # Build normalized price-per-m² list (comps adjusted to target finishing)
    norm_ppm2_list = []
    for l in listings:
        nppm2 = normalize_price(l.price_egp, l.area_m2, l.finishing, target_finishing)
        if nppm2 and 1000 < nppm2 < 1_000_000:
            norm_ppm2_list.append(nppm2)
    norm_ppm2_list.sort()

    raw_ppm2 = sorted(l.price_per_m2 for l in listings if l.price_per_m2 and l.price_per_m2 > 0)

    def pct(data, p):
        if not data:
            return None
        idx = max(0, int(len(data) * p / 100) - 1)
        return data[idx]

    def median(data):
        if not data:
            return None
        n = len(data)
        mid = n // 2
        return int((data[mid - 1] + data[mid]) / 2) if n % 2 == 0 else data[mid]

    med_price = median(prices)
    med_ppm2 = int(median(norm_ppm2_list)) if norm_ppm2_list else (int(median(raw_ppm2)) if raw_ppm2 else None)

    # Floor adjustment on top of finishing
    floor_factor = FLOOR_FACTORS.get(target_floor, 1.0)

    # Recommended listing range for seller:
    # Low end  = fair value (what the market will accept — don't list below this)
    # High end = fair value + 15% (leaves room to negotiate down without underselling)
    rec_ppm2_low  = int(med_ppm2 * 1.00 * floor_factor) if med_ppm2 else None
    rec_ppm2_high = int(med_ppm2 * 1.15 * floor_factor) if med_ppm2 else None
    rec_price_low  = int(rec_ppm2_low  * target_area_m2) if rec_ppm2_low  and target_area_m2 else None
    rec_price_high = int(rec_ppm2_high * target_area_m2) if rec_ppm2_high and target_area_m2 else None

    return {
        "count": len(listings),
        "price_min": prices[0] if prices else None,
        "price_max": prices[-1] if prices else None,
        "price_median": med_price,
        "price_p25": pct(prices, 25),
        "price_p75": pct(prices, 75),
        "price_p10": pct(prices, 10),
        "price_p90": pct(prices, 90),
        # Normalized price/m² (adjusted to target finishing)
        "norm_ppm2_median": med_ppm2,
        "norm_ppm2_p25": int(pct(norm_ppm2_list, 25)) if norm_ppm2_list else None,
        "norm_ppm2_p75": int(pct(norm_ppm2_list, 75)) if norm_ppm2_list else None,
        # Recommended listing range for seller (with floor adjustment)
        "rec_price_low": rec_price_low,
        "rec_price_high": rec_price_high,
        "rec_ppm2_low": rec_ppm2_low,
        "rec_ppm2_high": rec_ppm2_high,
        # Deal price (what it likely closes at)
        # Expected close = 90–100% of fair value (median ppm2 * area)
        "deal_price_low":  int(med_ppm2 * 0.90 * floor_factor * target_area_m2) if med_ppm2 and target_area_m2 else None,
        "deal_price_high": int(med_ppm2 * 1.00 * floor_factor * target_area_m2) if med_ppm2 and target_area_m2 else None,
        "sources": sorted({l.source for l in listings}),
        "listings_with_area": len(norm_ppm2_list),
        "floor_factor": floor_factor,
        "finishing_factor": FINISHING_FACTORS.get(target_finishing, 1.0),
    }


def detect_compound_from_text(text: str, location: str,
                              compounds: list[dict]) -> Optional[str]:
    """Match listing text+location against known compound dubizzle strings.

    Uses whole-word regex so 'salt' won't match 'default', 'abha' won't match
    'rehab', etc. Returns the label of the longest (most specific) match."""
    haystack = (text + " " + location).lower()
    best_label, best_len = None, 0
    for c in compounds:
        needle = c.get("dubizzle", "").lower().strip()
        if not needle or len(needle) <= best_len:
            continue
        # Require the needle to appear as a whole-word phrase
        pattern = r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])"
        if re.search(pattern, haystack):
            best_label = c["label"]
            best_len = len(needle)
    return best_label


def _trim_compound_outliers(listings: list[Listing]) -> list[Listing]:
    """Remove the most extreme price-per-m² outliers within a compound group.

    Keeps only listings whose EGP/m² sits inside [P10, P90] when n >= 8,
    or [P15, P85] when n >= 4. Smaller groups are returned unchanged."""
    valid = [l for l in listings if l.area_m2 and l.area_m2 > 0 and l.price_egp > 0]
    other = [l for l in listings if l not in valid]

    n = len(valid)
    if n < 4:
        return listings

    valid.sort(key=lambda l: l.price_egp / l.area_m2)
    pct = 0.10 if n >= 8 else 0.15
    cut = max(1, int(n * pct))
    trimmed = valid[cut: n - cut] if n - 2 * cut >= 2 else valid
    return trimmed + other


def build_compound_report(listings: list[Listing],
                          compounds: list[dict],
                          target_finishing: str = "fully_finished",
                          area_median_ppm2: Optional[float] = None) -> list[dict]:
    """Group listings by compound and compute tier-blended price benchmarks.

    Priority order for price estimation:
      1. Live market data from current scrape (if ≥5 listings with area)
      2. Historical DB snapshot for the compound  (persistent cross-scrape data)
      3. Territory median from DB                 (geo-adjusted baseline)
      4. Tier prior vs area median                (developer reputation factor)

    The blend weights shift automatically based on how much live data is present.
    """
    from collections import defaultdict
    from tier_data import COMPOUND_TIERS, TIER_MULTIPLIERS, TIER_LABELS, blend_weights
    from reference_prices import REFERENCE_PRICES as REF_PRICES
    try:
        from db import get_compound_ref, get_territory_ref
        from locations import COMPOUND_TERRITORY_MAP
        _db_available = True
    except Exception:
        _db_available = False

    known_labels = {c["label"] for c in compounds}

    # Aqarmap extracts compound from location breadcrumbs which are often street
    # names, not compound names. Wipe them and re-detect from text.
    for lst in listings:
        if lst.source == "Aqarmap":
            lst.compound = None

    # Tag every listing against our known compound list
    for lst in listings:
        lst.compound = detect_compound_from_text(lst.title, lst.location, compounds)

    by_compound: dict[str, list[Listing]] = defaultdict(list)
    for lst in listings:
        if lst.compound and lst.compound in known_labels:
            by_compound[lst.compound].append(lst)

    # Need the area-wide EGP/m² range for a sanity guard
    all_ppm2 = [
        l.price_egp / l.area_m2
        for l in listings
        if l.area_m2 and l.area_m2 > 0 and l.price_egp > 0
    ]
    all_ppm2.sort()
    if len(all_ppm2) >= 4:
        # Acceptable range: P5–P95 of area-wide distribution × 2 safety margin
        area_p5  = all_ppm2[max(0, int(len(all_ppm2) * 0.05))]
        area_p95 = all_ppm2[min(len(all_ppm2)-1, int(len(all_ppm2) * 0.95))]
        ppm2_floor = area_p5 * 0.5
        ppm2_cap   = area_p95 * 2.0
    else:
        ppm2_floor, ppm2_cap = 0, float("inf")

    # Build market-data rows for compounds that have listings
    market_rows = {}
    for label, comp_listings in by_compound.items():
        comp_listings = [
            l for l in comp_listings
            if not (l.area_m2 and l.price_egp)
            or ppm2_floor <= (l.price_egp / l.area_m2) <= ppm2_cap
        ]
        comp_listings = _trim_compound_outliers(comp_listings)
        stats = analyze_listings(comp_listings, target_finishing, None, None)
        if stats.get("error"):
            continue
        med = stats.get("norm_ppm2_median")
        if not med:
            continue
        market_rows[label] = {
            "count":              stats["count"],
            "listings_with_area": stats.get("listings_with_area", 0),
            "market_ppm2":        med,
            "p25_ppm2":           stats.get("norm_ppm2_p25"),
            "p75_ppm2":           stats.get("norm_ppm2_p75"),
            "sources":            stats.get("sources", []),
        }

    # Pre-compute territory average tier multiplier (for tier-relative territory scaling)
    # territory → weighted avg of TIER_MULTIPLIERS for all compounds in that territory
    from collections import defaultdict as _dd
    _ter_mults: dict[str, list[float]] = _dd(list)
    for _cd in compounds:
        _t = _cd.get("territory")
        if _t:
            _tm = TIER_MULTIPLIERS.get(COMPOUND_TIERS.get(_cd["label"], {}).get("tier", 3), 0.85)
            _ter_mults[_t].append(_tm)
    territory_avg_mult: dict[str, float] = {
        t: sum(v) / len(v) for t, v in _ter_mults.items()
    }

    # Build final results, blending market data with tier prior for every known compound
    results = []
    for comp_def in compounds:
        label     = comp_def["label"]
        territory = comp_def.get("territory")
        tier_info = COMPOUND_TIERS.get(label, {})
        tier      = tier_info.get("tier", 3)
        developer = tier_info.get("developer", "")
        tier_mult = TIER_MULTIPLIERS[tier]

        market = market_rows.get(label)
        n      = market["listings_with_area"] if market else 0
        mw, tw = blend_weights(n)

        # ── Priority 1: DB compound (area-specific, avoids cross-area name collision) ──
        db_compound_ppm2 = None
        if _db_available:
            ter_info_map = COMPOUND_TERRITORY_MAP.get(label)
            area_id_for_comp = ter_info_map[0] if ter_info_map else None
            if area_id_for_comp:
                db_comp = get_compound_ref(label, area_id_for_comp)
                if db_comp and db_comp.get("median_ppm2") and db_comp["sample_n"] >= 5:
                    db_compound_ppm2 = db_comp["median_ppm2"]

        # ── Priority 2: territory median from DB, scaled by this compound's tier ─────
        db_territory_ppm2 = None
        if _db_available and territory and not db_compound_ppm2:
            ter_info_map = COMPOUND_TERRITORY_MAP.get(label)
            if ter_info_map:
                db_ter = get_territory_ref(ter_info_map[0], territory)
                if db_ter and db_ter.get("median_ppm2") and db_ter["sample_n"] >= 10:
                    ter_avg = territory_avg_mult.get(territory, tier_mult)
                    scale = tier_mult / ter_avg if ter_avg else 1.0
                    db_territory_ppm2 = int(db_ter["median_ppm2"] * scale)

        # ── Priority 3: researched reference price (knowledge-based, per compound) ────
        ref = REF_PRICES.get(label)
        ref_ppm2 = ref["median"] if ref else None

        # ── Priority 4: tier × area median (last resort) ─────────────────────────────
        tier_ppm2 = int(area_median_ppm2 * tier_mult) if area_median_ppm2 else None

        # Best static prior for blending when live data is sparse
        best_prior = db_compound_ppm2 or db_territory_ppm2 or ref_ppm2 or tier_ppm2

        if market and market["market_ppm2"]:
            raw_market = market["market_ppm2"]
            if best_prior:
                blended = int(mw * raw_market + tw * best_prior)
            else:
                blended = raw_market
            spread_factor = 0.15 + 0.05 * (1 - mw)
            p25 = market.get("p25_ppm2") or int(blended * (1 - spread_factor))
            p75 = market.get("p75_ppm2") or int(blended * (1 + spread_factor))
            sources = market["sources"]
            basis   = "market" if mw >= 0.75 else "blended"
        elif db_compound_ppm2:
            ter_info_map = COMPOUND_TERRITORY_MAP.get(label)
            area_id_for_comp = ter_info_map[0] if ter_info_map else None
            db_ref = get_compound_ref(label, area_id_for_comp) if (area_id_for_comp and _db_available) else None
            blended = int(db_compound_ppm2)
            p25 = int(db_ref["p25_ppm2"]) if db_ref and db_ref.get("p25_ppm2") else int(db_compound_ppm2 * 0.85)
            p75 = int(db_ref["p75_ppm2"]) if db_ref and db_ref.get("p75_ppm2") else int(db_compound_ppm2 * 1.15)
            sources = []
            basis   = "db"
        elif db_territory_ppm2:
            blended = db_territory_ppm2
            p25     = int(db_territory_ppm2 * 0.87)
            p75     = int(db_territory_ppm2 * 1.13)
            sources = []
            basis   = "territory"
        elif ref_ppm2:
            # No live or DB data — use researched reference price
            blended = ref_ppm2
            p25     = ref["p25"]
            p75     = ref["p75"]
            sources = []
            basis   = "reference"
        elif tier_ppm2:
            blended = tier_ppm2
            p25     = int(tier_ppm2 * 0.85)
            p75     = int(tier_ppm2 * 1.15)
            sources = []
            basis   = "estimated"
        else:
            continue

        rec_low  = int(blended * 1.00)
        rec_high = int(blended * 1.15)

        conf = "high" if n >= 10 else "medium" if n >= 5 else "low" if n >= 2 else "estimated"

        results.append({
            "compound":           label,
            "developer":          developer,
            "tier":               tier,
            "tier_label":         TIER_LABELS[tier],
            "basis":              basis,
            "count":              market["count"] if market else 0,
            "listings_with_area": n,
            "confidence":         conf,
            "median_ppm2":        blended,
            "p25_ppm2":           p25,
            "p75_ppm2":           p75,
            "rec_ppm2_low":       rec_low,
            "rec_ppm2_high":      rec_high,
            "price_min":          market.get("price_min") if market else None,
            "price_max":          market.get("price_max") if market else None,
            "sources":            sources,
        })

    results.sort(key=lambda x: x["median_ppm2"], reverse=True)
    return results


def buyer_verdict(asking_price: int, area_m2: float,
                  target_finishing: str, target_floor: str,
                  stats: dict) -> dict:
    """Score an asking price against market comps."""
    if not stats.get("norm_ppm2_median") or not area_m2:
        return {"verdict": "unknown", "score": None}

    floor_factor = FLOOR_FACTORS.get(target_floor, 1.0)
    finishing_factor = FINISHING_FACTORS.get(target_finishing, 1.0)

    # Adjust asking price to normalized equivalent (remove floor/finishing premium from asking)
    asking_ppm2 = asking_price / area_m2
    # Normalize asking price to fully_finished equivalent at ground-floor-neutral
    normalized_asking_ppm2 = asking_ppm2 / finishing_factor / floor_factor

    med = stats["norm_ppm2_median"]
    p25 = stats.get("norm_ppm2_p25") or med * 0.85
    p75 = stats.get("norm_ppm2_p75") or med * 1.15

    # Position in market
    ratio = normalized_asking_ppm2 / med  # 1.0 = exactly median

    if ratio <= 0.80:
        verdict = "excellent_deal"
        label = "Excellent Deal"
        color = "green"
        detail = f"Asking price is {int((1-ratio)*100)}% below market median — strong buy signal."
    elif ratio <= 0.92:
        verdict = "good_price"
        label = "Good Price"
        color = "green"
        detail = f"Asking price is {int((1-ratio)*100)}% below market median — fair value with upside."
    elif ratio <= 1.05:
        verdict = "fair_price"
        label = "Fair Market Price"
        color = "yellow"
        detail = "Asking price is in line with comparable properties."
    elif ratio <= 1.18:
        verdict = "above_market"
        label = "Above Market"
        color = "orange"
        detail = f"Asking price is {int((ratio-1)*100)}% above market median — room to negotiate."
    else:
        verdict = "overpriced"
        label = "Overpriced"
        color = "red"
        detail = f"Asking price is {int((ratio-1)*100)}% above market — significantly overvalued."

    # What the property is actually worth
    fair_low = int(p25 * finishing_factor * floor_factor * area_m2)
    fair_high = int(p75 * finishing_factor * floor_factor * area_m2)
    fair_median = int(med * finishing_factor * floor_factor * area_m2)

    # How much to negotiate
    negotiate_to = int(fair_median * 0.92) if ratio > 1.05 else None

    return {
        "verdict": verdict,
        "label": label,
        "color": color,
        "detail": detail,
        "ratio": round(ratio, 3),
        "pct_vs_median": round((ratio - 1) * 100, 1),
        "fair_value_low": fair_low,
        "fair_value_high": fair_high,
        "fair_value_median": fair_median,
        "negotiate_to": negotiate_to,
        "asking_ppm2": int(asking_ppm2),
        "market_ppm2": int(med * finishing_factor * floor_factor),
    }
