from flask import Blueprint, render_template

sendPath = Blueprint("path", __name__)
sendHTML = Blueprint("html", __name__)


@sendPath.route("/", defaults={"path": ""})
@sendPath.route("/<path:path>")
def catchAll(path):
    return path


@sendHTML.route("/", defaults={"path": ""})
@sendHTML.route("/<path:path>")
def catchAll(path):
    return render_template("index.html")
