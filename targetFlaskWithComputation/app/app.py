from flask import Flask
from .routes import sendPath as pathBlueprint


def createApp():
    app = Flask(__name__)
    app.register_blueprint(pathBlueprint)
    return app
