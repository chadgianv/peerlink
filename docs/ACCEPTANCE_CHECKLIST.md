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
- [ ] Tutor request shows “SIMULATED” and confirms no booking or notification.
- [ ] Group join shows “SIMULATED” and confirms no membership was created.
- [ ] `npm.cmd run build` completes.
- [ ] Backend unit tests pass.
- [ ] At least one desktop and one mobile viewport tested.

## Not implemented
- Real registration, direct messaging, notifications, group membership, or booking persistence.
- Teacher verification of actual tutors and secure student identity records.

## Seminar
- [ ] Presentation and script accurately describe simulated vs functional behavior.
- [ ] Both finder modes can be demonstrated.
- [ ] Fictional data is used exclusively.
 
## Five-account demo login add-on (awaiting owner approval)
- [ ] Login displays five fictional accounts, and their usernames are documented.
- [ ] Wrong password is rejected by the demo UI.
- [ ] Public demo password signs into each selected profile.
- [ ] Profile name, grade and default subject reflect the selected account.
- [ ] Sign out returns to the login screen; refresh resets the session.
- [ ] Tutor/group search still works for different dummy accounts.
- [ ] Mobile layout does not overflow.
- [ ] Frontend production build and browser checks are executed and results recorded.
- [ ] Documentation warns that demo credentials do **not** provide real access control.
