from flask import Flask
from .routes import sendPath as pathBlueprint
from .routes import sendHTML as htmlBlueprint


def createApp():
    app = Flask(__name__)
    app.register_blueprint(pathBlueprint)
