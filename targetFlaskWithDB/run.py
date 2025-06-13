from app import createApp, RequestCounterMiddleware
from app.models import Db

app = createApp()
middleware = RequestCounterMiddleware(app.wsgi_app)
app.wsgi_app = middleware
app.middleware = middleware

if __name__ == "__main__":
    Db()
    app.run(host="0.0.0.0", port=3000, debug=False)
