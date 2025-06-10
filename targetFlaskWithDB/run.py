from app import createApp
from app.models import Db

app = createApp()

if __name__ == "__main__":
    Db()
    app.run(host="0.0.0.0", port=3000, debug=False)
