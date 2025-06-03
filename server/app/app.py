from flask import Flask
from .routes import main as main_blueprint
from .tasks import BoradcastScheduler, Encrypt
from .utils import StatusUtils


def create_app():
    app = Flask(__name__)
    StatusUtils().setStartTime()
    app.register_blueprint(main_blueprint)
    BoradcastScheduler()
    Encrypt()
    return app
