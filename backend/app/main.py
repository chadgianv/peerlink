"""Phase 0: FastAPI application foundation and health check."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PEERLINK Lite API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

@app.get("/api/health")
def health() -> dict[str, str]:
    """Simple readiness endpoint: Phase 0 acceptance criterion."""
    return {"status": "ok", "application": "PEERLINK Lite", "phase": "0"}
