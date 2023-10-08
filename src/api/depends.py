from fastapi import Depends
from starlette.requests import Request

from src.core.config import Config
from src.repositories.statistic import StatisticRepository
from src.services.ping import PingService
from src.services.statistic import StatisticService


def get_config(request: Request) -> Config:
    return request.state.config


def get_redis(request: Request):
    return request.state.redis_client


def get_ping_service() -> PingService:
    return PingService()


def get_statistic_repository(redis=Depends(get_redis)) -> StatisticRepository:
    return StatisticRepository(db=redis)


def get_statistic_service(repository=Depends(get_statistic_repository)) -> StatisticService:
    return StatisticService(repository=repository)
