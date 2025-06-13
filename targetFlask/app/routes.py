from flask import Blueprint, render_template, current_app
from app.middleware import r

sendPath = Blueprint("path", __name__)
sendHTML = Blueprint("html", __name__)


@sendPath.route("/counts", defaults={"path": ""})
def counts(path):
    keys = r.keys("status_count:*")
    result = {}
    for key in keys:
        status_code = key.decode().split(":")[1]
        count = int(r.get(key))
        result[status_code] = count
    return result


@sendHTML.route("/counts", defaults={"path": ""})
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
    count = r.get("request_count_total")
    return str(count)


@sendHTML.route("/stats", defaults={"path": ""})
def stats(path):
    count = r.get("request_count_total")
    return str(count)


@sendPath.route("/", defaults={"path": ""})
@sendPath.route("/<path:path>")
def catchAll(path):
    return path


@sendHTML.route("/", defaults={"path": ""})
@sendHTML.route("/<path:path>")
def catchAll(path):
    return render_template("index.html")
