from flask import Blueprint, jsonify
from app.models import Db

sendPath = Blueprint("path", __name__)

db = Db()


@sendPath.route("/", defaults={"path": ""})
@sendPath.route("/<path:path>")
def catchAll(path):
    result = db.select()
    return jsonify(result)
