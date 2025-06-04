from flask import Flask
from .routes import main as mainBlueprint


def createApp():
    app = Flask(__name__)
    app.register_blueprint(mainBlueprint)
    return app
