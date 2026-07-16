"""
Marketplace database — supports SQLite (local dev) and PostgreSQL (Neon/Vercel).

Set DATABASE_URL env var to a Postgres connection string to switch backends.
Without it, uses the local marketplace.db SQLite file.

Tables:
  listings          — every listing (car or property)
  car_details       — car-specific fields
  property_details  — property-specific fields
  listing_photos    — ordered photo filenames (TEXT uuid id, no autoincrement)
  price_assessments — AI price verdict per listing
  offers            — buyer offers (property mode)
  bids              — buyer bids (auction mode)
  auctions          — auction config per listing
"""

import os
import sqlite3
import secrets
from contextlib import contextmanager
from pathlib import Path
from datetime import datetime, UTC
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE_URL = os.environ.get("DATABASE_URL")
_USE_PG      = bool(DATABASE_URL)
_ON_VERCEL   = bool(os.environ.get("VERCEL"))
_DEFAULT_DB  = "/tmp/marketplace.db" if _ON_VERCEL else str(Path(__file__).parent / "marketplace.db")
DB_PATH      = Path(os.environ.get("DB_PATH", _DEFAULT_DB))


# ── Helpers ───────────────────────────────────────────────────────────────────

def new_id() -> str:
    return secrets.token_urlsafe(10)


def now() -> str:
    return datetime.now(UTC).isoformat()


# ── Unified cursor wrapper ────────────────────────────────────────────────────

class _Db:
    """Normalises the sqlite3 and psycopg2 cursor APIs into one interface."""

    def __init__(self, conn, cur):
        self._conn = conn
        self._cur  = cur

    def _q(self, sql: str) -> str:
        """Replace ? placeholders with %s for Postgres."""
        return sql.replace("?", "%s") if _USE_PG else sql

    def execute(self, sql: str, params=()):
        self._cur.execute(self._q(sql), params)
        return self  # allow chaining: c.execute(...).fetchone()

    def executemany(self, sql: str, params_seq):
        q = self._q(sql)
        for p in params_seq:
            self._cur.execute(q, p)

    def executescript(self, sql: str):
        """Run multiple DDL statements separated by semicolons."""
        if _USE_PG:
            for stmt in sql.split(";"):
                stmt = stmt.strip()
                if stmt:
                    self._cur.execute(stmt)
        else:
            # sqlite3 executescript must be called on the connection
            self._conn.executescript(sql)

    def fetchone(self):
        row = self._cur.fetchone()
        return dict(row) if row is not None else None

    def fetchall(self):
        return [dict(r) for r in self._cur.fetchall()]

    @property
    def rowcount(self) -> int:
        return self._cur.rowcount


@contextmanager
def _conn():
    """Open a DB connection, yield a _Db wrapper, then commit/rollback/close."""
    if _USE_PG:
        import psycopg2
        import psycopg2.extras
        conn = psycopg2.connect(DATABASE_URL)
        cur  = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        cur = conn.cursor()

    db = _Db(conn, cur)
    try:
        yield db
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ── Upsert helper ─────────────────────────────────────────────────────────────

def _upsert_exec(db: _Db, table: str, pk_col: str, data: dict):
    """
    INSERT OR REPLACE (SQLite) / INSERT … ON CONFLICT DO UPDATE (Postgres).
    data must be a dict of {column: value} including the pk column.
    """
    cols     = list(data.keys())
    vals     = list(data.values())
    ph       = ", ".join(["?"] * len(cols))
    col_list = ", ".join(cols)

    if _USE_PG:
        sets = ", ".join(
            f"{c} = EXCLUDED.{c}" for c in cols if c != pk_col
        )
        sql = (
            f"INSERT INTO {table} ({col_list}) VALUES ({ph}) "
            f"ON CONFLICT ({pk_col}) DO UPDATE SET {sets}"
        )
    else:
        sql = f"INSERT OR REPLACE INTO {table} ({col_list}) VALUES ({ph})"

    db.execute(sql, vals)


# ── Schema ────────────────────────────────────────────────────────────────────

_SCHEMA = """
CREATE TABLE IF NOT EXISTS listings (
    id            TEXT PRIMARY KEY,
    type          TEXT NOT NULL,
    mode          TEXT NOT NULL,
    title         TEXT NOT NULL,
    description   TEXT,
    asking_price  INTEGER NOT NULL,
    seller_name   TEXT NOT NULL,
    seller_phone  TEXT NOT NULL,
    city          TEXT,
    status        TEXT DEFAULT 'active',
    manage_token  TEXT NOT NULL,
    created_at    TEXT NOT NULL,
    expires_at    TEXT
);
CREATE INDEX IF NOT EXISTS idx_l_type   ON listings(type);
CREATE INDEX IF NOT EXISTS idx_l_status ON listings(status);
CREATE INDEX IF NOT EXISTS idx_l_city   ON listings(city);

CREATE TABLE IF NOT EXISTS car_details (
    listing_id    TEXT PRIMARY KEY REFERENCES listings(id),
    make          TEXT,
    model         TEXT,
    year          INTEGER,
    mileage_km    INTEGER,
    fuel          TEXT,
    transmission  TEXT,
    condition     TEXT,
    color         TEXT,
    body_type     TEXT
);

CREATE TABLE IF NOT EXISTS property_details (
    listing_id    TEXT PRIMARY KEY REFERENCES listings(id),
    area_id       TEXT,
    area_label    TEXT,
    compound      TEXT,
    property_type TEXT,
    size_m2       REAL,
    bedrooms      INTEGER,
    bathrooms     INTEGER,
    finishing     TEXT,
    floor         TEXT,
    furnished     INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS listing_photos (
    id            TEXT PRIMARY KEY,
    listing_id    TEXT REFERENCES listings(id),
    filename      TEXT NOT NULL,
    display_order INTEGER DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_ph_listing ON listing_photos(listing_id);

CREATE TABLE IF NOT EXISTS price_assessments (
    listing_id    TEXT PRIMARY KEY REFERENCES listings(id),
    market_price  INTEGER,
    market_ppm2   INTEGER,
    verdict       TEXT,
    pct_vs_market REAL,
    basis         TEXT,
    note          TEXT,
    generated_at  TEXT
);

CREATE TABLE IF NOT EXISTS offers (
    id             TEXT PRIMARY KEY,
    listing_id     TEXT REFERENCES listings(id),
    buyer_user_id  TEXT REFERENCES users(id),
    buyer_name     TEXT NOT NULL,
    buyer_phone    TEXT NOT NULL,
    amount         INTEGER NOT NULL,
    message        TEXT,
    status         TEXT DEFAULT 'pending',
    counter_amount INTEGER,
    created_at     TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_off_listing ON offers(listing_id);

CREATE TABLE IF NOT EXISTS bids (
    id            TEXT PRIMARY KEY,
    listing_id    TEXT REFERENCES listings(id),
    bidder_name   TEXT NOT NULL,
    bidder_phone  TEXT NOT NULL,
    amount        INTEGER NOT NULL,
    created_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bid_listing ON bids(listing_id);

CREATE TABLE IF NOT EXISTS auctions (
    listing_id    TEXT PRIMARY KEY REFERENCES listings(id),
    start_price   INTEGER NOT NULL,
    reserve_price INTEGER,
    current_bid   INTEGER,
    min_increment INTEGER DEFAULT 5000,
    end_at        TEXT NOT NULL,
    status        TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS users (
    id            TEXT PRIMARY KEY,
    name          TEXT NOT NULL,
    phone         TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    role          TEXT DEFAULT 'both',
    created_at    TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_phone ON users(phone)
"""


def init_db():
    with _conn() as c:
        c.executescript(_SCHEMA)
    # Add columns if missing (safe migrations for existing DBs)
    if not _USE_PG:
        for stmt in [
            "ALTER TABLE listings ADD COLUMN user_id TEXT REFERENCES users(id)",
            "ALTER TABLE offers ADD COLUMN buyer_user_id TEXT REFERENCES users(id)",
            "CREATE INDEX IF NOT EXISTS idx_off_buyer ON offers(buyer_user_id)",
        ]:
            try:
                with _conn() as c:
                    c.execute(stmt)
            except Exception:
                pass


# ── Listings ──────────────────────────────────────────────────────────────────

def create_listing(data: dict) -> tuple[str, str]:
    lid   = new_id()
    token = secrets.token_urlsafe(20)
    with _conn() as c:
        c.execute(
            "INSERT INTO listings "
            "(id, type, mode, title, description, asking_price, "
            " seller_name, seller_phone, city, manage_token, created_at, expires_at, user_id) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                lid, data["type"], data["mode"], data["title"],
                data.get("description"), data["asking_price"],
                data["seller_name"], data["seller_phone"], data.get("city"),
                token, now(), data.get("expires_at"), data.get("user_id"),
            ),
        )
    return lid, token


def get_listing(lid: str) -> dict | None:
    with _conn() as c:
        return c.execute("SELECT * FROM listings WHERE id=?", (lid,)).fetchone()


def get_listing_full(lid: str) -> dict | None:
    row = get_listing(lid)
    if not row:
        return None
    with _conn() as c:
        if row["type"] == "car":
            det = c.execute(
                "SELECT * FROM car_details WHERE listing_id=?", (lid,)
            ).fetchone()
        else:
            det = c.execute(
                "SELECT * FROM property_details WHERE listing_id=?", (lid,)
            ).fetchone()
        photos = c.execute(
            "SELECT filename FROM listing_photos WHERE listing_id=? ORDER BY display_order",
            (lid,),
        ).fetchall()
        assessment = c.execute(
            "SELECT * FROM price_assessments WHERE listing_id=?", (lid,)
        ).fetchone()
        offers = c.execute(
            "SELECT * FROM offers WHERE listing_id=? ORDER BY created_at DESC", (lid,)
        ).fetchall()
        bids = c.execute(
            "SELECT * FROM bids WHERE listing_id=? ORDER BY amount DESC", (lid,)
        ).fetchall()
        auction = c.execute(
            "SELECT * FROM auctions WHERE listing_id=?", (lid,)
        ).fetchone()

    row["details"]    = det or {}
    row["photos"]     = [p["filename"] for p in photos]
    row["assessment"] = assessment
    row["offers"]     = offers
    row["bids"]       = bids
    row["auction"]    = auction
    return row


def list_listings(
    type_filter=None, city_filter=None, min_price=None, max_price=None,
    mode_filter=None, limit=60,
) -> list[dict]:
    where  = "l.status='active'"
    params: list = []
    if type_filter:
        where += " AND l.type=?";          params.append(type_filter)
    if city_filter:
        where += " AND l.city=?";          params.append(city_filter)
    if min_price:
        where += " AND l.asking_price>=?"; params.append(min_price)
    if max_price:
        where += " AND l.asking_price<=?"; params.append(max_price)
    if mode_filter:
        where += " AND l.mode=?";          params.append(mode_filter)
    params.append(limit)

    # Single query: listings + offer count + cover photo + assessment
    q = f"""
        SELECT
            l.*,
            COALESCE(oc.offer_count, 0) AS offer_count,
            ph.filename                 AS cover_photo,
            pa.verdict                  AS assessment_verdict,
            pa.pct_vs_market            AS assessment_pct
        FROM listings l
        LEFT JOIN (
            SELECT listing_id, COUNT(*) AS offer_count
            FROM offers
            GROUP BY listing_id
        ) oc ON oc.listing_id = l.id
        LEFT JOIN (
            SELECT listing_id, filename
            FROM listing_photos
            WHERE display_order = (
                SELECT MIN(display_order) FROM listing_photos p2
                WHERE p2.listing_id = listing_photos.listing_id
            )
        ) ph ON ph.listing_id = l.id
        LEFT JOIN price_assessments pa ON pa.listing_id = l.id
        WHERE {where}
        ORDER BY l.created_at DESC
        LIMIT ?
    """

    with _conn() as c:
        rows = c.execute(q, params).fetchall()

    result = []
    for r in rows:
        with _conn() as c:
            if r["type"] == "car":
                det = c.execute(
                    "SELECT make, model, year, mileage_km, condition "
                    "FROM car_details WHERE listing_id=?",
                    (r["id"],),
                ).fetchone()
            else:
                det = c.execute(
                    "SELECT area_label, compound, property_type, size_m2, bedrooms "
                    "FROM property_details WHERE listing_id=?",
                    (r["id"],),
                ).fetchone()

        assessment = None
        if r["assessment_verdict"]:
            assessment = {"verdict": r["assessment_verdict"], "pct_vs_market": r["assessment_pct"]}

        row_dict = dict(r)
        row_dict["assessment"] = assessment
        row_dict["details"]    = det or {}
        result.append(row_dict)
    return result


def update_listing_status(lid: str, status: str, token: str) -> bool:
    with _conn() as c:
        c.execute(
            "UPDATE listings SET status=? WHERE id=? AND manage_token=?",
            (status, lid, token),
        )
        return c.rowcount > 0


# ── Details ───────────────────────────────────────────────────────────────────

def save_car_details(listing_id: str, data: dict):
    with _conn() as c:
        _upsert_exec(c, "car_details", "listing_id", {"listing_id": listing_id, **data})


def save_property_details(listing_id: str, data: dict):
    with _conn() as c:
        _upsert_exec(c, "property_details", "listing_id", {"listing_id": listing_id, **data})


def save_photos(listing_id: str, filenames: list[str]):
    """Insert photos; each row gets a TEXT uuid primary key."""
    with _conn() as c:
        c.executemany(
            "INSERT INTO listing_photos (id, listing_id, filename, display_order) "
            "VALUES (?,?,?,?)",
            [(new_id(), listing_id, fn, i) for i, fn in enumerate(filenames)],
        )


def save_assessment(listing_id: str, data: dict):
    with _conn() as c:
        _upsert_exec(c, "price_assessments", "listing_id", {
            "listing_id":   listing_id,
            **data,
            "generated_at": now(),
        })


# ── Offers ────────────────────────────────────────────────────────────────────

def create_offer(listing_id: str, data: dict) -> str:
    oid = new_id()
    with _conn() as c:
        c.execute(
            "INSERT INTO offers "
            "(id, listing_id, buyer_user_id, buyer_name, buyer_phone, amount, message, created_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (
                oid, listing_id,
                data.get("buyer_user_id"),
                data["buyer_name"], data["buyer_phone"],
                data["amount"], data.get("message", ""), now(),
            ),
        )
    return oid


def respond_offer(offer_id: str, status: str, counter: int | None, token: str) -> bool:
    with _conn() as c:
        offer = c.execute(
            "SELECT listing_id FROM offers WHERE id=?", (offer_id,)
        ).fetchone()
        if not offer:
            return False
        listing = c.execute(
            "SELECT id FROM listings WHERE id=? AND manage_token=?",
            (offer["listing_id"], token),
        ).fetchone()
        if not listing:
            return False
        c.execute(
            "UPDATE offers SET status=?, counter_amount=? WHERE id=?",
            (status, counter, offer_id),
        )
    return True


# ── Bids ──────────────────────────────────────────────────────────────────────

def place_bid(listing_id: str, data: dict) -> tuple[bool, str]:
    bid_id = new_id()
    with _conn() as c:
        auction = c.execute(
            "SELECT * FROM auctions WHERE listing_id=? AND status='active'",
            (listing_id,),
        ).fetchone()
        if not auction:
            return False, "Auction not found or ended"
        min_bid = (auction["current_bid"] or auction["start_price"]) + auction["min_increment"]
        if data["amount"] < min_bid:
            return False, f"Minimum bid is EGP {min_bid:,}"
        c.execute(
            "INSERT INTO bids (id, listing_id, bidder_name, bidder_phone, amount, created_at) "
            "VALUES (?,?,?,?,?,?)",
            (bid_id, listing_id, data["bidder_name"], data["bidder_phone"], data["amount"], now()),
        )
        c.execute(
            "UPDATE auctions SET current_bid=? WHERE listing_id=?",
            (data["amount"], listing_id),
        )
    return True, bid_id


def save_auction(listing_id: str, data: dict):
    with _conn() as c:
        _upsert_exec(c, "auctions", "listing_id", {
            "listing_id":    listing_id,
            "start_price":   data["start_price"],
            "reserve_price": data.get("reserve_price"),
            "current_bid":   None,
            "min_increment": data.get("min_increment", 5000),
            "end_at":        data["end_at"],
            "status":        "active",
        })


def create_user(name: str, phone: str, password: str, role: str = "both") -> str | None:
    """Register a new user. Returns user id or None if phone already taken."""
    uid = new_id()
    try:
        with _conn() as c:
            c.execute(
                "INSERT INTO users (id, name, phone, password_hash, role, created_at) "
                "VALUES (?,?,?,?,?,?)",
                (uid, name.strip(), phone.strip(),
                 generate_password_hash(password), role, now()),
            )
        return uid
    except Exception:
        return None


def authenticate_user(phone: str, password: str) -> dict | None:
    """Return user dict if credentials match, else None."""
    with _conn() as c:
        row = c.execute(
            "SELECT * FROM users WHERE phone=?", (phone.strip(),)
        ).fetchone()
    if row and check_password_hash(row["password_hash"], password):
        return {k: v for k, v in row.items() if k != "password_hash"}
    return None


def get_user(uid: str) -> dict | None:
    with _conn() as c:
        row = c.execute(
            "SELECT id, name, phone, role, created_at FROM users WHERE id=?", (uid,)
        ).fetchone()
    return row


def list_user_listings(user_id: str) -> list[dict]:
    with _conn() as c:
        rows = c.execute(
            "SELECT * FROM listings WHERE user_id=? ORDER BY created_at DESC",
            (user_id,),
        ).fetchall()
    return rows


def list_user_offers(user_id: str) -> list[dict]:
    """Offers where the buyer's user_id matches (stored in buyer_user_id column)."""
    with _conn() as c:
        rows = c.execute(
            """SELECT o.*, l.title, l.asking_price, l.type, l.status AS listing_status
               FROM offers o
               JOIN listings l ON l.id = o.listing_id
               WHERE o.buyer_user_id = ?
               ORDER BY o.created_at DESC""",
            (user_id,),
        ).fetchall()
    return rows


def get_stats() -> dict:
    with _conn() as c:
        total    = c.execute(
            "SELECT COUNT(*) as n FROM listings WHERE status='active'"
        ).fetchone()["n"]
        cars     = c.execute(
            "SELECT COUNT(*) as n FROM listings WHERE type='car' AND status='active'"
        ).fetchone()["n"]
        props    = c.execute(
            "SELECT COUNT(*) as n FROM listings WHERE type='property' AND status='active'"
        ).fetchone()["n"]
        auctions = c.execute(
            "SELECT COUNT(*) as n FROM listings WHERE mode='auction' AND status='active'"
        ).fetchone()["n"]
    return {"total": total, "cars": cars, "properties": props, "auctions": auctions}


init_db()
