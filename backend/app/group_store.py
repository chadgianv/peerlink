"""Local fictional group join requests. Public demo identities, not real authentication."""
from .requests_store import connect, ALLOWED_ACCOUNTS
from .catalog import GROUPS

HOSTS = {"g1":"joshua","g2":"angela","g4":"sofia","g5":"daniel","g6":"carlo"}

def initialize(db):
    db.execute("""CREATE TABLE IF NOT EXISTS group_requests (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      group_id TEXT NOT NULL, learner_id TEXT NOT NULL,
      status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','accepted','declined')),
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      UNIQUE(group_id,learner_id)
    )""")
    db.commit()

def state(db, group_id):
    group=next((g for g in GROUPS if g["id"]==group_id),None)
    if group is None: return None
    accepted=db.execute("SELECT COUNT(*) FROM group_requests WHERE group_id=? AND status='accepted'",(group_id,)).fetchone()[0]
    return {**group, "host_id":HOSTS.get(group_id), "members":group["members"]+accepted,
            "available_seats":max(0,group["capacity"]-group["members"]-accepted)}

def list_groups():
    with connect() as db:
        initialize(db)
        return [state(db,g["id"]) for g in GROUPS]

def list_requests(account_id):
    with connect() as db:
        initialize(db)
        rows=db.execute("SELECT * FROM group_requests ORDER BY id DESC").fetchall()
        relevant=[dict(r) for r in rows if r["learner_id"]==account_id or HOSTS.get(r["group_id"])==account_id]
        return [{**r,"group_name":next(g["name"] for g in GROUPS if g["id"]==r["group_id"]),
                 "host_id":HOSTS.get(r["group_id"])} for r in relevant]

def join(account_id,group_id):
    if account_id not in ALLOWED_ACCOUNTS: return None,"unknown_account"
    with connect() as db:
        initialize(db)
        group=state(db,group_id)
        if group is None or group_id not in HOSTS: return None,"unknown_group"
        if account_id==HOSTS[group_id]: return None,"self"
        if group["available_seats"]<=0: return None,"full"
        existing=db.execute("SELECT id,status FROM group_requests WHERE group_id=? AND learner_id=?",(group_id,account_id)).fetchone()
        if existing: return None,"already_requested"
        cursor=db.execute("INSERT INTO group_requests(group_id,learner_id) VALUES(?,?)",(group_id,account_id))
        db.commit()
        return {"id":cursor.lastrowid,"group_id":group_id,"learner_id":account_id,"status":"pending"},None

def decide(request_id,account_id,decision):
    with connect() as db:
        initialize(db)
        db.execute("BEGIN IMMEDIATE")
        row=db.execute("SELECT * FROM group_requests WHERE id=?",(request_id,)).fetchone()
        if row is None:return None,"not_found"
        if HOSTS.get(row["group_id"])!=account_id:return None,"forbidden"
        if row["status"]!="pending":return None,"already_decided"
        if decision=="accepted" and state(db,row["group_id"])["available_seats"]<=0:return None,"full"
        db.execute("UPDATE group_requests SET status=? WHERE id=?",(decision,request_id))
        db.commit()
        return {"id":request_id,"status":decision,"group_id":row["group_id"],"learner_id":row["learner_id"]},None

# Only demo hosts and accepted members may inspect the fictional group roster.
# The catalog's initial member totals have no named accounts; do not invent them.
DISPLAY_NAMES = {"alex":"Alex Rivera","mia":"Mia Santos","noah":"Noah Cruz","ella":"Ella Garcia","liam":"Liam Reyes",
 "joshua":"Joshua Reyes","angela":"Angela Cruz","mark":"Mark Santos","sofia":"Sofia Garcia",
 "patricia":"Patricia Flores","daniel":"Daniel Lim","lea":"Lea Mendoza","carlo":"Carlo Navarro","isabella":"Isabella Aquino"}

def member_directory(group_id,account_id):
    if account_id not in ALLOWED_ACCOUNTS: return None,"unknown_account"
    with connect() as db:
        initialize(db)
        group=state(db,group_id)
        if group is None or group_id not in HOSTS: return None,"not_found"
        host=HOSTS[group_id]
        accepted=db.execute("SELECT learner_id FROM group_requests WHERE group_id=? AND status='accepted' ORDER BY id",(group_id,)).fetchall()
        member_ids=[r["learner_id"] for r in accepted]
        if account_id != host and account_id not in member_ids:
            return None,"forbidden"
        members=[{"account_id":host,"name":DISPLAY_NAMES[host],"role":"Host"}]
        members.extend({"account_id":m,"name":DISPLAY_NAMES.get(m,m),"role":"Member"} for m in member_ids)
        return {"group_id":group_id,"group_name":group["name"],"subject":group["subject"],
            "topic":group["topic"],"slot":group["slot"],
            "members":members,"unnamed_seed_members":group["members"]-len(member_ids),
            "total_member_count":group["members"],"demo_only":True},None
