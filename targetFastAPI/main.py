from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from threading import Lock

app = FastAPI()

request_count = 0
lock = Lock()


@app.middleware("http")
async def count_requests(request: Request, call_next):
    global request_count
    with lock:
        request_count += 1
    response = await call_next(request)
    return response


@app.get("/stats")
def get_stats():
    return {"total_requests": request_count}


@app.api_route(
    "/{full_path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"],
)
async def catch_all(full_path: str, request: Request):
    # return Response(status_code=204)
    return JSONResponse(content={"status": "ok"}, status_code=200)


# uvicorn main:app --reload
