from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from threading import Lock


sendHTML = True

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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


if not sendHTML:

    @app.api_route(
        "/{full_path:path}",
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"],
    )
    async def catch_all(full_path: str, request: Request):
        return JSONResponse(content={"status": "ok"}, status_code=200)

else:

    @app.api_route(
        "/{full_path:path}",
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"],
    )
    async def catch_all(full_path: str, request: Request):
        return templates.TemplateResponse("index.html", {"request": request})


# uvicorn main:app --reload
