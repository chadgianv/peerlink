"""Local-only SQLite demo request workflow. NOT authenticated or suitable for production."""
import os
import sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("PEERLINK_DEMO_DB", str(Path(__file__).resolve().parent.parent / "peerlink_demo.sqlite3")))
from .catalog import TUTORS
ALLOWED_ACCOUNTS = {"alex", "mia", "noah", "ella", "liam"} | {t["account_id"] for t in TUTORS if t["eligible"]}
TUTOR_ACCOUNT = {t["id"]:t["account_id"] for t in TUTORS if t["eligible"]}

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(str(DB_PATH), timeout=5)
    db.row_factory = sqlite3.Row
    db.execute("""CREATE TABLE IF NOT EXISTS tutoring_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        learner_id TEXT NOT NULL,
        tutor_id TEXT NOT NULL,
        subject TEXT NOT NULL,
        topic TEXT NOT NULL,
        slot TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','accepted','declined')),
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")
    db.commit()
    return db

def create(learner_id, tutor_id, subject, topic, slot):
    with connect() as db:
        cursor = db.execute("INSERT INTO tutoring_requests (learner_id,tutor_id,subject,topic,slot) VALUES (?,?,?,?,?)",
                            (learner_id,tutor_id,subject,topic,slot))
        db.commit()
        return get_one(db,cursor.lastrowid)

def get_one(db, request_id):
    row=db.execute("SELECT * FROM tutoring_requests WHERE id=?",(request_id,)).fetchone()
    return dict(row) if row else None

def listing(account_id):
    with connect() as db:
        tutor_ids=[t for t, owner in TUTOR_ACCOUNT.items() if owner == account_id]
        placeholders=",".join("?" for _ in tutor_ids)
        query="SELECT * FROM tutoring_requests WHERE learner_id=?"
        params=[account_id]
        if tutor_ids:
            query+=" OR tutor_id IN ("+placeholders+")"
            params+=tutor_ids
        rows=db.execute(query+" ORDER BY id DESC",params).fetchall()
        return [dict(r) for r in rows]

def decide(request_id, actor, status):
    with connect() as db:
        row=get_one(db,request_id)
        if row is None: return None, "not_found"
        if TUTOR_ACCOUNT.get(row["tutor_id"]) != actor: return None, "forbidden"
        if row["status"] != "pending": return None, "already_decided"
        db.execute("UPDATE tutoring_requests SET status=? WHERE id=?",(status,request_id))
        db.commit()
        return get_one(db,request_id), None
