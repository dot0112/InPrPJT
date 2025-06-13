from flask import Blueprint, jsonify
from app.models import Db
from app.middleware import r

sendPath = Blueprint("path", __name__)

db = Db()


@sendPath.route("/counts", defaults={"path": ""})
def counts(path):
    keys = r.keys("status_count:*")
    result = {}
    for key in keys:
        status_code = key.decode().split(":")[1]
        count = int(r.get(key))
        result[status_code] = count
    return result


@sendPath.route("/stats", defaults={"path": ""})
def stats(path):
    result = {}
    result["total_count"] = int(r.get("request_count_total"))
    return result


@sendPath.route("/", defaults={"path": ""})
@sendPath.route("/<path:path>")
def catchAll(path):
    result = db.select()
    return jsonify(result)
