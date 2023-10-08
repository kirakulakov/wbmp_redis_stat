from fastapi import APIRouter, Depends

from src.api.depends import get_statistic_service
from src.api.response.v1.statistic import ResponseStatistic, ResponseStatisticFactory
from src.services.statistic import StatisticService

statistic_router = APIRouter(
    prefix="/statistic"
)


@statistic_router.get("", response_model=list[ResponseStatistic])
async def get_stat(
        statistic_service: StatisticService = Depends(get_statistic_service)
):
    statistic_models = await statistic_service.get_all()
    return ResponseStatisticFactory.get_many_from_models(statistic_models=statistic_models)
