from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter(tags=["catchAll"])


@app.api_route(
    "/{full_path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"],
)
async def catch_all(full_path: str, request: Request):
    return JSONResponse(content={"status": "ok"}, status_code=200)
