from flask import Flask
from .routes import main as main_blueprint
from .tasks import BoradcastScheduler, Encrypt
from .utils import StatusUtils


def create_app(test=False):
    app = Flask(__name__)
    StatusUtils().setStartTime()
    app.register_blueprint(main_blueprint)
    BoradcastScheduler(test)
    Encrypt()
    return app
