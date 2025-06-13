from fastapi import FastAPI
from app.core.middleware import count_requests
from threading import Lock


app = FastAPI()

app.state.request_count = 0
app.state.lock = Lock()

app.middleware("http")(count_requests)


from app.api import v1_router

app.include_router(v1_router)

# uvicorn app.main:app --reload
