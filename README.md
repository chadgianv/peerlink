# PEERLINK Lite

Seminar-ready **React/Vite + Python/FastAPI** peer tutoring and study group finder prototype.

## Phase status
- Phases 0–2: merged into main.
- Phase 3: integration submitted for review, **not merged** until approved.
- Phase 4: testing and UI polish (pending).
- Phase 5: presentation rehearsal (pending).

## Run locally (Windows)

Start **two separate terminals** from the repository root.

**Terminal A — FastAPI**
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000
```
API documentation: http://127.0.0.1:8000/docs

**Terminal B — React**
```powershell
cd frontend
npm.cmd install
npm.cmd run dev
```
Open http://localhost:5173 in a browser.

Using `npm.cmd` avoids the PowerShell `npm.ps1` execution-policy error. Install npm dependencies from `frontend/`, not from the repository root.

## Demo workflow (Phase 3)

1. Choose **Find a Peer Tutor** or **Find a Study Group**.
2. Enter a **fictional** learner name and choose grade, subject, topic, and schedule.
3. Click **Find**; React sends JSON to either `POST /api/match/tutors` or `POST /api/match/groups`.
4. Python returns ranked fictional matches; React displays scores, reasons, and schedule details.
5. Click the matching result's **(demo)** button; a local confirmation appears.

**IMPORTANT:** Session requests and group joining are **front-end-only simulations**. They do not send a booking request to FastAPI, save records, contact classmates, or create group membership.

## Checks
```powershell
cd backend
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```
And, from `frontend/`:
```powershell
npm.cmd run build
```
These checks require local execution; their results must not be reported as passing without running them.

## References
- [Mandatory agent rules](AGENTS.md)
- [Three-hour development roadmap](docs/THREE_HOUR_PLAN.md)
- [Presentation outline](docs/PRESENTATION.md)
- [Presenter script](docs/PRESENTER_SCRIPT.md)
- [Acceptance checklist](docs/ACCEPTANCE_CHECKLIST.md)

All sample tutor and group information is fictional. The matching scores are rule-based, **not AI accuracy** or evidence of verified teaching proficiency.
