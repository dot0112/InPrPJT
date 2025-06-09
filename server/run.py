from app import create_app, Cli
import threading
import sys

test = False

if len(sys.argv) > 1:
    if sys.argv[1].lower() in ["true", "t"]:
        print("test mode")
        test = True

app = create_app(test)

if __name__ == "__main__":
    threading.Thread(target=Cli().run, daemon=True).start()
    app.run(host="127.0.0.1", port=8000, debug=False)
