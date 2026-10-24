# Phase 0 — Foundation (review handoff)

**Source of truth:** `docs/THREE_HOUR_PLAN.md`, Phase 0, first 15 minutes.

## Implemented
- React + Vite starter with a responsive foundation landing screen.
- Python + FastAPI application with `GET /api/health`.
- CORS restricted to local Vite origins.
- Local startup instructions in `README.md`.
- Backend unit test for the health endpoint.

## Validation steps
1. In `backend`, install `requirements.txt` and run `uvicorn app.main:app --reload --port 8000`.
2. Open `http://127.0.0.1:8000/api/health`; inspect `status` and `phase`.
3. Run `python -m unittest discover -s tests -v` from `backend`.
4. In `frontend`, run `npm install`, `npm run dev`, and `npm run build`.
5. Open `http://localhost:5173` and inspect mobile and desktop layout.

**Test execution note:** The repository changes were reviewed as source through GitHub; no verified local Node/Python install and end-to-end execution evidence is attached yet. Run the steps before approving the merge.

## Study Group Finder scope
The owner has approved adding Study Group Finder conceptually. Phase 0 includes only naming the planned feature, not group matching. Before Phase 1, propose updates to the 180-minute roadmap and presentation to cover both Finder modes without extending the time box.

## Merge gate
Do **not** merge into `main` until the owner explicitly approves this phase/PR.
