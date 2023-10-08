import asyncio
import os
from typing import Generator

import pytest
from starlette.testclient import TestClient

from src.core.app import Application
from src.core.config import Config
from src.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from src.utils.constants.config import CONFIG_TEST_PATH


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def config() -> Config:
    config_path = os.environ.get('CONFIG', CONFIG_TEST_PATH)
    return Config(file=config_path)


@pytest.fixture(scope='session')
def app(config) -> Application:
    app = Application(config)
    RedisStatCustomRoute.set_app(app)
    app.init_server()
    app.init_redis()
    app.include_routers()

    return app


@pytest.fixture(scope='session')
def client(app) -> Generator:
    with TestClient(app.fast_api_server) as client:
        yield client
