# Phase 2 — Matching Engine Review

## Implemented
- Two deterministic Python matching functions in `backend/app/matching.py`.
- Ten fictional tutors; one marked ineligible and excluded from results.
- Six fictional study groups; full groups excluded.
- `POST /api/match/tutors` for subject-filtered tutor rankings: 40 subject + 30 topic + 20 time + 10 grade.
- `POST /api/match/groups` for available groups: subject and available capacity required; 50 topic + 30 time + 20 open seats.
- `GET /api/options` for subjects, topics, and schedule options.
- Pydantic validation for subject/topic/time/grade combinations.
- Four unit-test cases for matching logic and eligibility.

## Manual test commands
From `backend/`, with dependencies installed:

```cmd
python -m unittest discover -s tests -v
uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000/docs`, run either matching endpoint with:

```json
{"subject":"Mathematics","topic":"Quadratic Equations","preferred_slot":"Wednesday 3 PM","grade":11}
```

Expected top tutor: Joshua Reyes (100); top group: Math Study Circle (100). Full group Equation Explorers is excluded.

**Execution status:** Source committed and reviewed only. Tests and live HTTP checks have NOT been executed in this environment.

## Deliberately postponed
- React calls to the matching endpoints (Phase 3)
- Fake booking/group join confirmation (Phase 3)
- Actual booking, group membership and persistent database (outside seminar scope)

## Reviewer checklist
- [ ] Weights and eligibility match the three-hour plan
- [ ] No real student records
- [ ] No claims of AI or teacher validation
- [ ] Unit tests and HTTP checks executed on local computer before deployment
- [ ] Explicit approval before merging
