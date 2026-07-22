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
    id               TEXT PRIMARY KEY,
    listing_id       TEXT REFERENCES listings(id),
    bidder_user_id   TEXT REFERENCES users(id),
    bidder_name      TEXT NOT NULL,
    bidder_phone     TEXT NOT NULL,
    amount           INTEGER NOT NULL,
    max_auto_bid     INTEGER,
    is_autobid       INTEGER DEFAULT 0,
    created_at       TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bid_listing ON bids(listing_id);

CREATE TABLE IF NOT EXISTS auctions (
    listing_id           TEXT PRIMARY KEY REFERENCES listings(id),
    start_price          INTEGER NOT NULL,
    reserve_price        INTEGER,
    buy_now_price        INTEGER,
    buy_now_active       INTEGER DEFAULT 1,
    current_bid          INTEGER,
    current_bidder_name  TEXT,
    current_bidder_id    TEXT,
    min_increment        INTEGER DEFAULT 5000,
    auto_extend_mins     INTEGER DEFAULT 5,
    end_at               TEXT NOT NULL,
    status               TEXT DEFAULT 'active',
    winner_name          TEXT,
    winner_phone         TEXT,
    winner_user_id       TEXT,
    winner_bid           INTEGER
);

CREATE TABLE IF NOT EXISTS watchlist (
    id          TEXT PRIMARY KEY,
    user_id     TEXT NOT NULL REFERENCES users(id),
    listing_id  TEXT NOT NULL REFERENCES listings(id),
    created_at  TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_watch_ul ON watchlist(user_id, listing_id);
CREATE INDEX IF NOT EXISTS idx_watch_listing    ON watchlist(listing_id);

CREATE TABLE IF NOT EXISTS users (
    id            TEXT PRIMARY KEY,
    name          TEXT NOT NULL,
    phone         TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    role          TEXT DEFAULT 'both',
    created_at    TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_phone ON users(phone);

CREATE TABLE IF NOT EXISTS game_matches (
    code        TEXT PRIMARY KEY,
    game_type   TEXT NOT NULL DEFAULT 'tawla31',
    p1_id       TEXT NOT NULL REFERENCES users(id),
    p2_id       TEXT REFERENCES users(id),
    state       TEXT,
    seq         INTEGER NOT NULL DEFAULT 0,
    status      TEXT NOT NULL DEFAULT 'waiting',
    winner_id   TEXT,
    score1      INTEGER NOT NULL DEFAULT 0,
    score2      INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_gm_p1 ON game_matches(p1_id);
CREATE INDEX IF NOT EXISTS idx_gm_p2 ON game_matches(p2_id)
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
            # bids columns
            "ALTER TABLE bids ADD COLUMN bidder_user_id TEXT REFERENCES users(id)",
            "ALTER TABLE bids ADD COLUMN max_auto_bid INTEGER",
            "ALTER TABLE bids ADD COLUMN is_autobid INTEGER DEFAULT 0",
            "CREATE INDEX IF NOT EXISTS idx_bid_user ON bids(bidder_user_id)",
            # auctions columns
            "ALTER TABLE auctions ADD COLUMN buy_now_price INTEGER",
            "ALTER TABLE auctions ADD COLUMN buy_now_active INTEGER DEFAULT 1",
            "ALTER TABLE auctions ADD COLUMN current_bidder_name TEXT",
            "ALTER TABLE auctions ADD COLUMN current_bidder_id TEXT",
            "ALTER TABLE auctions ADD COLUMN auto_extend_mins INTEGER DEFAULT 5",
            "ALTER TABLE auctions ADD COLUMN winner_name TEXT",
            "ALTER TABLE auctions ADD COLUMN winner_phone TEXT",
            "ALTER TABLE auctions ADD COLUMN winner_user_id TEXT",
            "ALTER TABLE auctions ADD COLUMN winner_bid INTEGER",
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

def save_auction(listing_id: str, data: dict):
    with _conn() as c:
        _upsert_exec(c, "auctions", "listing_id", {
            "listing_id":       listing_id,
            "start_price":      data["start_price"],
            "reserve_price":    data.get("reserve_price"),
            "buy_now_price":    data.get("buy_now_price"),
            "buy_now_active":   1 if data.get("buy_now_price") else 0,
            "current_bid":      None,
            "current_bidder_name": None,
            "current_bidder_id":   None,
            "min_increment":    data.get("min_increment", 5000),
            "auto_extend_mins": data.get("auto_extend_mins", 5),
            "end_at":           data["end_at"],
            "status":           "active",
        })


def _close_auction_if_expired(auction: dict, db: "_Db"):
    """Check if auction time has passed; if so mark ended and assign winner."""
    from datetime import datetime
    if auction["status"] != "active":
        return auction
    try:
        end = datetime.fromisoformat(auction["end_at"].replace("Z", "+00:00"))
        now_dt = datetime.now(end.tzinfo)
    except Exception:
        return auction
    if now_dt < end:
        return auction
    # Expired — determine winner
    winner_name = auction.get("current_bidder_name")
    winner_bid  = auction.get("current_bid")
    reserve     = auction.get("reserve_price")
    if winner_bid and reserve and winner_bid < reserve:
        winner_name = None  # reserve not met, no winner
        winner_bid  = None
    db.execute(
        "UPDATE auctions SET status='ended', winner_name=?, winner_bid=? WHERE listing_id=?",
        (winner_name, winner_bid, auction["listing_id"]),
    )
    auction = dict(auction)
    auction["status"] = "ended"
    auction["winner_name"] = winner_name
    auction["winner_bid"]  = winner_bid
    return auction


def check_and_close_auction(listing_id: str) -> dict | None:
    """Called on listing view to lazily close expired auctions. Returns updated auction."""
    with _conn() as c:
        auc = c.execute("SELECT * FROM auctions WHERE listing_id=?", (listing_id,)).fetchone()
        if not auc:
            return None
        return _close_auction_if_expired(auc, c)


def place_bid(listing_id: str, data: dict) -> tuple[bool, str]:
    """
    eBay-style proxy bidding.
    data['amount'] = buyer's MAXIMUM budget (not necessarily the displayed bid).
    The system automatically bids the minimum necessary to win.
    """
    from datetime import datetime, timedelta

    with _conn() as c:
        auc = c.execute(
            "SELECT * FROM auctions WHERE listing_id=?", (listing_id,)
        ).fetchone()
        if not auc:
            return False, "Auction not found"

        auc = _close_auction_if_expired(auc, c)
        if auc["status"] != "active":
            return False, "Auction has ended"

        max_bid   = int(data["amount"])
        start     = auc["start_price"]
        cur_bid   = auc["current_bid"]
        min_inc   = auc["min_increment"]
        bidder_id = data.get("bidder_user_id")

        # Reject self-bid
        if bidder_id and auc.get("current_bidder_id") == bidder_id:
            return False, "You are already the highest bidder"

        # First bid: can equal start_price
        if cur_bid is None:
            if max_bid < start:
                return False, f"Minimum bid is EGP {start:,}"
            actual = start
            bid_id = new_id()
            c.execute(
                "INSERT INTO bids (id, listing_id, bidder_user_id, bidder_name, bidder_phone, "
                "amount, max_auto_bid, is_autobid, created_at) VALUES (?,?,?,?,?,?,?,?,?)",
                (bid_id, listing_id, bidder_id,
                 data["bidder_name"], data["bidder_phone"], actual, max_bid, 0, now()),
            )
            c.execute(
                "UPDATE auctions SET current_bid=?, current_bidder_name=?, current_bidder_id=?, "
                "buy_now_active=0 WHERE listing_id=?",
                (actual, data["bidder_name"], bidder_id, listing_id),
            )
        else:
            # Get current leader's max auto-bid
            top = c.execute(
                "SELECT * FROM bids WHERE listing_id=? AND is_autobid=0 "
                "ORDER BY amount DESC, created_at DESC LIMIT 1",
                (listing_id,),
            ).fetchone()
            top_max = (top["max_auto_bid"] or top["amount"]) if top else cur_bid

            min_to_beat = cur_bid + min_inc
            if max_bid < min_to_beat:
                return False, f"Minimum bid is EGP {min_to_beat:,}"

            if max_bid <= top_max:
                # Current leader wins via proxy — auto-counter
                new_price = min(top_max, max_bid + min_inc)
                if new_price > cur_bid and top:
                    auto_id = new_id()
                    c.execute(
                        "INSERT INTO bids (id, listing_id, bidder_user_id, bidder_name, bidder_phone, "
                        "amount, max_auto_bid, is_autobid, created_at) VALUES (?,?,?,?,?,?,?,?,?)",
                        (auto_id, listing_id, top["bidder_user_id"],
                         top["bidder_name"], top["bidder_phone"], new_price, top_max, 1, now()),
                    )
                    c.execute(
                        "UPDATE auctions SET current_bid=? WHERE listing_id=?",
                        (new_price, listing_id),
                    )
                return False, (
                    f"You've been outbid. Current bid: EGP {new_price:,}. "
                    f"Place a higher max bid to take the lead."
                )
            else:
                # New bidder wins — price rises to top_max + 1 increment
                new_price = min(max_bid, top_max + min_inc)
                bid_id = new_id()
                c.execute(
                    "INSERT INTO bids (id, listing_id, bidder_user_id, bidder_name, bidder_phone, "
                    "amount, max_auto_bid, is_autobid, created_at) VALUES (?,?,?,?,?,?,?,?,?)",
                    (bid_id, listing_id, bidder_id,
                     data["bidder_name"], data["bidder_phone"], new_price, max_bid, 0, now()),
                )
                c.execute(
                    "UPDATE auctions SET current_bid=?, current_bidder_name=?, current_bidder_id=? "
                    "WHERE listing_id=?",
                    (new_price, data["bidder_name"], bidder_id, listing_id),
                )

        # Anti-sniping: extend if bid placed in last N minutes
        extend = auc.get("auto_extend_mins") or 5
        try:
            end_dt = datetime.fromisoformat(auc["end_at"].replace("Z", "+00:00"))
            now_dt = datetime.now(end_dt.tzinfo)
            remaining_mins = (end_dt - now_dt).total_seconds() / 60
            if remaining_mins < extend:
                new_end = (end_dt + timedelta(minutes=extend)).isoformat()
                c.execute(
                    "UPDATE auctions SET end_at=? WHERE listing_id=?",
                    (new_end, listing_id),
                )
        except Exception:
            pass

    return True, "Bid placed!"


def buy_now(listing_id: str, buyer_name: str, buyer_phone: str, buyer_user_id=None) -> tuple[bool, str]:
    """Execute a Buy It Now purchase."""
    with _conn() as c:
        auc = c.execute("SELECT * FROM auctions WHERE listing_id=?", (listing_id,)).fetchone()
        if not auc or auc["status"] != "active":
            return False, "Auction not available"
        if not auc.get("buy_now_price") or not auc.get("buy_now_active"):
            return False, "Buy It Now is no longer available"
        price = auc["buy_now_price"]
        bid_id = new_id()
        c.execute(
            "INSERT INTO bids (id, listing_id, bidder_user_id, bidder_name, bidder_phone, "
            "amount, max_auto_bid, is_autobid, created_at) VALUES (?,?,?,?,?,?,?,?,?)",
            (bid_id, listing_id, buyer_user_id, buyer_name, buyer_phone, price, price, 0, now()),
        )
        c.execute(
            "UPDATE auctions SET status='ended', current_bid=?, current_bidder_name=?, "
            "current_bidder_id=?, buy_now_active=0, winner_name=?, winner_phone=?, "
            "winner_user_id=?, winner_bid=? WHERE listing_id=?",
            (price, buyer_name, buyer_user_id, buyer_name, buyer_phone, buyer_user_id, price, listing_id),
        )
        c.execute("UPDATE listings SET status='sold' WHERE id=?", (listing_id,))
    return True, "Purchase complete!"


def lower_reserve(listing_id: str, new_reserve: int, token: str) -> tuple[bool, str]:
    with _conn() as c:
        listing = c.execute(
            "SELECT * FROM listings WHERE id=? AND manage_token=?", (listing_id, token)
        ).fetchone()
        if not listing:
            return False, "Unauthorized"
        auc = c.execute("SELECT * FROM auctions WHERE listing_id=?", (listing_id,)).fetchone()
        if not auc:
            return False, "No auction"
        if auc["reserve_price"] and new_reserve >= auc["reserve_price"]:
            return False, "New reserve must be lower than current reserve"
        c.execute(
            "UPDATE auctions SET reserve_price=? WHERE listing_id=?",
            (new_reserve, listing_id),
        )
    return True, "Reserve lowered"


def end_auction_early(listing_id: str, token: str) -> tuple[bool, str]:
    """Seller ends auction early. Only allowed with 0 bids."""
    with _conn() as c:
        listing = c.execute(
            "SELECT * FROM listings WHERE id=? AND manage_token=?", (listing_id, token)
        ).fetchone()
        if not listing:
            return False, "Unauthorized"
        bid_count = c.execute(
            "SELECT COUNT(*) AS n FROM bids WHERE listing_id=?", (listing_id,)
        ).fetchone()["n"]
        if bid_count > 0:
            return False, "Cannot end early — bids already placed. Lower the reserve instead."
        c.execute(
            "UPDATE auctions SET status='ended' WHERE listing_id=?", (listing_id,)
        )
        c.execute(
            "UPDATE listings SET status='cancelled' WHERE id=?", (listing_id,)
        )
    return True, "Auction ended"


def cancel_auction(listing_id: str, token: str) -> tuple[bool, str]:
    with _conn() as c:
        listing = c.execute(
            "SELECT * FROM listings WHERE id=? AND manage_token=?", (listing_id, token)
        ).fetchone()
        if not listing:
            return False, "Unauthorized"
        c.execute("UPDATE auctions SET status='cancelled' WHERE listing_id=?", (listing_id,))
        c.execute("UPDATE listings SET status='cancelled' WHERE id=?", (listing_id,))
    return True, "Auction cancelled"


def toggle_watchlist(user_id: str, listing_id: str) -> bool:
    """Returns True if now watching, False if removed."""
    with _conn() as c:
        existing = c.execute(
            "SELECT id FROM watchlist WHERE user_id=? AND listing_id=?",
            (user_id, listing_id),
        ).fetchone()
        if existing:
            c.execute(
                "DELETE FROM watchlist WHERE user_id=? AND listing_id=?",
                (user_id, listing_id),
            )
            return False
        c.execute(
            "INSERT INTO watchlist (id, user_id, listing_id, created_at) VALUES (?,?,?,?)",
            (new_id(), user_id, listing_id, now()),
        )
        return True


def get_watchlist_count(listing_id: str) -> int:
    with _conn() as c:
        return c.execute(
            "SELECT COUNT(*) AS n FROM watchlist WHERE listing_id=?", (listing_id,)
        ).fetchone()["n"]


def is_watching(user_id: str, listing_id: str) -> bool:
    with _conn() as c:
        return bool(c.execute(
            "SELECT id FROM watchlist WHERE user_id=? AND listing_id=?",
            (user_id, listing_id),
        ).fetchone())


def get_user_watchlist(user_id: str) -> list[dict]:
    with _conn() as c:
        return c.execute(
            """SELECT l.*, w.created_at AS watched_at,
                      a.current_bid, a.end_at, a.status AS auc_status
               FROM watchlist w
               JOIN listings l ON l.id = w.listing_id
               LEFT JOIN auctions a ON a.listing_id = l.id
               WHERE w.user_id = ?
               ORDER BY w.created_at DESC""",
            (user_id,),
        ).fetchall()


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




# ── Online games ──────────────────────────────────────────────────────────────

_CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # no 0/O/1/I


def _game_code() -> str:
    return "".join(secrets.choice(_CODE_ALPHABET) for _ in range(5))


def create_game_match(user_id: str, game_type: str = "tawla31") -> str:
    """Open a new online match and return its join code."""
    for _ in range(20):
        code = _game_code()
        try:
            with _conn() as c:
                c.execute(
                    "INSERT INTO game_matches "
                    "(code, game_type, p1_id, status, created_at, updated_at) "
                    "VALUES (?,?,?,?,?,?)",
                    (code, game_type, user_id, "waiting", now(), now()),
                )
            return code
        except Exception:
            continue
    raise RuntimeError("could not allocate a game code")


def get_game_match(code: str) -> dict | None:
    with _conn() as c:
        return c.execute(
            "SELECT * FROM game_matches WHERE code=?", (code.strip().upper(),)
        ).fetchone()


def join_game_match(code: str, user_id: str) -> tuple[dict | None, str | None]:
    """Join as second player (or re-open a match you are part of)."""
    code = code.strip().upper()
    with _conn() as c:
        row = c.execute("SELECT * FROM game_matches WHERE code=?", (code,)).fetchone()
        if not row:
            return None, "No table found with that code."
        if user_id in (row["p1_id"], row["p2_id"]):
            return row, None                     # rejoining own match
        if row["p2_id"]:
            return None, "That table is already full."
        if row["status"] != "waiting":
            return None, "That match has already started."
        c.execute(
            "UPDATE game_matches SET p2_id=?, status='active', updated_at=? "
            "WHERE code=?",
            (user_id, now(), code),
        )
        row = c.execute("SELECT * FROM game_matches WHERE code=?", (code,)).fetchone()
    return row, None


def save_game_state(code: str, user_id: str, seq: int, state: str,
                    score1: int, score2: int,
                    status: str | None = None,
                    winner_id: str | None = None) -> tuple[bool, str | None]:
    """Store a new game state. seq must be exactly current seq + 1 (optimistic
    lock so two clients cannot clobber each other)."""
    with _conn() as c:
        row = c.execute("SELECT * FROM game_matches WHERE code=?", (code,)).fetchone()
        if not row:
            return False, "not_found"
        if user_id not in (row["p1_id"], row["p2_id"]):
            return False, "forbidden"
        if row["status"] == "finished":
            return False, "finished"
        if seq != row["seq"] + 1:
            return False, "conflict"
        c.execute(
            "UPDATE game_matches SET state=?, seq=?, score1=?, score2=?, "
            "status=?, winner_id=?, updated_at=? WHERE code=? AND seq=?",
            (state, seq, score1, score2, status or row["status"],
             winner_id or row["winner_id"], now(), code, row["seq"]),
        )
    return True, None


def list_user_games(user_id: str, limit: int = 50) -> list[dict]:
    """All matches (active + finished) the user is part of, newest first."""
    with _conn() as c:
        return c.execute(
            """SELECT g.*, u1.name AS p1_name, u2.name AS p2_name
               FROM game_matches g
               JOIN users u1 ON u1.id = g.p1_id
               LEFT JOIN users u2 ON u2.id = g.p2_id
               WHERE g.p1_id=? OR g.p2_id=?
               ORDER BY g.updated_at DESC
               LIMIT ?""",
            (user_id, user_id, limit),
        ).fetchall()



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
