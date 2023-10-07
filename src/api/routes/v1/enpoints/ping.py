from fastapi import APIRouter, Depends

from api.depends import get_ping_service
from api.response.v1.ping import ResponseCurrentServerTime, ResponseCurrentServerTimeFactory
from core.custom_route_classes.redis_stat import RedisStatCustomRoute
from services.ping import PingService

ping_router = APIRouter(
    prefix="/ping", route_class=RedisStatCustomRoute
)


@ping_router.get("", response_model=ResponseCurrentServerTime)
async def ping(
        ping_service: PingService = Depends(get_ping_service)
):
    current_server_time = await ping_service.get_current_server_time()
    return ResponseCurrentServerTimeFactory.factory_method(time=current_server_time)
