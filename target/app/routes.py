from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/", defaults={"path": ""})
@main.route("/<path:path>")
def catchAll(path):
    return path
