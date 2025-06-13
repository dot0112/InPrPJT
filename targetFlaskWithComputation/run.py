from app import createApp, RequestCounterMiddleware
import sys


app = createApp()
middleware = RequestCounterMiddleware(app.wsgi_app)
app.wsgi_app = middleware
app.middleware = middleware

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
