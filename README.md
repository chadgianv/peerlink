# PEERLINK Lite

Seminar-ready **React/Vite + Python/FastAPI** peer tutoring and study group finder prototype.

## Phase status
- Phases 0–4 and follow-on requests through PR #11: merged into main.
- Phase 5: presentation outline and presenter script proposed for review; live rehearsal/build tests remain unverified.

## Fictional demo accounts

The owner requested a simple classroom login to switch between five **fictional profiles**. This feature is separate from the original 180-minute roadmap. On the proposed review branch, choose one of these usernames: `alex`, `mia`, `noah`, `ella`, or `liam`. The displayed sample password is **`peerlink-demo`**, but entering a password is **optional**. Select an account and click **Enter demo as selected student** to continue immediately; any entered password text is ignored.

This is **not secure authentication**: the profiles and password are visible in frontend source, no backend endpoint is protected, and no sessions are persisted. The browser returns to login on refresh. After sign-in, the fictional student's name, grade and initial subject are applied to the finder; Sign out returns to account selection.

Never enter actual student passwords or personal details in this demonstration.

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

## Local API connectivity (Phase 4)

During local development React now sends `/api` requests through the Vite proxy to FastAPI on `http://127.0.0.1:8000`. **Both terminals must run:** backend on port 8000 and frontend on port 5173. Restart `npm.cmd run dev` after updating Vite config. Do not set `VITE_API_URL` in `.env.local` for the default setup; if it is already defined, remove it to use the proxy.

Try `http://127.0.0.1:8000/api/health` first. If the health check fails, start the backend; if it succeeds, reload React and try a tutor search. The Vite proxy only works with the local Vite development server; a production host needs `/api` routing or an explicit backend URL.

## Demo workflow (Phase 3)

1. Choose **Find a Peer Tutor** or **Find a Study Group**.
2. Enter a **fictional** learner name and choose grade, subject, topic, and schedule.
3. Click **Find**; React sends JSON to either `POST /api/match/tutors` or `POST /api/match/groups`.
4. Python returns ranked fictional matches; React displays scores, reasons, and schedule details.
5. Click the matching result's **(demo)** button; a local confirmation appears.

**IMPORTANT:** Tutor requests and group joins now save local fictional request/membership states in SQLite and can be accepted/declined by a recipient or host. This does **not** create real appointments, notifications, verified student accounts, messaging, or meetings.

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

## Functional local tutoring workflow

Sign in as **Alex Rivera**, search Mathematics / Quadratic Equations / Wednesday 3 PM, and click **Send tutoring request** on **Joshua Reyes**. FastAPI writes a *pending* request to the local SQLite file `backend/peerlink_demo.sqlite3` (ignored by Git). Sign out and use the additional **Joshua Reyes** demo account (`joshua`, optional demo password), view **incoming requests**, and choose **Accept** or **Decline**. Sign back in as Alex and click **Refresh requests** to see the final status. Fourteen selectable fictional accounts now exist: the original five learners and nine eligible tutor personas.

Every eligible recommended tutor now has a corresponding fictional sign-in account: `joshua`, `angela`, `mark`, `sofia`, `patricia`, `daniel`, `lea`, `carlo`, and `isabella`. The original five learner accounts remain available. Study-group joining uses a local demo join-and-approval workflow. Status survives browser refresh and account switching while the same backend/database is used; it does not send notifications, create actual appointments or protect identity. The demo account ID is supplied by the browser and **can be impersonated**; this must never be exposed publicly or used with real personal records. For a fresh seminar scenario, stop FastAPI and delete `backend/peerlink_demo.sqlite3` before restarting.

### After the tutor accepts

Both accounts can open **My tutoring requests & tutor inbox** and see the accepted status, subject/topic, agreed recurring time slot and session reference. The UI calls this a **demo session confirmation**. The participants must arrange a physical or online meeting separately; the app does not yet generate meeting links, calendar dates, notifications, or actual appointments. A declined request instead prompts the student to search again.

## Availability-first rankings

When a preferred schedule is selected, recommendations **exclude** tutors or groups that do not meet at that time. Tutor score: **50 shared schedule + 30 matching subject (required) + 15 topic + 5 same grade**. Group score: **50 schedule + 35 topic + 15 available capacity**, with subject and open seats mandatory. Use **Any time** to explore options, then select a shared slot before sending a tutoring request. This prevents showing a high-ranked tutor who cannot meet at the learner's chosen time.

## Functional Study Group Finder

Search with **Find a Study Group** and request membership in an available fictional group. The group's demo host reviews a pending request, accepts or declines, and the learner sees the updated status after signing back in. Host accounts: Math Study Circle → `joshua`, Algebra Buddies → `angela`, English Review Club → `sofia`, Science Study Buddies → `daniel`, Panitikan Circle → `carlo`. Full Equation Explorers stays unavailable. Accepted membership increases the group's locally stored seat usage; the backend prevents approval beyond capacity. Use **Refresh group requests** after switching accounts. SQLite is local only; no actual class groups, chats, authentication, or notifications exist.

### Study group recommendation membership indicators
Recommended groups show **Already a member** and a disabled button when the signed-in fictional account has an accepted join request. Pending join requests likewise show **Request pending** and disable repeat submission. Group recommendation results are annotated by the backend for the selected demo account; group hosts cannot join their own groups. Re-search after the host accepts to see the updated status.

## Group member directory

After the group host approves a join request, the accepted member can click **View group members** from the accepted request card. The host and approved joiners can also open **View members** from group recommendations. The directory lists the host and accepted joiners by fictional name and demo username, plus the group's subject, topic, and recurring schedule. Original placeholder members have only seeded counts, not linked accounts; they appear as an unnamed count rather than invented names. Endpoint: `GET /api/groups/{group_id}/members?account_id=...`; unapproved accounts receive HTTP 403. **Demo account IDs are unauthenticated and may be impersonated; never put real student contact information into this prototype.** No chat or private contact details.

## Final seminar preparation (Phase 5 review branch)

See [final slide-by-slide outline](docs/PRESENTATION.md), [timed demo / speaker script](docs/PRESENTER_SCRIPT.md), and [acceptance checklist](docs/ACCEPTANCE_CHECKLIST.md). The Phase 5 delivery is documentation for a seminar demonstration, **not** an exported PowerPoint deck or verified live demo. Backend tests, frontend build, and browser/mobile checks still require execution on a running local project.

## Flexible tutor requests — Any time

If the learner selects **Any time**, they may send a tutoring request to any eligible recommended tutor without choosing a specific schedule. The request is stored with a blank slot, meaning **schedule to be arranged**, not a confirmed appointment. If the tutor accepts, both see accepted status but must agree on an actual time outside the prototype. Selecting a specific slot still requires the tutor to offer that slot. Study-group times remain fixed.
