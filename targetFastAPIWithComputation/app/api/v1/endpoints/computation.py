from fastapi import APIRouter, Query
import hashlib
import time

router = APIRouter(tags=["computation"])


@router.api_route(
    "/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
)
def catch_all(
    numHashes: int = Query(1000, description="Number of hash computations"),
    dataSize: int = Query(1024, description="Size of dummy data in bytes"),
):

    startTime = time.time()
    dummyData = b"a" * dataSize

    for _ in range(numHashes):
        hashlib.sha256(dummyData).hexdigest()

    endTime = time.time()

    return {
        "message": "complete",
        "duration": f"{endTime - startTime:.4f} seconds",
        "hashes_performed": numHashes,
    }
