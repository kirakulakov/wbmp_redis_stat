from fastapi import APIRouter, Depends

from src.api.depends import get_statistics_service
from src.api.response.v1.statistic import (ResponseStatistic,
                                           ResponseStatisticFactory)
from src.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from src.services.statistic import StatisticsService

statistic_router = APIRouter(
    prefix="/statistic",
    route_class=RedisStatCustomRoute
)


@statistic_router.get("", response_model=list[ResponseStatistic])
async def get_statistics(
        statistics_service: StatisticsService = Depends(get_statistics_service)
):
    statistic_models = await statistics_service.get_all()
    return ResponseStatisticFactory.get_many_from_models(statistic_models=statistic_models)
