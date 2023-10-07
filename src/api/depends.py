from starlette.requests import Request

from core.config import Config
from services.ping import PingService


def get_config(request: Request) -> Config:
    return request.state.config


def get_redis(request: Request):
    return request.state.redis_client


def get_ping_service():
    return PingService()
