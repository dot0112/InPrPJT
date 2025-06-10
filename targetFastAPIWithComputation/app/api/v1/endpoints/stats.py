from fastapi import APIRouter, Request

router = APIRouter(tags=["stats"])


@router.get("/stats")
def get_stats(request: Request):
    return {"total_requests": request.app.state.request_count}
