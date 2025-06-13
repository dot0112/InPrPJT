from fastapi import Request
import redis

r = redis.Redis(host="localhost", port=6379, db=0)


async def count_requests(request: Request, call_next):
    try:
        r.incr("request_count_total")
    except redis.ConnectionError:
        pass

    response = await call_next(request)

    try:
        r.incr(f"status_count:{response.status_code}")
    except redis.ConnectionError:
        pass

    return response
