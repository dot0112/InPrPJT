import redis

r = redis.Redis(host="localhost", port=6379, db=0)


def reset_redis():
    r.flushdb()
    print("Redis DB 0 초기화 완료")


if __name__ == "__main__":
    reset_redis()
