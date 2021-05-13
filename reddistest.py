import redis
import os
from redis.exceptions import ConnectionError as ConnectionError


def get_redis_host():
    return os.environ["REDIS_HOST"]


def get_redis_port():
    return os.environ["REDIS_PORT"]


try:
    r = redis.Redis(host=get_redis_host(), port=get_redis_port())
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    result = r.get("Bahamas")
    print(result)
except ConnectionError:
    print("redis connection error")
