# PEERLINK Lite — Acceptance checklist

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
