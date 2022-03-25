from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from models import VisitLog
from schemas import LogModel


async def insert_visit(request: Request, response: Response):
    try:
        status_code = response.status_code
    except HTTPException:
        status_code = 502
    visit = LogModel(
        host=request.client.host,
        url=request.url.path,
        method=request.method,
        headers=dict(request.headers),
        status_code=status_code,
    )
    await VisitLog.create(**visit.dict(exclude_unset=True))


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        await insert_visit(request, response)
        return response


middleware_list = [
    Middleware(CORSMiddleware, allow_origins=["*"],  allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]),
    Middleware(LogMiddleware),
]
