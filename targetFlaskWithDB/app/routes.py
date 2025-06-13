from flask import Blueprint, jsonify, current_app
from app.models import Db

sendPath = Blueprint("path", __name__)

db = Db()


@sendPath.route("/stats", defaults={"path": ""})
def stats(path):
    return str(current_app.middleware.request_count)


@sendPath.route("/", defaults={"path": ""})
@sendPath.route("/<path:path>")
def catchAll(path):
    result = db.select()
    return jsonify(result)
