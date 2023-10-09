from aioredis import Redis
from fastapi import APIRouter, Depends

from app.api.depends import get_ping_service, get_redis
from app.api.response.v1.ping import (ResponseCurrentServerTime,
                                      ResponseCurrentServerTimeFactory)
from app.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from app.services.ping import PingService

ping_router = APIRouter(
    prefix="/ping",
    route_class=RedisStatCustomRoute
)


@ping_router.get("", response_model=ResponseCurrentServerTime)
async def ping(
        ping_service: PingService = Depends(get_ping_service),
        redis: Redis = Depends(get_redis)
):
    await redis.ping()
    current_server_time = await ping_service.get_current_server_time()
    return ResponseCurrentServerTimeFactory.factory_method(time=current_server_time)
