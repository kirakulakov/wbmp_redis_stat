from dataclasses import dataclass

from api.routes.v1.routes import routers as v1_routers
from core.app.base import Application, ApplicationFactory
from core.config import Config
from core.constants.server import API_V1
from fastapi import FastAPI
from util.class_object import singleton


@singleton
@dataclass
class RedisStatApplication(Application):
    config: Config

    def __post_init__(self):
        self.init_server()
        self.include_routers()

    def init_server(self) -> None:
        self._fast_api_server = FastAPI(
            debug=self.config.app.debug,
            title=self.config.app.name,
            description=self.config.app.description,
            version=self.config.app.version,
            docs_url=self.config.server.docs_url,
            openapi_url=self.config.server.openapi_url,
            root_path=self.config.server.root_path
        )

    def include_routers(self):
        self._fast_api_server.include_router(v1_routers, prefix=API_V1)

    def __call__(self, *args, **kwargs) -> FastAPI:
        return self._fast_api_server


class RedisStatApplicationFactory(ApplicationFactory):
    @staticmethod
    def get_from_config(config: Config) -> Application:
        return RedisStatApplication(config)
