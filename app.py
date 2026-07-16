"""
Egypt Marketplace — Flask app.
Port 5055.
"""

import os
import uuid
from functools import wraps
from pathlib import Path
from flask import (
    Flask, render_template, request, jsonify,
    redirect, url_for, session, flash,
)
from werkzeug.utils import secure_filename

from db import (
    create_listing, get_listing, get_listing_full, list_listings,
    save_car_details, save_property_details, save_photos, save_assessment,
    save_auction, create_offer, place_bid, respond_offer,
    update_listing_status, get_stats,
    buy_now, lower_reserve, end_auction_early, cancel_auction,
    toggle_watchlist, get_watchlist_count, is_watching, get_user_watchlist,
    check_and_close_auction,
    create_user, authenticate_user, get_user,
    list_user_listings, list_user_offers,
)
from pricing.cars import (
    get_car_market_price, score_car_asking, CAR_MAKES, get_models_for_make,
)
from pricing.locations import CITIES, AREAS, COMPOUNDS

# Real estate price assessment (reuse from old project)
import sys
sys.path.insert(0, str(Path(__file__).parent / "pricing"))
from reference_prices import REFERENCE_PRICES, AREA_REFERENCE_PRICES
from tier_data import TIER_MULTIPLIERS, TIER_LABELS
from locations import COMPOUND_TERRITORY_MAP, TERRITORY_LABELS

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)


# ── Auth helpers ──────────────────────────────────────────────────────────────

def current_user():
    uid = session.get("user_id")
    return get_user(uid) if uid else None


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("user_id"):
            return redirect(url_for("login", next=request.path))
        return f(*args, **kwargs)
    return decorated

# ── Cloudinary (Vercel) vs local uploads ─────────────────────────────────────

_CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")
if _CLOUDINARY_URL:
    import cloudinary
    import cloudinary.uploader
    cloudinary.config_from_url(_CLOUDINARY_URL)
    USE_CLOUDINARY = True
else:
    USE_CLOUDINARY = False


# On Vercel the project root is read-only; use /tmp for local storage
_ON_VERCEL     = bool(os.environ.get("VERCEL"))
_DEFAULT_UPLOAD = Path("/tmp/uploads") if _ON_VERCEL else Path(__file__).parent / "static" / "uploads"
UPLOAD_FOLDER  = Path(os.environ.get("UPLOAD_FOLDER", _DEFAULT_UPLOAD))
try:
    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
except OSError:
    pass


def photo_url_filter(value):
    """Jinja2 filter: return Cloudinary URL as-is, or /uploads/<filename> for local files."""
    if not value:
        return ""
    if str(value).startswith("http"):
        return value
    return url_for("serve_upload", filename=value)


app.jinja_env.filters["photo_url"] = photo_url_filter


@app.context_processor
def inject_user():
    return {"current_user": current_user()}
ALLOWED_EXT  = {"jpg", "jpeg", "png", "webp", "heic"}
MAX_PHOTOS   = 12


# ── Helpers ───────────────────────────────────────────────────────────────────

def fmt_egp(n):
    if n is None:
        return "—"
    if n >= 1_000_000:
        return f"EGP {n/1_000_000:.2f}M"
    if n >= 1_000:
        return f"EGP {n/1_000:.0f}K"
    return f"EGP {n:,}"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


def save_upload(file) -> str | None:
    if not file or not allowed_file(file.filename):
        return None
    if USE_CLOUDINARY:
        result = cloudinary.uploader.upload(file, folder="suqmasr", resource_type="image")
        return result["secure_url"]
    ext = file.filename.rsplit(".", 1)[1].lower()
    fname = f"{uuid.uuid4().hex}.{ext}"
    file.save(UPLOAD_FOLDER / fname)
    return fname


# ── Property price assessment (mirrors old app logic) ────────────────────────

def _get_db_refs():
    try:
        # Use the old project's DB if available
        import sqlite3
        old_db = Path(__file__).parent.parent / "egypt-realestate-pricer" / "prices.db"
        if not old_db.exists():
            return {}, {}
        conn = sqlite3.connect(old_db)
        conn.row_factory = sqlite3.Row
        comps = conn.execute(
            "SELECT compound, area_id, median_ppm2, p25_ppm2, p75_ppm2, sample_n "
            "FROM price_snapshots WHERE scope='compound' AND sample_n >= 2"
        ).fetchall()
        areas = conn.execute(
            "SELECT area_id, median_ppm2, p25_ppm2, p75_ppm2 "
            "FROM price_snapshots WHERE scope='area'"
        ).fetchall()
        comp_map = {(r["area_id"], r["compound"]): dict(r) for r in comps}
        area_map = {r["area_id"]: dict(r) for r in areas}
        conn.close()
        return comp_map, area_map
    except Exception:
        return {}, {}


FINISHING_FACTORS = {
    "furnished": 1.18, "fully_finished": 1.00,
    "semi_finished": 0.88, "core_shell": 0.78,
}

FLOOR_FACTORS = {
    "ground": 0.95, "1-3": 1.00, "4-7": 1.03,
    "8-12": 1.06, "penthouse": 1.12,
}


def assess_property_price(area_id, compound, size_m2, finishing, floor):
    """Return market_price, market_ppm2, basis, note."""
    ff = FINISHING_FACTORS.get(finishing, 1.0)
    fl = FLOOR_FACTORS.get(floor, 1.0)

    comp_map, area_map = _get_db_refs()

    median_ppm2 = None
    basis = None
    note  = ""

    # 1. DB compound
    if compound and area_id:
        db = comp_map.get((area_id, compound))
        if db and db.get("sample_n", 0) >= 2:
            median_ppm2 = db["median_ppm2"]
            basis = "db"
            note  = f"Based on {db['sample_n']} recent listings in {compound}"

    # 2. Reference prices
    if median_ppm2 is None and compound:
        ref = AREA_REFERENCE_PRICES.get((area_id, compound)) or REFERENCE_PRICES.get(compound)
        if ref:
            median_ppm2 = ref["median"]
            basis = "reference"
            note  = "Based on researched reference price (Q1 2025)"

    # 3. Area median
    if median_ppm2 is None and area_id:
        db_area = area_map.get(area_id)
        if db_area:
            median_ppm2 = db_area["median_ppm2"]
            basis = "area"
            note  = "Based on area-wide median"

    if median_ppm2 is None or not size_m2:
        return None

    adj_ppm2    = int(median_ppm2 * ff * fl)
    market_price = int(adj_ppm2 * size_m2)
    return {
        "market_ppm2":  adj_ppm2,
        "market_price": market_price,
        "basis":        basis,
        "note":         note,
    }


def score_property_asking(asking_price, market_price):
    ratio = asking_price / market_price
    if ratio <= 0.82:
        verdict, label = "deal",       "Great Deal"
    elif ratio <= 0.94:
        verdict, label = "fair",       "Good Price"
    elif ratio <= 1.06:
        verdict, label = "fair",       "Fair Market Price"
    elif ratio <= 1.18:
        verdict, label = "above",      "Above Market"
    else:
        verdict, label = "overpriced", "Overpriced"
    return {
        "verdict":       verdict,
        "label":         label,
        "pct_vs_market": round((ratio - 1) * 100, 1),
    }


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/uploads/<path:filename>")
def serve_upload(filename):
    from flask import send_from_directory
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/")
def index():
    type_f  = request.args.get("type")
    city_f  = request.args.get("city")
    mode_f  = request.args.get("mode")
    min_p   = request.args.get("min_price", type=int)
    max_p   = request.args.get("max_price", type=int)
    listings = list_listings(type_f, city_f, min_p, max_p, mode_f)
    stats    = get_stats()
    cities   = [c["label"] for city_areas in AREAS.values() for c in city_areas]
    all_cities = sorted(set(
        c["city"] if "city" in c else c.get("label", "")
        for city_list in AREAS.values() for c in city_list
    ))
    return render_template("index.html",
        listings=listings, stats=stats,
        type_filter=type_f, city_filter=city_f,
        mode_filter=mode_f,
        fmt_egp=fmt_egp,
    )


@app.route("/post", methods=["GET"])
def post_form():
    return render_template("post.html",
        car_makes=CAR_MAKES,
        cities_data=CITIES,
        areas_data=AREAS,
        compounds_data=COMPOUNDS,
    )


@app.route("/post", methods=["POST"])
def post_submit():
    f = request.form
    listing_type = f.get("listing_type")   # 'car' | 'property'
    mode         = f.get("mode")           # 'offer' | 'auction'

    # ── Base listing ──────────────────────────────────────────────────────
    u = current_user()
    lid, token = create_listing({
        "type":         listing_type,
        "mode":         mode,
        "title":        f.get("title", "").strip(),
        "description":  f.get("description", "").strip(),
        "asking_price": int(f.get("asking_price") or 0),
        "seller_name":  u["name"] if u else f.get("seller_name", "").strip(),
        "seller_phone": u["phone"] if u else f.get("seller_phone", "").strip(),
        "city":         f.get("city", "").strip(),
        "expires_at":   None,
        "user_id":      u["id"] if u else None,
    })

    # ── Photos ────────────────────────────────────────────────────────────
    photos = request.files.getlist("photos")
    fnames = []
    for ph in photos[:MAX_PHOTOS]:
        fn = save_upload(ph)
        if fn:
            fnames.append(fn)
    if fnames:
        save_photos(lid, fnames)

    # ── Details + price assessment ────────────────────────────────────────
    if listing_type == "car":
        make  = f.get("make", "")
        model = f.get("model", "")
        year  = int(f.get("year") or 0)
        mileage = int(f.get("mileage_km") or 0)
        condition = f.get("condition", "good")

        save_car_details(lid, {
            "make": make, "model": model, "year": year,
            "mileage_km": mileage, "fuel": f.get("fuel"),
            "transmission": f.get("transmission"),
            "condition": condition, "color": f.get("color"),
            "body_type": f.get("body_type"),
        })

        ref = get_car_market_price(make, model, year, mileage, condition)
        if ref:
            asking = int(f.get("asking_price") or 0)
            score  = score_car_asking(asking, ref["market_price"])
            save_assessment(lid, {
                "market_price":  ref["market_price"],
                "market_ppm2":   None,
                "verdict":       score["verdict"],
                "pct_vs_market": score["pct_vs_market"],
                "basis":         ref["basis"],
                "note": f"Market estimate for {year} {make} {model} ({condition} condition, {mileage:,} km)",
            })

    else:  # property
        area_id   = f.get("area_id", "")
        area_label = f.get("area_label", "")
        compound  = f.get("compound", "")
        size_m2   = float(f.get("size_m2") or 0) or None
        finishing = f.get("finishing", "fully_finished")
        floor_val = f.get("floor") or None

        save_property_details(lid, {
            "area_id": area_id, "area_label": area_label,
            "compound": compound,
            "property_type": f.get("property_type"),
            "size_m2": size_m2,
            "bedrooms": int(f.get("bedrooms") or 0) or None,
            "bathrooms": int(f.get("bathrooms") or 0) or None,
            "finishing": finishing,
            "floor": floor_val,
            "furnished": 1 if f.get("furnished") else 0,
        })

        ref = assess_property_price(area_id, compound, size_m2, finishing, floor_val)
        if ref:
            asking = int(f.get("asking_price") or 0)
            score  = score_property_asking(asking, ref["market_price"])
            save_assessment(lid, {
                "market_price":  ref["market_price"],
                "market_ppm2":   ref["market_ppm2"],
                "verdict":       score["verdict"],
                "pct_vs_market": score["pct_vs_market"],
                "basis":         ref["basis"],
                "note":          ref["note"],
            })

    # ── Auction config ────────────────────────────────────────────────────
    if mode == "auction":
        save_auction(lid, {
            "start_price":      int(f.get("start_price") or f.get("asking_price") or 0),
            "reserve_price":    int(f.get("reserve_price") or 0) or None,
            "buy_now_price":    int(f.get("buy_now_price") or 0) or None,
            "min_increment":    int(f.get("min_increment") or 5000),
            "auto_extend_mins": int(f.get("auto_extend_mins") or 5),
            "end_at":           f.get("auction_end") or None,
        })

    return redirect(url_for("listing_manage", lid=lid, token=token))


@app.route("/listing/<lid>")
def listing_detail(lid):
    listing = get_listing_full(lid)
    if not listing:
        return render_template("404.html"), 404
    # Lazily close expired auctions
    if listing["mode"] == "auction" and listing.get("auction"):
        updated_auc = check_and_close_auction(lid)
        if updated_auc:
            listing["auction"] = updated_auc
    if listing["status"] not in ("active", "sold") and listing["mode"] != "auction":
        return render_template("404.html"), 404
    u = current_user()
    watching = is_watching(u["id"], lid) if u else False
    watch_count = get_watchlist_count(lid)
    # Is logged-in user the current high bidder?
    is_winning = (
        u and listing.get("auction") and
        listing["auction"].get("current_bidder_id") == u["id"]
    )
    return render_template("listing.html", listing=listing, fmt_egp=fmt_egp,
                           watching=watching, watch_count=watch_count,
                           is_winning=is_winning)


@app.route("/listing/<lid>/manage")
def listing_manage(lid):
    token = request.args.get("token", "")
    listing = get_listing_full(lid)
    u = current_user()
    # Allow access via manage token OR if the logged-in user owns the listing
    owner = (u and listing and listing.get("user_id") == u["id"])
    if not listing or (listing["manage_token"] != token and not owner):
        return render_template("404.html"), 404
    watch_count = get_watchlist_count(lid)
    offers = listing.get("offers", [])
    return render_template("manage.html", listing=listing, token=token,
                           watch_count=watch_count, offers=offers, fmt_egp=fmt_egp)


@app.route("/listing/<lid>/offer", methods=["POST"])
def make_offer(lid):
    data = request.json or {}
    if not data.get("buyer_name") or not data.get("buyer_phone") or not data.get("amount"):
        return jsonify({"error": "Name, phone and amount are required"}), 400
    u = current_user()
    if u:
        data["buyer_user_id"] = u["id"]
        data.setdefault("buyer_name",  u["name"])
        data.setdefault("buyer_phone", u["phone"])
    oid = create_offer(lid, data)
    return jsonify({"ok": True, "offer_id": oid})


@app.route("/listing/<lid>/bid", methods=["POST"])
def make_bid(lid):
    data = request.json or {}
    u = current_user()
    if u:
        data.setdefault("bidder_name",  u["name"])
        data.setdefault("bidder_phone", u["phone"])
        data["bidder_user_id"] = u["id"]
    if not data.get("bidder_name") or not data.get("bidder_phone") or not data.get("amount"):
        return jsonify({"error": "Name, phone and amount are required"}), 400
    ok, msg = place_bid(lid, data)
    if ok:
        return jsonify({"ok": True, "message": msg})
    return jsonify({"error": msg}), 400


@app.route("/listing/<lid>/buy-now", methods=["POST"])
def auction_buy_now(lid):
    data = request.json or {}
    u = current_user()
    name  = (u["name"]  if u else data.get("buyer_name",  "")).strip()
    phone = (u["phone"] if u else data.get("buyer_phone", "")).strip()
    uid   = u["id"] if u else None
    if not name or not phone:
        return jsonify({"error": "Name and phone required"}), 400
    ok, msg = buy_now(lid, name, phone, uid)
    if ok:
        return jsonify({"ok": True, "message": msg})
    return jsonify({"error": msg}), 400


@app.route("/listing/<lid>/watch", methods=["POST"])
@login_required
def toggle_watch(lid):
    u = current_user()
    watching = toggle_watchlist(u["id"], lid)
    count = get_watchlist_count(lid)
    return jsonify({"ok": True, "watching": watching, "count": count})


def _resolve_token(lid, data):
    """Return token from JSON body, or from listing if user is the owner."""
    token = data.get("token", "")
    if not token:
        u = current_user()
        if u:
            listing = get_listing_full(lid)
            if listing and listing.get("user_id") == u["id"]:
                token = listing["manage_token"]
    return token


@app.route("/listing/<lid>/lower-reserve", methods=["POST"])
def auction_lower_reserve(lid):
    data  = request.json or {}
    token = _resolve_token(lid, data)
    new_r = int(data.get("reserve_price") or data.get("new_reserve") or 0)
    if not new_r:
        return jsonify({"error": "Reserve amount required"}), 400
    ok, msg = lower_reserve(lid, new_r, token)
    if ok:
        return jsonify({"ok": True})
    return jsonify({"error": msg}), 400


@app.route("/listing/<lid>/end-early", methods=["POST"])
def auction_end_early(lid):
    data  = request.json or {}
    token = _resolve_token(lid, data)
    ok, msg = end_auction_early(lid, token)
    if ok:
        return jsonify({"ok": True})
    return jsonify({"error": msg}), 400


@app.route("/listing/<lid>/cancel-auction", methods=["POST"])
def auction_cancel(lid):
    data  = request.json or {}
    token = _resolve_token(lid, data)
    ok, msg = cancel_auction(lid, token)
    if ok:
        return jsonify({"ok": True})
    return jsonify({"error": msg}), 400


@app.route("/listing/<lid>/offer/<oid>", methods=["PATCH"])
def update_offer(lid, oid):
    data  = request.json or {}
    token = _resolve_token(lid, data)
    status = data.get("status")
    ok = respond_offer(oid, status, data.get("counter_amount"), token)
    if ok:
        return jsonify({"ok": True})
    return jsonify({"error": "Unauthorized or offer not found"}), 403


@app.route("/watchlist")
@login_required
def my_watchlist():
    u = current_user()
    raw = get_user_watchlist(session["user_id"])
    items = []
    for row in raw:
        listing = get_listing_full(row["id"])
        if not listing:
            continue
        auc = listing.get("auction") or {}
        is_winning = bool(
            auc and u and auc.get("current_bidder_id") == u["id"]
        )
        items.append({"listing": listing, "auction": auc, "is_winning": is_winning})
    return render_template("watchlist.html", items=items, fmt_egp=fmt_egp)


@app.route("/listing/<lid>/offer/<oid>/respond", methods=["POST"])
def respond_to_offer(lid, oid):
    data  = request.json or {}
    token = data.get("token", "")
    ok = respond_offer(oid, data.get("status"), data.get("counter_amount"), token)
    if ok:
        return jsonify({"ok": True})
    return jsonify({"error": "Unauthorized or offer not found"}), 403


@app.route("/listing/<lid>/mark-sold", methods=["POST"])
def mark_sold(lid):
    data  = request.json or {}
    token = data.get("token", "")
    ok = update_listing_status(lid, "sold", token)
    return jsonify({"ok": ok})


# ── API: car models for make ──────────────────────────────────────────────────
@app.route("/api/car-models")
def car_models():
    make = request.args.get("make", "")
    return jsonify(get_models_for_make(make))


# ── API: price assessment (AJAX during listing form) ─────────────────────────
@app.route("/api/assess", methods=["POST"])
def assess():
    d = request.json or {}
    if d.get("listing_type") == "car":
        ref = get_car_market_price(
            d.get("make", ""), d.get("model", ""),
            int(d.get("year") or 0),
            int(d.get("mileage_km") or 50000),
            d.get("condition", "good"),
        )
        if not ref:
            return jsonify({"error": "Model not found in reference data"})
        asking = int(d.get("asking_price") or 0)
        score  = score_car_asking(asking, ref["market_price"]) if asking else {}
        return jsonify({
            "market_price":      ref["market_price"],
            "market_price_fmt":  fmt_egp(ref["market_price"]),
            "basis":             ref.get("basis"),
            # Live market insight
            "offered_price":     ref.get("offered_price"),
            "offered_price_fmt": fmt_egp(ref["offered_price"]) if ref.get("offered_price") else None,
            "offered_n":         ref.get("offered_n"),
            "offered_p25":       ref.get("offered_p25"),
            "offered_p75":       ref.get("offered_p75"),
            "sold_price":        ref.get("sold_price"),
            "sold_price_fmt":    fmt_egp(ref["sold_price"]) if ref.get("sold_price") else None,
            "sold_n":            ref.get("sold_n"),
            "sold_p25":          ref.get("sold_p25"),
            "sold_p75":          ref.get("sold_p75"),
            **score,
        })
    else:
        ref = assess_property_price(
            d.get("area_id", ""), d.get("compound", ""),
            float(d.get("size_m2") or 0) or None,
            d.get("finishing", "fully_finished"),
            d.get("floor") or None,
        )
        if not ref:
            return jsonify({"error": "Insufficient data for estimate"})
        asking = int(d.get("asking_price") or 0)
        score  = score_property_asking(asking, ref["market_price"]) if asking else {}
        return jsonify({
            "market_price":     ref["market_price"],
            "market_price_fmt": fmt_egp(ref["market_price"]),
            "market_ppm2":      ref["market_ppm2"],
            "market_ppm2_fmt":  fmt_egp(ref["market_ppm2"]) + "/m²" if ref.get("market_ppm2") else None,
            "note":             ref["note"],
            **score,
        })


@app.route("/api/locations")
def locations_api():
    return jsonify({"cities": CITIES, "areas": AREAS, "compounds": COMPOUNDS})


# ── Auth routes ───────────────────────────────────────────────────────────────

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("index"))
    error = None
    if request.method == "POST":
        name     = request.form.get("name", "").strip()
        phone    = request.form.get("phone", "").strip()
        password = request.form.get("password", "")
        role     = request.form.get("role", "both")
        if not name or not phone or not password:
            error = "All fields are required."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        else:
            uid = create_user(name, phone, password, role)
            if uid is None:
                error = "This phone number is already registered."
            else:
                session["user_id"]   = uid
                session["user_name"] = name
                session["user_role"] = role
                return redirect(url_for("index"))
    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("index"))
    error = None
    if request.method == "POST":
        phone    = request.form.get("phone", "").strip()
        password = request.form.get("password", "")
        user     = authenticate_user(phone, password)
        if user:
            session["user_id"]   = user["id"]
            session["user_name"] = user["name"]
            session["user_role"] = user["role"]
            next_url = request.args.get("next") or url_for("index")
            return redirect(next_url)
        error = "Invalid phone number or password."
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/my-listings")
@login_required
def my_listings():
    listings = list_user_listings(session["user_id"])
    return render_template("my_listings.html", listings=listings, fmt_egp=fmt_egp)


@app.route("/my-offers")
@login_required
def my_offers():
    offers = list_user_offers(session["user_id"])
    return render_template("my_offers.html", offers=offers, fmt_egp=fmt_egp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5055))
    app.run(debug=True, port=port)
