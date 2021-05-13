import redis
from redis.exceptions import ConnectionError as ConnectionError
import os


from fastapi import APIRouter
from app.ex import RestException


router = APIRouter()


def get_redis_host():
    return os.environ["REDIS_HOST"]


def get_redis_port():
    return os.environ["REDIS_PORT"]


@router.get("/redis", tags=["redis"])
async def test_redis():
    try:
        r = redis.Redis(host=get_redis_host(), port=get_redis_port())
        r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
        return [{"redis result": r.get("Bahamas")}]
    except ConnectionError:
        print("Error: redis connection error")
        raise RestException("Redis Connection Error")
