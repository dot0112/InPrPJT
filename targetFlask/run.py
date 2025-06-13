from app import createApp, RequestCounterMiddleware
import sys

sendHTML = False


if len(sys.argv) > 1:
    if sys.argv[1].lower() in ["true", "t"]:
        print("send html")
        sendHTML = True

app = createApp(sendHTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
