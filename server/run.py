from app import create_app, Cli
import threading


app = create_app()

if __name__ == "__main__":
    threading.Thread(target=Cli().run, daemon=True).start()
    app.run(debug=False)
