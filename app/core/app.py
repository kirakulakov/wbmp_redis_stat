from dataclasses import dataclass

import aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.v1.routes import routers as v1_routers
from app.core.config import Config
from app.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from app.utils.class_object import singleton
from app.utils.constants.server import API_V1


@singleton
@dataclass
class Application:
    config: Config | None = None
    redis_client: aioredis.Redis | None = None

    def full_init(self) -> None:
        self.init_server()
        self.include_routers()
        self.add_middleware()
        self.init_redis()
        RedisStatCustomRoute.set_app(self)

    @property
    def fast_api_server(self) -> FastAPI:
        if not self._fast_api_server:
            raise ValueError
        return self._fast_api_server

    def init_server(self) -> None:
        self._fast_api_server = FastAPI(
            debug=self.config.app.debug,
            title=self.config.app.name,
            description=self.config.app.description,
            version=self.config.app.version,
            docs_url=self.config.server.docs_url,
            openapi_url=self.config.server.openapi_url
        )

    def init_redis(self) -> None:
        self.redis_client = aioredis.Redis(
            host=self.config.redis.host,
            port=int(self.config.redis.port),
            db=self.config.redis.db
        )

    def include_routers(self) -> None:
        self._fast_api_server.include_router(v1_routers, prefix=API_V1)

    def add_middleware(self) -> None:
        self._fast_api_server.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
            allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                           "Access-Control-Allow-Origin",
                           "Authorization"],
        )

        @self._fast_api_server.on_event('shutdown')
        async def close_redis() -> None:
            await self.redis_client.close()

    def __call__(self, *args, **kwargs) -> FastAPI:
        return self._fast_api_server


@dataclass
class AppBuilder:
    app = Application()

    def with_config(self, config: Config):
        self.app.config = config
        return self

    def build(self) -> Application:
        return self.app
