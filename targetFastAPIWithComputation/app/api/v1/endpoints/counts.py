from fastapi import APIRouter, Request
from app.core.middleware import r

router = APIRouter(tags=["counts"])


@router.get("/counts")
def get_counts(request: Request):
    keys = r.keys("status_count:*")
    result = {}
    for key in keys:
        status_code = key.decode().split(":")[1]
        count = int(r.get(key))
        result[status_code] = count
    return result
