from flask import Flask
from .middleware import register_middleware
from .routes import sendPath as pathBlueprint


def createApp():
    app = Flask(__name__)
    app.register_blueprint(pathBlueprint)
    register_middleware(app)
    return app
