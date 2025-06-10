from fastapi import APIRouter
from app.core.middleware import request_count

router = APIRouter(tags=["stats"])


@router.get("/stats")
def get_stats():
    return {"total_requests": request_count}
