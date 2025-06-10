from fastapi import Request
from threading import Lock

request_count = 0
lock = Lock()


async def count_requests(request: Request, call_next):
    global request_count
    with lock:
        request_count += 1
    return await call_next(request)
