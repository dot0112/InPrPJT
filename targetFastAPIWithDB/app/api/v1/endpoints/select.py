from fastapi import APIRouter, Request
from fastapi.concurrency import run_in_threadpool
from app.db import Db

router = APIRouter(tags=["select"])


db = Db()


@router.api_route(
    "/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
)
async def catch_all(request: Request, full_path: str):
    result = await run_in_threadpool(db.select)
    return result
