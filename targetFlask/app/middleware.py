import redis

r = redis.Redis(host="localhost", port=6379, db=0)


class RequestCounterMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        r.incr("request_count_total")
        return self.wsgi_app(environ, start_response)


def register_middleware(app):
    app.wsgi_app = RequestCounterMiddleware(app.wsgi_app)

    @app.after_request
    def after_request(response):
        status = response.status_code
        r.incr(f"status_count:{status}")
        return response
