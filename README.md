# PEERLINK Lite

Seminar-ready peer learning prototype built with **React (Vite)** and **Python (FastAPI)**.

## Phase status

**Phase 0 — foundation proposed for review.** No tutor recommendations or study group functionality exists yet. Those belong to later phases. This is not a deployed service.

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

The approved concept includes **Peer Tutor Finder** and **Study Group Finder**. The current roadmap on `main` details tutor matching; a scoped roadmap revision for group matching should be proposed for owner review before those implementation phases.

For safety, the future demo will use **fictional** students and only **simulated** booking/group requests. No real student information should be added.
