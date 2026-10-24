# PEERLINK Lite — Presentation outline (Phase 3)

1. **Title:** PEERLINK Lite — Learn Better, Together.
2. **Problem:** Students need accessible ways to find classmates with compatible academic interests and schedules.
3. **Solution:** Two modes — peer tutor recommendations and study group recommendations.
4. **Student journey:** Select a mode, choose subject/topic/time, review matches, click a simulated request.
5. **Architecture:** React/Vite sends JSON to Python/FastAPI, which ranks fictional sample records.
6. **Matching algorithm:** tutor eligibility and 40/30/20/10 points; group subject/open seat filter then 50/30/20 points.
7. **Live demonstration:** Search Mathematics / Quadratic Equations / Wednesday 3 PM in both modes; demonstrate explanations and simulated confirmation.
8. **Three-hour roadmap:** 15 + 40 + 45 + 40 + 25 + 15 = 180 minutes.
9. **Limitations and future work:** No real student accounts, persistent sessions, verification, messages, or group joins.
10. **Conclusion:** Students can discover potential learning partners with a transparent recommendation process.

**Phase 4 review state:** Local dev proxy and stale health-test correction have been committed; browser/mobile tests still require evidence. Both local servers must run.\n\n**Phase 3 implementation state:** React now calls the Phase 2 matching APIs. Request buttons deliberately create **only a local simulated confirmation**. Runtime demonstration remains subject to local verification.
 
## Requested additional demo-account segment (not in original time budget)

Show the client-side sign-in selector with five fictional profiles and optional password (example: `peerlink-demo`); enter as Alex, demonstrate tutor matching, sign out, then log in as Mia and show a different profile and initial subject. State clearly that **demo credentials are public and provide no real authentication or data protection**. This feature is an added seminar demonstration, not a production identity system.

## Optional two-account functional request demo

Alex sends Joshua a request, signs out, Joshua signs in and accepts, then Alex signs in and refreshes to see *accepted*. Local SQLite stores the fictional request; it is not a real appointment or external notification. Sixth fictional login added specifically to demonstrate recipient response.

### Expanded tutor request follow-through
Demonstrate Alex choosing **any eligible tutor account**, sign in as that tutor to accept, then return to Alex to show the **Session confirmed in PEERLINK demo** card. Clarify a recurring schedule alone is not a dated calendar event, and real meeting coordination remains outside PEERLINK Lite.

## Revised ranking formula (pending review)
Shared schedule becomes the top priority at 50 points. A selected time is a hard eligibility filter for tutor and group matches; explain why this makes recommendations actionable. Tutor: 50 time, 30 subject, 15 topic, 5 grade. Group: 50 time, 35 topic, 15 open capacity.
