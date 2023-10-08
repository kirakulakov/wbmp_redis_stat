import json
from dataclasses import dataclass

import aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.v1.routes import routers as v1_routers
from src.core.config import Config
from src.utils.class_object import singleton
from src.utils.constants.server import API_V1


@singleton
@dataclass
class Application:
    config: Config
    redis_client: aioredis.Redis | None = None

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

    def include_routers(self):
        self._fast_api_server.include_router(v1_routers, prefix=API_V1)

    def add_middleware(self):
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

        @self._fast_api_server.on_event('startup')
        async def generate_fake_data() -> None:
            data = {
                "name": "suppliers",
                "value": 484961,
                "history": [
                    482152,
                    482630,
                    483057,
                    483453,
                    483897,
                    484354,
                    484961
                ]
            }
            json_data = json.dumps(data)
            await self.redis_client.set("Statistic:suppliers", json_data)

            data = {
                "name": "brands",
                "value": 484961,
                "history": [
                    482152,
                    482630,
                    483057,
                    483453,
                    483897,
                    484354,
                    484961
                ]
            }
            json_data = json.dumps(data)
            await self.redis_client.set("Statistic:brands", json_data)

            data = {
                "name": "cards",
                "value": 484961,
                "history": [
                    482152,
                    482630,
                    483057,
                    483453,
                    483897,
                    484354,
                    484961
                ]
            }
            json_data = json.dumps(data)
            await self.redis_client.set("Statistic:cards", json_data)

    def __call__(self, *args, **kwargs) -> FastAPI:
        return self._fast_api_server
