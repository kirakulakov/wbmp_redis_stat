from fastapi import Depends
from starlette.requests import Request

from app.core.config import Config
from app.repositories.statistic import StatisticRepository
from app.services.ping import PingService
from app.services.statistic import StatisticsService


def get_config(request: Request) -> Config:
    return request.state.config


def get_redis(request: Request):
    return request.state.redis_client


def get_ping_service() -> PingService:
    return PingService()


def get_statistic_repository(redis=Depends(get_redis)) -> StatisticRepository:
    return StatisticRepository(db=redis)


def get_statistics_service(repository=Depends(get_statistic_repository)) -> StatisticsService:
    return StatisticsService(repository=repository)
