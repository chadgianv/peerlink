# AGENTS.md — PEERLINK Lite Development Instructions

> **Mandatory repository instructions for every development phase and follow-up change.**
>
> At the start of **every** development phase, read this file and `docs/THREE_HOUR_PLAN.md`. Treat this file as the development contract unless the project owner explicitly changes it.

## 1. Project mission and limits

PEERLINK Lite is a seminar-ready web app demonstrating student-to-student tutoring recommendations for Senior High School learners.

- **Frontend:** ReactJS with Vite.
- **Backend:** Python with FastAPI.
- **Prototype data:** Fictional, in-memory tutor profiles; no production student records.
- **Core journey:** Choose subject/topic/grade/time → rank eligible fictional tutors → show reasons → submit a clearly **simulated** tutoring request.
- **Time box:** Follow the six-phase, 180-minute plan in `docs/THREE_HOUR_PLAN.md`. Keep scope tight, and call out risks to the schedule.
- Do not quietly turn simulated booking, tutor verification, real messaging, or data persistence into claims of production functionality.

## 2. Non-negotiable human review and merge policy

**The developer agent writes the code; the project owner reviews and decides whether it may be merged.**

For **every phase**, and for material changes within a phase:

1. **Read the instructions.** Review this file, the development roadmap, and the current repository state.
2. **Check the baseline.** Identify the active phase and confirm the previous phase's merge/review status before starting.
3. **Create a dedicated branch off the current main branch.** Use `phase/<number>-<short-name>` (e.g., `phase/1-student-interface`) or `fix/<issue>`. **Do not write feature code directly to `main`.**
4. **Implement the phase.** Write the actual code, update relevant documentation, and add/update tests appropriate to the change. Keep commits focused.
5. **Validate before review.** Run relevant tests, lint/build checks when available, and a basic functional smoke test. Report exactly what passed, failed, or could not run. Do not fabricate test results.
6. **Present the changes for review.** Open a pull request into `main` (preferred) or provide a reviewable branch with commit and diff links if a pull request cannot be created.
7. **Give the project owner a plain-language code summary** including:
   - Phase number and objective
   - Features implemented and how they work
   - Significant files added/modified
   - API routes and data flow affected
   - Matching-rule or business-logic changes
   - Test/build results and known issues or limitations
   - Screenshots or a preview, when feasible
   - Link to the pull request or branch/diff
   - Any decisions requiring the owner's feedback
8. **STOP FOR EXPLICIT APPROVAL.** Ask whether the owner approves or wants revisions. A user request to “continue,” general encouragement, or silence must **not** be treated as approval of an outstanding pull request.
9. **Respond to requested changes on the same branch/PR.** Update code, rerun checks, summarize revisions, and request review again.
10. **Merge into `main` only after an explicit, unambiguous approval from the project owner for that particular phase/PR.** Examples: “Approved, merge Phase 1” or “Merge PR #12.” Do not infer approval from a successful build, green checks, or PR creation.
11. **After approval and merge**, provide the merge commit/link, final status, and the next proposed phase. Begin the next phase only when instructed.

**A PR, branch, passing tests, or review request is not a merge authorization.** Never bypass this policy with direct pushes, auto-merge, or squashing through another route. Do not deploy to any public host without separate user authorization.

## 3. Standard phase delivery format

Use the following structure when handing over a phase for review:

### Phase [N] — [Title] — READY FOR REVIEW
- **Objective:** ...
- **Implemented:** ...
- **Key code/files:** ...
- **Data flow / endpoints:** ...
- **Tests:** PASS / FAIL / NOT RUN, with commands and explanation
- **Known limitations:** ...
- **User-facing experience:** ...
- **Review link:** ...
- **Decision needed:** **Approve merge** or **request changes**

After the owner explicitly approves, report:

### Phase [N] — MERGED
- **PR/branch:** ...
- **Merge commit:** ...
- **Checks performed:** ...
- **Next suggested phase:** ...

Never call a phase “merged,” “deployed,” or “completed” until that action is verified.

## 4. Phase scope (read the detailed roadmap)

- **Phase 0 (15 min):** React and FastAPI setup; health check.
- **Phase 1 (40 min):** Responsive learner form and result-card UI.
- **Phase 2 (45 min):** Fictional catalog and explainable Python matching API.
- **Phase 3 (40 min):** React/API integration and simulated session requests.
- **Phase 4 (25 min):** Validation, mobile usability, error states, polish.
- **Phase 5 (15 min):** Seminar slide review, test evidence, demo rehearsal.

Phase timing is a planning budget, not a guarantee. Do not sacrifice truthful status reporting or safe code just to claim the schedule was met.

## 5. Technical requirements

- Keep frontend and backend separated (`frontend/` and `backend/`).
- Validate all API input server-side; never trust React inputs alone.
- Enable CORS only for intended local development origins, not an unrestricted wildcard by default.
- Implement matching as transparent rules for the MVP. For example: subject eligibility 40 points, topic fit 30, schedule fit 20, same grade 10 (total 100). Explain deviations before requesting approval.
- Exclude tutors who are not qualified/marked eligible in the **fictional demo dataset**.
- Clearly distinguish matching scores from verified teaching ability or statistical AI confidence.
- Keep tutor recommendations deterministic for the same sample request and dataset.
- Handle API errors, empty results, loading states, and invalid input clearly.
- Maintain keyboard-accessible labels and mobile-friendly layouts.
- Never add real student grades, phone numbers, passwords, or other sensitive student data to the repository or demo.

## 6. Documentation and presentation synchronization

With **every phase**, review and update the documents affected by implementation:

- `README.md`: current setup, features, running instructions, limitations
- `docs/THREE_HOUR_PLAN.md`: phase status and any scope changes
- `docs/PRESENTATION.md`: presentation outline and up-to-date feature claims
- `docs/PRESENTER_SCRIPT.md`: speaking notes and live-demo script
- `docs/ACCEPTANCE_CHECKLIST.md`: objective acceptance requirements
- Slide deck, if present: reflect actual reviewed features only

If a file does not exist yet, create it when relevant instead of pretending it is already available. Do not claim the presentation is updated unless the presentation file was actually changed.

## 7. Testing and safety gates

- Run available backend unit tests for matching logic and API validation.
- Run a frontend build and verify the form can submit and display valid results.
- Exercise at least Mathematics and a second subject; confirm results differ.
- Test a tutor/topic/schedule mismatch and explain the ranking.
- Ensure any session request prominently states **SIMULATED** and does not notify a real user.
- Do not expose secrets, environment files, credentials, or private student information in commits.
- Do not deploy or introduce remote services unless explicitly authorized.
- Report environmental blockers honestly and distinguish **NOT RUN** from **PASS**.

## 8. Collaboration and priorities

- Prioritize a working, demonstrable student-matching flow over nonessential embellishments.
- Make review summaries understandable to seminar presenters who are not developers.
- When the owner requests changes, implement them and return to review; do not merge until new approval.
- Do not proceed past an unapproved phase unless the owner explicitly authorizes work to continue **without merging**; in that case, preserve branch dependencies and still require explicit approval for each merge.
- If instructions conflict, pause the unsafe or irreversible action and request an owner decision; otherwise follow the latest explicit owner direction.

**Golden rule: CODE → TEST → SUMMARIZE → OWNER REVIEW → REVISE OR EXPLICIT APPROVAL → MERGE TO MAIN.**
