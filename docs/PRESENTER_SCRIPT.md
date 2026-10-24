# PEERLINK Lite — Presenter script (updated for Phase 3)

**Opening:** “PEERLINK Lite is a student-to-student learning support concept with two options: finding a peer tutor or finding a study group.”

**Problem:** “Students often know what topic they struggle with but do not know who shares their study schedule or has relevant subject strengths.”

**Technology:** “React powers the user interface. FastAPI in Python supplies rankings using fictional records. The browser sends a JSON request and receives ranked matches.”

**Local setup:** Run the FastAPI server on port 8000, then start Vite on port 5173; Vite proxies `/api` requests to Python. Ensure both terminals remain open.\n\n**Live demo:**
1. Start both local servers (React on port 5173, Python on port 8000).
2. Select **Find a Peer Tutor** and use the fictional learner Alex Rivera, Grade 11.
3. Select **Mathematics → Quadratic Equations → Wednesday 3 PM**, then click **Find peer tutors**.
4. Explain why the top fictional tutor has the highest rule-based score.
5. Click **Request tutoring (demo)** and read the simulated-only notice.
6. Switch to **Find a Study Group**, repeat the search, and show available member seats.
7. Click **Join group (demo)** and emphasize **no actual membership is created**.

**Scoring:** Tutor points: subject 40, topic 30, time 20, grade 10. Group eligibility: subject match and open seats; score topic 50, time 30, capacity 20.

**Limitations:** “We use fictional names. Tutoring requests and group joins are simulated rather than actual bookings. It is not a school-ready platform.”

**Closing:** “The prototype illustrates how schoolmates could locate academic support efficiently.”

If API testing fails, show screenshots of verified states only; do not claim a successful live demonstration without evidence.
