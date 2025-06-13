from fastapi import APIRouter, Request
from app.core.middleware import r

router = APIRouter(tags=["stats"])


@router.get("/stats")
def get_stats(request: Request):
    result = {}
    result["total_count"] = int(r.get("request_count_total"))
    return result
