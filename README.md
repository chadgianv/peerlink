# PEERLINK Lite

Seminar-ready peer learning prototype built with **React (Vite)** and **Python (FastAPI)**.

## Phase status

**Phases 0 and 1 — merged. Phase 2 — proposed for review.** The React interface offers two modes, Peer Tutor Finder and Study Group Finder, with learner preference forms and search previews. Python matching endpoints exist in the Phase 2 branch, but the React interface is not integrated yet. No actual group membership or booking exists. This is not a deployed service.

## Requirements

- Node.js 20+ and npm
- Python 3.10+

## Run locally

**Terminal 1 — Python API:**

```bash
cd backend
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Windows CMD: .venv\\Scripts\\activate.bat
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open http://127.0.0.1:8000/api/health — expected JSON includes `"status":"ok"`.

**Terminal 2 — React frontend:**

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 (or the address Vite displays).

**Health smoke test** (backend virtual environment active, from `backend/`):

```bash
python -m unittest discover -s tests -v
```

**Frontend build:**

```bash
cd frontend
npm run build
```

## Roadmap and governance

- [3-hour phase roadmap](docs/THREE_HOUR_PLAN.md)
- [Mandatory review/approval instructions](AGENTS.md)

The approved concept includes **Peer Tutor Finder** and **Study Group Finder**. The Phase 1 review branch proposes a revised roadmap for both modes within 180 minutes; matching implementation comes in Phases 2–3.

For safety, the future demo will use **fictional** students and only **simulated** booking/group requests. No real student information should be added.

## Phase 2 API (review branch)

- `GET /api/options`
- `POST /api/match/tutors`
- `POST /api/match/groups`

See [API details](docs/PHASE_2_API.md) and [Phase 2 review](docs/PHASE_2_REVIEW.md). Test locally from `backend/` with `python -m unittest discover -s tests -v` and browse `http://localhost:8000/docs`.
