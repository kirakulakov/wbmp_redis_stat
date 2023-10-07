from fastapi import APIRouter, Depends

from api.depends import get_statistic_service
from api.response.v1.statistic import ResponseStatistic, ResponseStatisticFactory
from core.custom_route_classes.redis_stat import RedisStatCustomRoute
from services.statistic import StatisticService

statistic_router = APIRouter(
    prefix="/statistic", route_class=RedisStatCustomRoute
)


@statistic_router.get("", response_model=list[ResponseStatistic])
async def get_stat(
        statistic_service: StatisticService = Depends(get_statistic_service)
):
    statistic_models = await statistic_service.get_all()
    return ResponseStatisticFactory.get_many_from_models(statistic_models=statistic_models)
