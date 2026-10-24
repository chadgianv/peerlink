# PEERLINK Lite — Phase 5 Presenter Script

**State of evidence:** Script prepared for rehearsal; a completed live run has not been recorded. Do not claim all tests passed.

## Opening (20 seconds)
“PEERLINK Lite demonstrates how a senior-high-school learner can find a peer tutor or study group with a suitable topic **and overlapping availability**. All profiles are fictional and the demo login is not secure.”

## Tutor demonstration (~75–100 seconds)
1. Open `http://localhost:5173`. Choose `alex`. Password is optional.
2. Find a Peer Tutor. Mathematics → Quadratic Equations → Wednesday 3 PM → Find peer tutors.
3. Point to Joshua Reyes and explain the ranking: **50 time + 30 subject + 15 topic + 5 grade**. Tutors without Wednesday 3 PM do not appear.
4. **Send tutoring request**. It is stored **pending** in the local backend.
5. Sign out. Choose `joshua`. Under **My tutoring requests & tutor inbox**, accept the incoming request.
6. Sign out; return to `alex`; select **Refresh requests** and show the accepted status, topic, recurring slot and request ID.
7. Say: “Accepted here means the request status is saved, not that a real dated meeting, link, or notification was created.”

## Group demonstration (~90–120 seconds, separate from tutor demo)
1. As `alex`, choose **Find a Study Group**, Mathematics / Quadratic Equations / Wednesday 3 PM.
2. Select **Math Study Circle → Request to join group**. Show pending request.
3. Switch to `joshua` (group host), scroll to **My group memberships & join requests**, and **Approve member**.
4. Switch back to `alex`, **Refresh group requests**, and show Accepted.
5. Repeat group search: show **Already a member** and disabled join action; open **View members** (or **View group members** from accepted request).
6. Explain: “The fictional roster shows the host and students approved via demo accounts. Original seeded member counts are unnamed; messaging does not exist.”

## Explain score and no-match case (~20 seconds)
Availability is the largest scoring component, **50 of 100 points** in both finder modes. A learner-selected time excludes incompatible tutors or groups. If no results, choose another time or **Any time** to explore; a tutor request must still use a time the tutor offers.

## Rehearsal sequence and expected checks
- Launch backend from `backend/`: `python -m uvicorn app.main:app --reload --port 8000`.
- Launch frontend from `frontend/`: `npm.cmd run dev`.
- Check `http://127.0.0.1:8000/api/health` and `http://localhost:5173/api/health`.
- Confirm both modes, account switching, request status changes, member-directory access, and 360px mobile fit.
- Run `python -m unittest discover -s tests -v` from `backend/` and `npm.cmd run build` from `frontend/`. Record actual output and issues in `docs/ACCEPTANCE_CHECKLIST.md`.
- Prefer a **clean demo database** only if you are comfortable erasing prior fictional test requests: stop backend, back up or delete `backend/peerlink_demo.sqlite3`, then restart.
- If a live request cannot be completed, show the matching screen and explain the intended workflow accurately; do not pretend a booking or approval occurred.

## Anticipated questions
**“Is it AI?”** No: deterministic, transparent rule-based ranking, not trained AI.
**“Are the scores grades or reliability?”** No: weight-based compatibility only.
**“Why is time 50 points?”** Students cannot coordinate if they cannot meet, so selected time is also mandatory.
**“Does acceptance book a session?”** It stores a fictional accepted request, not a date/location or real invitation.
**“Are students secure?”** No: fictional accounts are public and can be impersonated; production requires authenticated identities and privacy protections.
**“Can members chat?”** Not yet. The roster shows only fictional names and demo usernames; no real contact mechanism.
**“How are full groups handled?”** Join approvals update seats; groups at capacity cannot accept more members.

## Closing (~15 seconds)
“PEERLINK shows an explainable starting point for finding learning support: compatible timing, suitable peers, requests, approval, and group visibility—all demonstrated with fictional accounts.”

**Any time demonstration:** As Alex, choose Any time, search eligible mathematics tutors and send a request to Joshua. Switch to Joshua to accept; when Alex returns, the request reads **Schedule: flexible, to be arranged together** rather than inventing a confirmed time. Specific time selections still require tutor availability.
