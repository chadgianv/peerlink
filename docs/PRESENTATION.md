# PEERLINK Lite — Final Seminar Presentation (Phase 5 Review)

**Status:** Speaker-ready outline and demo plan drafted, but build, backend regression tests, live browser testing, and rehearsal are **NOT YET VERIFIED**. No PPTX slide deck is claimed.

## Slide 1 — PEERLINK: Learn Better, Together
A fictional senior-high-school peer tutoring and study group finder. **Demo only — not a secure school deployment.**

## Slide 2 — The student problem
Students may know the subject they need help with, but not which peer or study group is both relevant **and available at the same time**.

## Slide 3 — Two ways to connect
**Peer Tutor Finder** recommends eligible fictional tutors. **Study Group Finder** recommends fictional groups with open seats and compatible meeting times. The app supports requests in both journeys.

## Slide 4 — Fictional accounts and user journey
Select one of **14** fictional demo profiles; the displayed sample password `peerlink-demo` is optional and does not authenticate anybody.
Student → select subject/topic/time → get ranked matches → submit pending request → switch to recipient/host account → accept/decline → student sees new status.

## Slide 5 — Architecture
React/Vite frontend → FastAPI endpoints → deterministic matching from fictional catalog. Request decisions and group membership records are stored in local SQLite. Vite proxies `/api` to Python port 8000; React normally serves on port 5173.

## Slide 6 — Explainable and actionable matching
**Tutor scores (out of 100):** 50 schedule overlap, 30 subject match, 15 topic fit, 5 same grade. Subject must be eligible; a selected schedule must be available to the tutor.
**Group scores:** 50 schedule, 35 topic, 15 free-seat bonus. Subject, open capacity and selected time are required.
Scores are transparent rules, **not AI confidence** or proof of verified academic ability.

## Slide 7 — Live demo: tutor lifecycle
Sign in as `alex` → tutor finder → Mathematics → Quadratic Equations → Wednesday 3 PM → find Joshua Reyes → **Send tutoring request**. Switch to `joshua` → tutoring inbox → accept → switch back to `alex` → **Refresh requests** → see accepted status, topic, recurring time, and request reference. Meeting location/date and contact are not generated.

## Slide 8 — Live demo: group lifecycle
Use `alex` → Study Group Finder → Mathematics → Quadratic Equations → Wednesday 3 PM → Math Study Circle → **Request to join group**. Switch to `joshua` (group host) → approve member. Switch to `alex`, refresh group requests and re-search to show **Already a member** with disabled button. Open **View group members** to see named host and accepted joiners. Prefilled unnamed members remain an unnamed count.

## Slide 9 — Scope, evidence, and limits
Features committed: fictional login switching, tutor request decisions, accepted-session status, availability-first match, group approvals/capacity, member indicators, restricted demo group roster. **No secure authentication, real student data, chat, notifications, real calendar appointments, or live contacting capability.** Backend identity values can be impersonated. Do not publish this app for real students.
**Testing evidence:** GitHub merges and source commits confirmed. Python test execution, Vite build, API/browser smoke checks, and timed rehearsal are **not verified** at this stage. The original 180-minute plan covers foundational phases; follow-on features are extra scope.

## Slide 10 — Conclusion and Q&A
PEERLINK illustrates **find compatible learning peers → request → accept → view next steps** within a fictional, local demonstration. Future production work: real authentication, consent/privacy safeguards, verified tutor identity, safe messaging, actual scheduling and group communications.

**Slide deck status:** This is a slide-by-slide Markdown outline, **not** a completed PPTX.
