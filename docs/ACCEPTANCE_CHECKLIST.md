# PEERLINK Lite — Acceptance checklist

## Phase 4 quality checks
- [ ] `npm.cmd run build` succeeds from frontend folder
- [ ] `python -m unittest discover -s tests -v` succeeds from backend folder
- [ ] When the backend is stopped, a useful connection error appears
- [ ] With both servers running, default same-origin `/api` proxy gives recommendations
- [ ] Tutor search for Mathematics and English produce different results
- [ ] Group search excludes full groups
- [ ] At 360px and desktop widths the results remain usable

## Phase 3 integration (verify locally)
- [ ] Python server runs on port 8000.
- [ ] React frontend runs on port 5173.
- [ ] Peer Tutor Finder retrieves ranked results via `POST /api/match/tutors`.
- [ ] Study Group Finder retrieves ranked results via `POST /api/match/groups`.
- [ ] Changing the subject resets old matches and topic.
- [ ] Ranked cards display names, score, match reasons, and time slots or available seats.
- [ ] Loading, offline API, and no-result states are understandable.
- [ ] Tutor requests save a local pending state; accepting stores accepted status without creating a real calendar appointment or notification.
- [ ] Group join requests save pending/accepted/declined fictional membership records; no actual school enrollment or chat is created.
- [ ] `npm.cmd run build` completes.
- [ ] Backend unit tests pass.
- [ ] At least one desktop and one mobile viewport tested.

## Not implemented
- Real registration, direct messaging, notifications, secure school membership, or real booking/calendar persistence.
- Teacher verification of actual tutors and secure student identity records.

## Seminar
- [ ] Presentation and script accurately describe simulated vs functional behavior.
- [ ] Both finder modes can be demonstrated.
- [ ] Fictional data is used exclusively.
 
## Fictional demo login (already merged; verify runtime)
- [ ] Login offers 14 fictional accounts (five original learners plus nine eligible tutor personas).
- [ ] Account can enter with the password field blank (one-click demo access).
- [ ] Shared example password `peerlink-demo` is clearly visible and accepted; no password security is implied.
- [ ] Profile name, grade and default subject reflect the selected account.
- [ ] Sign out returns to the login screen; refresh resets the session.
- [ ] Tutor/group search still works for different dummy accounts.
- [ ] Mobile layout does not overflow.
- [ ] Frontend production build and browser checks are executed and results recorded.
- [ ] Documentation warns that demo credentials do **not** provide real access control.

## Owner-requested functional request demonstration
- [ ] Alex sends request to Joshua and gets pending record ID.
- [ ] Joshua's incoming inbox lists Alex's request after account switch.
- [ ] Joshua accepts/declines, and Alex sees the updated status after refresh.
- [ ] Other student account cannot decide as tutor (demo API response).
- [ ] Re-deciding a resolved request returns 409.
- [ ] Invalid schedule, unknown recipient and mismatched subject rejected.
- [ ] Local SQLite file is ignored by Git and persists after browser refresh.
- [ ] Python tests and React build executed with results recorded.
- [ ] App and docs explicitly state lack of secure authentication.

## Recommendation-account linkage and post-acceptance
- [ ] Every eligible tutor returned by API has `account_id` and matching selectable dummy login.
- [ ] Learner can send an available-slot request to a tutor other than Joshua.
- [ ] Recipient sees the incoming request and may accept/decline.
- [ ] On acceptance, both accounts see the demo session confirmation, topic, time slot and request ID.
- [ ] On decline, learner is instructed to search for another tutor.
- [ ] No real meeting date, meeting link, or notification is falsely presented as created.

## Availability-first revision
- [ ] A selected tutor time excludes all tutors not available then.
- [ ] Study groups at other times are excluded.
- [ ] Shared availability accounts for 50/100 points in both ranking formulas.
- [ ] Any time permits exploratory results; sending a request still requires a real shared slot.
- [ ] Empty state explains how to adjust times.
- [ ] Run backend regression tests and frontend build, and document actual outcomes.

## Functional Study Group Finder
- [ ] Match results exclude full groups and nonmatching times.
- [ ] Joining creates pending group request and routes it to correct host.
- [ ] Host can accept or decline; learner sees status on refresh.
- [ ] Accepted membership increases dynamic group member count and reduces seats.
- [ ] Host cannot approve over capacity; duplicates rejected.
- [ ] Python group tests, backend API smoke checks, Vite build and browser testing completed and reported honestly.

## Group membership indicators
- [ ] Accepted group member sees **Already a member** in recommendations and disabled join button.
- [ ] Pending join requester sees **Request pending** and disabled join button.
- [ ] Different account still sees join option if the group has remaining seats.
- [ ] Membership status persists across sign-outs and refreshes in local SQLite.
- [ ] Backend test, frontend build, and browser behavior verified before declaring runtime PASS.

## Group directory
- [ ] Approved member may open a fictional roster from accepted membership or recommendations.
- [ ] Group host may open roster without joining.
- [ ] Pending or unrelated demo account receives 403 when requesting roster.
- [ ] Newly accepted members appear by fictional name and username; seeded unnamed members are not misrepresented as identified students.
- [ ] Python tests, frontend build and desktop/mobile live tests are completed and results reported.

## Phase 5 seminar readiness — evidence ledger

| Check | Status | Evidence / next action |
|---|---|---|
| PR #11 merged into main | VERIFIED | GitHub merge commit `5b8ad9e05129a8579876964a6ebaaf34cfde04d0` |
| Current features summarized accurately in slides/script | DOCUMENTED | Review `docs/PRESENTATION.md` and `docs/PRESENTER_SCRIPT.md` |
| Backend Python unit suite | NOT RUN | Run `python -m unittest discover -s tests -v` from `backend/` |
| Frontend production build | NOT RUN | Run `npm.cmd run build` from `frontend/` |
| Live FastAPI / Vite health and matching | NOT RUN | Start both servers; check `/api/health`, both finder modes |
| Tutor request lifecycle in two demo accounts | NOT RUN | Alex → Joshua → Alex; verify accepted status |
| Group join / member list lifecycle | NOT RUN | Alex → Joshua host → Alex; verify badge and member directory |
| Desktop and 360px layout / projector readability | NOT RUN | Browser viewport smoke test |
| 2-minute timed demo rehearsal / fallback captured | NOT RUN | Rehearse, time, and record actual results |
| PPTX slide deck produced | NOT PROVIDED | This project currently has a Markdown outline only |

**Important:** The historical checkboxes above are not proof of execution; leave them unchecked until supported by actual output. Do not assume correctness from merged commits alone.
