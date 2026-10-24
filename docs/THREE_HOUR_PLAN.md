# PEERLINK Lite — Three-Hour Development Roadmap

## Goal
Build a **seminar-ready student-to-student tutor and study group matching prototype** for Senior High School students in **180 minutes**, using **ReactJS (Vite)** and **Python (FastAPI)**.

**Demonstration flow:** Learner selects Peer Tutor Finder or Study Group Finder, plus subject, topic, grade and time → Python ranks eligible fictional tutors or groups → simulated request.

**Scope:** A demo, not a production school system. All tutor names, qualifications, and schedules are fictional. No real appointments or student notifications are created.

## Technology
- **Frontend:** ReactJS, Vite, CSS
- **Backend:** Python 3.10+, FastAPI, Uvicorn
- **Data:** In-memory fictional tutor profiles (no database)
- **Matching:** Explainable rules, no AI API required
- **Development:** VS Code, Node.js, npm, Git

## Development phases — exactly 3 hours

| Phase | Elapsed time | Duration | Deliverable | Acceptance criteria |
|---|---|---:|---|---|
| **0. Setup** | 00:00–00:15 | **15 min** | React and FastAPI projects | Both servers run; `GET /api/health` returns OK |
| **1. Student interface** | 00:15–00:55 | **40 min** | Two-mode responsive form and result placeholders | Choose name, grade, subject, topic, preferred time |
| **2. Matching engine** | 00:55–01:40 | **45 min** | Tutor/group catalogs and matching API endpoints | Only eligible tutors and available groups returned, ranked |
| **3. Integration** | 01:40–02:20 | **40 min** | React integrates both modes and demo requests | Dynamic recommendations; simulated request acknowledgment |
| **4. Quality check** | 02:20–02:45 | **25 min** | Error states, testing, UI polish | Switching subjects changes matches; works on laptop/projector |
| **5. Presentation** | 02:45–03:00 | **15 min** | Final slide review and demonstration rehearsal | Complete end-to-end demo in ~2 minutes |
| **TOTAL** | **00:00–03:00** | **180 min** | **Seminar prototype** | |

These are aggressive targets assuming Python and Node.js are installed and the team uses prepared sample data.

## Approved Study Group Finder addition

Group Finder selects only groups with a matching subject and open capacity, then uses topic fit (50 points), schedule fit (30 points), and available seats (20 points) for ranking. The three-hour prototype demonstrates discovery and simulated join requests; actual group creation, membership persistence, and live chats are out of scope. Phase 1 builds both interface modes; Phases 2–3 implement and integrate the matching logic. **Total time remains 180 minutes.**

## Core matching rules

**Eligibility:** The tutor must offer the requested subject and be marked approved **for this fictional demo**.

| Factor | Maximum points | Logic |
|---|---:|---|
| Subject | 40 | Tutor offers selected subject (required to qualify) |
| Specific topic | 30 | Topic matches tutor's listed strengths; if unspecified, award full points |
| Preferred time | 20 | Available at selected slot; if unspecified, award full points |
| Grade level | 10 | Same grade as learner |
| **Total** | **100** | Sort by score descending |

These points are a **ranking heuristic**, not an AI prediction, statistical probability, or proof of real tutoring ability.

## Required features (MVP)
1. Simple student profile form (fictional learner name and grade).
2. Four subjects: Mathematics, English, Science, and Filipino.
3. Topic and schedule dropdowns.
4. A prepared set of 10–15 fictional peer tutor profiles.
5. Python endpoint to filter and rank tutors.
6. Match results showing subject strengths, time slots, and ranking reasons.
7. Simulated tutoring request with an honest “No real booking was created” notice.
8. Mobile-responsive interface and clear empty/error/loading states.

## Additional owner-requested demonstration feature (outside the original 180-minute budget)

A client-side **five-account fictional demo login** has been proposed after Phase 4. It is a classroom account switcher only: one publicly displayed shared demo password, no backend authentication, no real security controls, no database, and no persistent accounts. The five profiles personalize the visible name, grade, and initial subject for demonstration. This is **additional scope**, not retroactively part of the original three-hour commitment. Real account security remains out of scope.

## Explicitly excluded from the 3-hour prototype
- Real student registration and authentication
- Access to actual grades or school records
- Real teacher certification or verification of student tutors
- Persistent appointment booking, tutor acceptance, and notifications
- Live chat, video calls, file uploads, and database management
- Machine learning or paid AI API integration
- Public hosting and production deployment

## Presentation plan (10 slides)

| Slide | Topic | Talking point |
|---|---|---|
| 1 | PEERLINK Lite | A peer tutor matching prototype |
| 2 | Problem | Students need help but may not know the right classmate to approach |
| 3 | Solution | Match learning needs with peers offering subject expertise |
| 4 | Student journey | Select → Match → Compare → Request |
| 5 | Architecture | React → FastAPI → fictional tutor catalog |
| 6 | Matching algorithm | Eligibility and 40/30/20/10 weighted scoring |
| 7 | Live demonstration | Mathematics → Quadratic Equations → Wednesday 3 PM |
| 8 | 180-minute roadmap | Six phases, time-boxed |
| 9 | Limitations and future work | No real student records or bookings yet |
| 10 | Conclusion and Q&A | Learn together, grow together |

### Suggested seminar live-demo script
1. Open the React student interface.
2. Use fictional student **Alex Rivera**, Grade 11.
3. Select **Mathematics → Quadratic Equations → Wednesday 3 PM**.
4. Click **Find My Peer Tutors**.
5. Explain why the best-ranked tutor is recommended.
6. Click **Request Tutoring (Demo)**.
7. Point out that no real tutor was notified and no actual booking exists.
8. Change to English to show that different subject selections produce different matches.

## Team assignments (optional)
- **Frontend:** React form, matching results, responsive UI
- **Backend:** Python FastAPI, fictional profiles, matching rules
- **Integration and QA:** Requests, errors, demo testing
- **Presentation:** Slides, speaker roles, rehearsal, fallback screenshots

## Completion checklist
- [ ] Two modes: Peer Tutor Finder and Study Group Finder
- [ ] Simulated join requests are clearly labeled

- [ ] React frontend opens locally
- [ ] FastAPI health endpoint responds
- [ ] Mathematics yields fictional Mathematics tutors
- [ ] Changing subject changes recommendations
- [ ] Topic and preferred time affect scores
- [ ] Highest-ranked tutor appears first
- [ ] Request button returns a simulated confirmation
- [ ] No real student details are used
- [ ] Presentation clearly distinguishes actual and simulated functions
- [ ] Demo and slide deck rehearsed

## After the seminar (not part of the three hours)
Add secure student authentication, teacher-verified tutoring qualifications, parental/school consent where appropriate, protected records, approved communications, real booking acceptance, and learning progress reports.

**Priority:** A small, demonstrably working matching system is preferable to a large, unfinished feature set.
