from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp
from fastapi import FastAPI, Request, Response


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
    async def dispatch(self, request: Request, call_next: DispatchFunction) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(content={"msg": str(e)}, status_code=500)