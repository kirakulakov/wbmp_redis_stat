from typing import Callable

from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response


class RedisStatCustomRoute(APIRoute):
    __app = None

    @classmethod
    def set_app(cls, app) -> None:
        cls.__app = app

    @classmethod
    def get_app(cls):
        if not cls.__app:
            raise ValueError
        return cls.__app

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            redis_client = self.get_app().redis_client
            config = self.get_app().config

            request.state.redis_client = redis_client
            request.state.config = config
            return await original_route_handler(request)

        return custom_route_handler
