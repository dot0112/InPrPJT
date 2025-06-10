from fastapi import FastAPI
from app.core.middleware import count_requests


app = FastAPI()
app.middleware("http")(count_requests)


from app.api import v1_router

app.include_router(v1_router)

# uvicorn app.main:app --reload
