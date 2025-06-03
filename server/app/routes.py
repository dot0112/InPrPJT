from flask import Blueprint, Response
from app.tasks import ManageBot
from app.utils import PngUtils

main = Blueprint("main", __name__)


@main.route("/", defaults={"path": ""})
@main.route("/<path:path>")
def catch_all(path):
    manageBot = ManageBot()
    manageBot.increaseBotCount()
    if manageBot.broadcast:
        return Response(manageBot.broadcastData, mimetype="application/octet-stream")
    else:
        return ""
