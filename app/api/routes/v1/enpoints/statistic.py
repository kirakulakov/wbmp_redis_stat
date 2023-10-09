from fastapi import APIRouter, Depends

from app.api.depends import get_statistics_service
from app.api.response.v1.statistic import (ResponseStatistic,
                                           ResponseStatisticFactory)
from app.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from app.services.statistic import StatisticsService

statistic_router = APIRouter(
    prefix="/statistics",
    route_class=RedisStatCustomRoute
)


@statistic_router.get("", response_model=list[ResponseStatistic])
async def get_statistics(
        statistics_service: StatisticsService = Depends(get_statistics_service)
):
    statistic_models = await statistics_service.get_all()
    return ResponseStatisticFactory.get_many_from_models(statistic_models=statistic_models)
