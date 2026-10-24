"""PEERLINK Lite FastAPI matching endpoints (fictional data only)."""
from typing import Literal
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, model_validator
from .catalog import TOPICS, SLOTS
from .matching import match_tutors, match_groups

app = FastAPI(title="PEERLINK Lite API", version="0.2.0")
app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

class MatchRequest(BaseModel):
    subject: Literal["Mathematics", "English", "Science", "Filipino"]
    topic: str = Field(default="", max_length=80)
    preferred_slot: str = Field(default="", max_length=50)
    grade: Literal[11, 12] = 11

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
    matches=match_groups(req.subject,req.topic,req.preferred_slot)
    return {"mode":"group","matches":matches,"count":len(matches),"demo_only":True}
