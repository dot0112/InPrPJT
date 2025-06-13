from flask import Blueprint, request, jsonify, current_app
from app.middleware import r
import hashlib
import time

sendPath = Blueprint("path", __name__)


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
    numHashes = int(request.args.get("num_hashes", 1000))
    dataSize = int(request.args.get("data_size", 1024))

    startTime = time.time()
    dummyData = b"a" * dataSize
    for _ in range(numHashes):
        hashlib.sha256(dummyData).hexdigest()
    endTime = time.time()

    return jsonify(
        {
            "message": "complete",
            "duration": f"{endTime - startTime:.4f} seconds",
            "hashes_performed": numHashes,
        }
    )
