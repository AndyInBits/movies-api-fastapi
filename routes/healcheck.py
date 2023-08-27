from fastapi.responses import HTMLResponse
from fastapi import APIRouter

healcheck_router = APIRouter()

@healcheck_router.get("/", tags=["Health Check"])
def healcheck():
    return HTMLResponse(
        content="<h1>FastAPI</h1><p>Server running</p>",
        status_code=200,
    )
