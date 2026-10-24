"""Transparent ranking functions, no machine learning or persistence."""
from .catalog import TUTORS, GROUPS

def match_tutors(subject: str, topic: str = "", slot: str = "", grade: int = 11) -> list[dict]:
    ranked = []
    for tutor in TUTORS:
        if not tutor["eligible"] or tutor["subject"] != subject:
            continue
        topic_fit = not topic or topic in tutor["topics"]
        time_fit = not slot or slot in tutor["slots"]
        grade_fit = tutor["grade"] == grade
        score = 40 + (30 if topic_fit else 0) + (20 if time_fit else 0) + (10 if grade_fit else 0)
        ranked.append({**{k:v for k,v in tutor.items() if k != "eligible"}, "score":score,
            "reasons": ["Subject match", "Topic match" if topic_fit else "Other topic expertise",
              "Schedule match" if time_fit else "Different available time",
              "Same grade" if grade_fit else "Different grade"]})
    return sorted(ranked, key=lambda x:(-x["score"],x["id"]))

def match_groups(subject: str, topic: str = "", slot: str = "") -> list[dict]:
    ranked = []
    for group in GROUPS:
        if group["subject"] != subject or group["members"] >= group["capacity"]:
            continue
        topic_fit = not topic or group["topic"] == topic
        time_fit = not slot or group["slot"] == slot
        score = (50 if topic_fit else 0) + (30 if time_fit else 0) + 20
        ranked.append({**group,"available_seats":group["capacity"]-group["members"],"score":score,
          "reasons":["Subject match", "Topic match" if topic_fit else "Different topic",
            "Schedule match" if time_fit else "Different schedule", "Open seats"]})
    return sorted(ranked,key=lambda x:(-x["score"],x["id"]))
