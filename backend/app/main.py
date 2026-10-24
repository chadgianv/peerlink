"""PEERLINK Lite FastAPI matching endpoints (fictional data only)."""
from typing import Literal
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, model_validator
from .catalog import TOPICS, SLOTS
from .matching import match_tutors, match_groups
from .catalog import TUTORS
from . import requests_store, group_store

app = FastAPI(title="PEERLINK Lite API", version="0.2.0")
app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST", "PATCH"], allow_headers=["Content-Type"])

class MatchRequest(BaseModel):
    subject: Literal["Mathematics", "English", "Science", "Filipino"]
    topic: str = Field(default="", max_length=80)
    preferred_slot: str = Field(default="", max_length=50)
    grade: Literal[11, 12] = 11
    account_id: str = Field(default="",max_length=32)

    @model_validator(mode="after")
    def validate_options(self):
        if self.topic and self.topic not in TOPICS[self.subject]:
            raise ValueError("Topic must belong to the selected subject")
        if self.preferred_slot and self.preferred_slot not in SLOTS:
            raise ValueError("Unknown time slot")
        return self

@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status":"ok","application":"PEERLINK Lite","phase":"2"}

@app.get("/api/options")
def options():
    return {"subjects":TOPICS,"slots":SLOTS,"notice":"Fictional seminar data only"}

@app.post("/api/match/tutors")
def tutors(req: MatchRequest):
    matches=match_tutors(req.subject,req.topic,req.preferred_slot,req.grade)
    return {"mode":"tutor","matches":matches,"count":len(matches),"demo_only":True}

@app.post("/api/match/groups")
def groups(req: MatchRequest):
    if req.account_id and req.account_id not in requests_store.ALLOWED_ACCOUNTS:
        raise HTTPException(422,"Unknown demo account.")
    available={g["id"]:g for g in group_store.list_groups()}
    memberships={r["group_id"]:r["status"] for r in group_store.list_requests(req.account_id) if r["learner_id"]==req.account_id} if req.account_id else {}
    matches=[{**m,"members":available[m["id"]]["members"],"available_seats":available[m["id"]]["available_seats"],"host_id":available[m["id"]]["host_id"],"membership_status":memberships.get(m["id"],"")} for m in match_groups(req.subject,req.topic,req.preferred_slot) if available[m["id"]]["available_seats"]>0 or memberships.get(m["id"])=="accepted"]
    return {"mode":"group","matches":matches,"count":len(matches),"demo_only":True}

# Classroom demonstration: account names are public IDs, NOT authentication.
class TutoringRequest(BaseModel):
    learner_id: str = Field(min_length=2,max_length=32)
    tutor_id: str = Field(min_length=2,max_length=10)
    subject: Literal["Mathematics","English","Science","Filipino"]
    topic: str = Field(default="",max_length=80)
    preferred_slot: str = Field(min_length=1,max_length=50)

class TutorDecision(BaseModel):
    account_id: str
    status: Literal["accepted","declined"]

@app.post("/api/requests",status_code=201)
def submit_tutoring(req: TutoringRequest):
    tutor=next((x for x in TUTORS if x["id"]==req.tutor_id and x["eligible"]),None)
    if tutor is None or tutor["subject"] != req.subject:
        raise HTTPException(422,"Tutor does not offer this subject.")
    if req.learner_id not in requests_store.ALLOWED_ACCOUNTS:
        raise HTTPException(422,"Unknown learner demo account.")
    if req.learner_id == requests_store.TUTOR_ACCOUNT[req.tutor_id]:
        raise HTTPException(422,"Cannot request tutoring from yourself.")
    if req.topic and req.topic not in TOPICS[req.subject]:
        raise HTTPException(422,"Invalid topic.")
    if req.preferred_slot not in tutor["slots"]:
        raise HTTPException(422,"Choose an available tutor schedule.")
    return requests_store.create(req.learner_id,req.tutor_id,req.subject,req.topic,req.preferred_slot)

@app.get("/api/requests")
def list_tutoring(account_id: str):
    if account_id not in requests_store.ALLOWED_ACCOUNTS:
        raise HTTPException(422,"Unknown demo account.")
    return {"requests":requests_store.listing(account_id),"demo_only":True}

@app.patch("/api/requests/{request_id}")
def respond_tutoring(request_id: int, decision: TutorDecision):
    record, err=requests_store.decide(request_id,decision.account_id,decision.status)
    if err == "not_found": raise HTTPException(404,"Request not found.")
    if err == "forbidden": raise HTTPException(403,"Only the selected tutor demo account can respond.")
    if err == "already_decided": raise HTTPException(409,"This request has already been decided.")
    return record

class GroupJoinRequest(BaseModel):
    account_id: str
    group_id: str

class GroupJoinDecision(BaseModel):
    account_id: str
    status: Literal["accepted","declined"]

@app.get("/api/groups")
def demo_groups():
    return {"groups":group_store.list_groups(),"demo_only":True}

@app.get("/api/group-requests")
def group_inbox(account_id: str):
    if account_id not in requests_store.ALLOWED_ACCOUNTS:
        raise HTTPException(422,"Unknown demo account.")
    return {"requests":group_store.list_requests(account_id),"demo_only":True}

@app.post("/api/group-requests",status_code=201)
def join_group(req: GroupJoinRequest):
    data,err=group_store.join(req.account_id,req.group_id)
    if err: raise HTTPException(409 if err in ("full","already_requested") else 422,err.replace("_"," "))
    return data

@app.patch("/api/group-requests/{request_id}")
def decide_group(request_id: int,decision: GroupJoinDecision):
    data,err=group_store.decide(request_id,decision.account_id,decision.status)
    if err: raise HTTPException({"not_found":404,"forbidden":403,"already_decided":409,"full":409}[err],err.replace("_"," "))
    return data
