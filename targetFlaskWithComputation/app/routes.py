from flask import Blueprint, request, jsonify, current_app
import hashlib
import time

sendPath = Blueprint("path", __name__)


@sendPath.route("/stats", defaults={"path": ""})
def stats(path):
    return str(current_app.middleware.request_count)


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
