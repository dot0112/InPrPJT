from fastapi import Request


async def count_requests(request: Request, call_next):
    with request.app.state.lock:
        request.app.state.request_count += 1
    return await call_next(request)
