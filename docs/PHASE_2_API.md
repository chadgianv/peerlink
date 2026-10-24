# Phase 2 API contract

Base URL: `http://localhost:8000` (local demonstration only)

| Method | Route | Result |
| --- | --- | --- |
| GET | `/api/health` | Health status |
| GET | `/api/options` | Subject/topic map and allowed slots |
| POST | `/api/match/tutors` | Ranked eligible fictional tutors |
| POST | `/api/match/groups` | Ranked subject-matched non-full study groups |

Both POST endpoints accept:

```json
{"subject":"Mathematics","topic":"Quadratic Equations","preferred_slot":"Wednesday 3 PM","grade":11}
```

`topic` and `preferred_slot` may be empty strings; `grade` is 11 or 12. Input errors return HTTP 422. Results contain `matches`, `count`, `mode` and `demo_only`.

Ranking scores are rules-based points **not probabilities**. No matching request is persisted. No booking endpoints are in this phase.
