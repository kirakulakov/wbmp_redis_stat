from dataclasses import dataclass

from fastapi import FastAPI

from .base import Application, ApplicationFactory
from ..config import Config


@dataclass
class RedisStatApplication(Application):
    config: Config

    def __post_init__(self):
        self.init_server()

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


class RedisStatApplicationFactory(ApplicationFactory):
    @staticmethod
    def get_from_config(config: Config) -> Application:
        return RedisStatApplication(config)
