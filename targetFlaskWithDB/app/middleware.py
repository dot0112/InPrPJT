class RequestCounterMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app
        self.request_count = 0

    def __call__(self, environ, start_response):
        self.request_count += 1
        return self.wsgi_app(environ, start_response)
