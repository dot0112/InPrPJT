from flask import Flask
from .routes import sendPath as pathBlueprint
from .routes import sendHTML as htmlBlueprint


def createApp(sendHTML=False):
    app = Flask(__name__)
    if not sendHTML:
        app.register_blueprint(pathBlueprint)
    else:
        app.register_blueprint(htmlBlueprint)
    return app
