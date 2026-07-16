"""
Listing importer — scrapes external marketplace URLs and returns
a normalized dict that pre-fills the SuqMasr post form.

Supported platforms (with specific parsers):
  olx.com.eg, hatla2ee.com, dubizzle.com.eg,
  aqarmap.com, propertyfinder.eg

All others fall back to JSON-LD / Open Graph extraction.
"""

import json
import re
import urllib.parse
from typing import Optional

import requests
from bs4 import BeautifulSoup

# ── HTTP session ──────────────────────────────────────────────────────────────

_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

_TIMEOUT = 12


def _fetch(url: str) -> Optional[BeautifulSoup]:
    try:
        r = requests.get(url, headers=_HEADERS, timeout=_TIMEOUT, allow_redirects=True)
        r.raise_for_status()
        return BeautifulSoup(r.text, "lxml")
    except Exception as e:
        raise ValueError(f"Could not fetch URL: {e}") from e


# ── Utility helpers ───────────────────────────────────────────────────────────

def _int(s) -> Optional[int]:
    if s is None:
        return None
    cleaned = re.sub(r"[^\d]", "", str(s))
    return int(cleaned) if cleaned else None


def _text(el) -> str:
    return el.get_text(strip=True) if el else ""


def _meta(soup, *names) -> Optional[str]:
    for name in names:
        tag = soup.find("meta", attrs={"property": name}) or soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None


def _jsonld(soup) -> list[dict]:
    out = []
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or "")
            if isinstance(data, list):
                out.extend(data)
            else:
                out.append(data)
        except Exception:
            pass
    return out


def _detect_platform(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
    if "olx.com.eg" in host:
        return "olx"
    if "hatla2ee.com" in host:
        return "hatla2ee"
    if "dubizzle.com.eg" in host or "dubizzle.com" in host:
        return "dubizzle"
    if "aqarmap.com" in host:
        return "aqarmap"
    if "propertyfinder.eg" in host:
        return "propertyfinder"
    if "contactcars.com" in host:
        return "contactcars"
    return "generic"


def _guess_type(title: str, desc: str) -> str:
    text = (title + " " + desc).lower()
    car_kw = ["car", "سيارة", "كار", "vehicle", "auto", "km", "كيلو", "مانيوال", "اوتوماتيك",
               "toyota", "honda", "kia", "hyundai", "nissan", "bmw", "mercedes", "vw", "volkswagen"]
    prop_kw = ["apartment", "villa", "شقة", "فيلا", "عقار", "property", "flat",
                "bedroom", "bath", "m²", "sqm", "sqft", "compound", "floor", "duplex"]
    car_score  = sum(1 for k in car_kw  if k in text)
    prop_score = sum(1 for k in prop_kw if k in text)
    return "car" if car_score >= prop_score else "property"


def _clean_price(s: str) -> Optional[int]:
    if not s:
        return None
    # remove currency symbols and commas
    cleaned = re.sub(r"[^\d]", "", str(s))
    v = int(cleaned) if cleaned else None
    # Some sites show price in thousands — heuristic: if v < 10000 assume K
    if v and v < 5000:
        v *= 1000
    return v


# ── Platform-specific parsers ─────────────────────────────────────────────────

def _parse_olx(soup: BeautifulSoup, url: str) -> dict:
    """OLX Egypt — data is in a window.__APP_CONFIG__ or JSON blobs in <script>."""
    result: dict = {"source_url": url, "source_platform": "OLX Egypt"}

    # Try JSON in script tags
    for tag in soup.find_all("script"):
        txt = tag.string or ""
        # OLX embeds listing data as window.__APP_CONFIG__ or similar
        if "adParams" in txt or '"price"' in txt:
            # Try to extract JSON-LD first
            break

    # Title
    title_el = soup.find("h1") or soup.find("h4", class_=re.compile(r"title", re.I))
    result["title"] = _text(title_el)

    # Price — OLX shows price in a <strong> near a label
    price_el = (soup.find("strong", class_=re.compile(r"price", re.I)) or
                soup.find("div", class_=re.compile(r"price", re.I)) or
                soup.find("h3", class_=re.compile(r"price", re.I)))
    result["asking_price"] = _clean_price(_text(price_el))

    # Description
    desc_el = soup.find("div", class_=re.compile(r"description|text-body", re.I))
    result["description"] = _text(desc_el)

    # Photos — OLX lazy-loads, grab data-src or src
    imgs = []
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("src") or ""
        if "images.olx" in src or "staticfiles" in src:
            imgs.append(src)
    result["photo_urls"] = imgs[:10]

    # Location
    loc_el = soup.find("span", class_=re.compile(r"location|breadcrumb", re.I))
    result["city"] = _text(loc_el)

    return result


def _parse_hatla2ee(soup: BeautifulSoup, url: str) -> dict:
    """Hatla2ee — cars marketplace."""
    result: dict = {"source_url": url, "source_platform": "Hatla2ee", "type": "car"}

    # Title
    result["title"] = _text(soup.find("h1"))

    # Price
    price_el = (soup.find("div", class_=re.compile(r"price", re.I)) or
                soup.find("span", class_=re.compile(r"price", re.I)))
    result["asking_price"] = _clean_price(_text(price_el))

    # Description
    desc_el = soup.find("div", class_=re.compile(r"description|details", re.I))
    result["description"] = _text(desc_el)

    # Specs table — hatla2ee has a table of car details
    specs = {}
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 2:
            k = _text(cells[0]).lower().strip(":")
            v = _text(cells[1])
            specs[k] = v

    # Normalize common hatla2ee keys
    def _sp(*keys):
        for k in keys:
            if k in specs:
                return specs[k]
        return None

    result["make"]         = _sp("brand", "make", "الماركة")
    result["model"]        = _sp("model", "الموديل")
    result["year"]         = _int(_sp("year", "السنة", "model year"))
    result["mileage_km"]   = _int(_sp("mileage", "km", "المسافة"))
    result["fuel"]         = _sp("fuel", "fuel type", "وقود")
    result["transmission"] = _sp("transmission", "gear", "ناقل الحركة")
    result["condition"]    = _sp("condition", "الحالة")
    result["color"]        = _sp("color", "اللون")

    # Photos
    imgs = []
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("src") or ""
        if "hatla2ee" in src and not "logo" in src.lower():
            imgs.append(src)
    result["photo_urls"] = imgs[:10]

    return result


def _parse_dubizzle(soup: BeautifulSoup, url: str) -> dict:
    """Dubizzle Egypt — cars + properties."""
    result: dict = {"source_url": url, "source_platform": "Dubizzle"}

    result["title"]       = _text(soup.find("h1"))
    result["description"] = _meta(soup, "og:description") or ""

    # Price
    price_el = soup.find("span", class_=re.compile(r"price", re.I))
    result["asking_price"] = _clean_price(_text(price_el))

    # Photos from OG
    og_img = _meta(soup, "og:image")
    result["photo_urls"] = [og_img] if og_img else []

    # Details list
    specs = {}
    for li in soup.find_all("li"):
        text = _text(li)
        if ":" in text:
            k, _, v = text.partition(":")
            specs[k.strip().lower()] = v.strip()

    result["make"]       = specs.get("make") or specs.get("brand")
    result["model"]      = specs.get("model")
    result["year"]       = _int(specs.get("year"))
    result["mileage_km"] = _int(specs.get("kilometers") or specs.get("mileage"))
    result["fuel"]       = specs.get("fuel type")
    result["transmission"] = specs.get("transmission")

    return result


def _parse_aqarmap(soup: BeautifulSoup, url: str) -> dict:
    """Aqarmap.com — Egyptian real estate."""
    result: dict = {"source_url": url, "source_platform": "Aqarmap", "type": "property"}

    result["title"]       = _text(soup.find("h1"))
    result["description"] = _text(soup.find("div", class_=re.compile(r"description|details", re.I)))

    price_el = soup.find("span", class_=re.compile(r"price", re.I))
    result["asking_price"] = _clean_price(_text(price_el))

    # Specs
    specs = {}
    for el in soup.find_all(class_=re.compile(r"spec|feature|detail", re.I)):
        text = _text(el)
        if ":" in text:
            k, _, v = text.partition(":")
            specs[k.strip().lower()] = v.strip()

    result["size_m2"]   = _int(specs.get("area") or specs.get("m²") or specs.get("size"))
    result["bedrooms"]  = _int(specs.get("bedrooms") or specs.get("rooms"))
    result["bathrooms"] = _int(specs.get("bathrooms"))
    result["finishing"] = specs.get("finishing")

    og_img = _meta(soup, "og:image")
    result["photo_urls"] = [og_img] if og_img else []

    return result


def _parse_propertyfinder(soup: BeautifulSoup, url: str) -> dict:
    """PropertyFinder.eg — real estate."""
    result: dict = {"source_url": url, "source_platform": "PropertyFinder", "type": "property"}

    result["title"] = _text(soup.find("h1"))
    result["description"] = _meta(soup, "og:description") or ""

    # Price from JSON-LD Product
    for ld in _jsonld(soup):
        if ld.get("@type") in ("Product", "Offer", "RealEstateListing"):
            offer = ld.get("offers", ld)
            price = offer.get("price") or ld.get("price")
            if price:
                result["asking_price"] = _clean_price(price)
            break

    # Bedrooms / area from page text
    text = soup.get_text()
    m = re.search(r"(\d+)\s*bed", text, re.I)
    if m:
        result["bedrooms"] = int(m.group(1))
    m = re.search(r"(\d[\d,]*)\s*(?:sq\.?\s*m|sqm|m²)", text, re.I)
    if m:
        result["size_m2"] = _int(m.group(1))

    og_img = _meta(soup, "og:image")
    result["photo_urls"] = [og_img] if og_img else []

    return result


# ── Generic JSON-LD + OG fallback ─────────────────────────────────────────────

def _parse_generic(soup: BeautifulSoup, url: str) -> dict:
    result: dict = {"source_url": url, "source_platform": "Unknown"}

    # JSON-LD
    for ld in _jsonld(soup):
        typ = ld.get("@type", "")
        if isinstance(typ, list):
            typ = typ[0] if typ else ""
        if typ in ("Product", "Car", "Vehicle", "Offer",
                   "RealEstateListing", "SingleFamilyResidence",
                   "Apartment", "House"):
            result["title"]       = ld.get("name") or ld.get("headline", "")
            result["description"] = ld.get("description", "")
            offers = ld.get("offers")
            if isinstance(offers, dict):
                result["asking_price"] = _clean_price(offers.get("price"))
            elif isinstance(offers, list) and offers:
                result["asking_price"] = _clean_price(offers[0].get("price"))
            else:
                result["asking_price"] = _clean_price(ld.get("price"))
            imgs = ld.get("image", [])
            if isinstance(imgs, str):
                imgs = [imgs]
            elif isinstance(imgs, dict):
                imgs = [imgs.get("url", "")]
            result["photo_urls"] = [i for i in imgs if i][:10]
            # Vehicle specifics
            result["make"]         = ld.get("brand", {}).get("name") if isinstance(ld.get("brand"), dict) else ld.get("brand")
            result["model"]        = ld.get("model")
            result["year"]         = _int(ld.get("vehicleModelDate") or ld.get("productionDate"))
            result["mileage_km"]   = _int((ld.get("mileageFromOdometer") or {}).get("value") if isinstance(ld.get("mileageFromOdometer"), dict) else None)
            result["fuel"]         = ld.get("fuelType")
            result["transmission"] = ld.get("vehicleTransmission")
            break

    # Fill gaps from OG / meta
    if not result.get("title"):
        result["title"] = _meta(soup, "og:title", "twitter:title") or _text(soup.find("h1"))
    if not result.get("description"):
        result["description"] = _meta(soup, "og:description", "description", "twitter:description") or ""
    if not result.get("photo_urls"):
        og_img = _meta(soup, "og:image", "twitter:image")
        result["photo_urls"] = [og_img] if og_img else []
    if not result.get("asking_price"):
        # Try meta price tags
        price_str = _meta(soup, "product:price:amount", "og:price:amount")
        result["asking_price"] = _clean_price(price_str)

    # Extract price from plain text if still missing
    if not result.get("asking_price"):
        text = soup.get_text()
        m = re.search(r"(?:EGP|ج\.?م\.?|جنيه)\s*[\d,]+", text, re.I)
        if m:
            result["asking_price"] = _clean_price(m.group())

    return result


# ── Main entry point ──────────────────────────────────────────────────────────

def import_listing(url: str) -> dict:
    """
    Fetch and parse an external listing URL.
    Returns a normalized dict with these possible keys:
        title, description, asking_price, type (car|property),
        city, photo_urls,
        [car]  make, model, year, mileage_km, fuel, transmission, condition, color
        [prop] size_m2, bedrooms, bathrooms, finishing
        source_platform, source_url
    """
    url = url.strip()
    if not url.startswith("http"):
        url = "https://" + url

    platform = _detect_platform(url)
    soup     = _fetch(url)

    parsers = {
        "olx":            _parse_olx,
        "hatla2ee":       _parse_hatla2ee,
        "dubizzle":       _parse_dubizzle,
        "aqarmap":        _parse_aqarmap,
        "propertyfinder": _parse_propertyfinder,
    }

    if platform in parsers:
        result = parsers[platform](soup, url)
        # Fill any gaps with generic parser
        generic = _parse_generic(soup, url)
        for k, v in generic.items():
            if k not in result or not result[k]:
                result[k] = v
    else:
        result = _parse_generic(soup, url)

    # Guess type if not set
    if not result.get("type"):
        result["type"] = _guess_type(result.get("title", ""), result.get("description", ""))

    # Clean up
    result = {k: v for k, v in result.items() if v is not None and v != "" and v != []}

    return result
