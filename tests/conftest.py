import asyncio
import json
import os
from typing import Generator, Callable

import aioredis
import pytest
from aioredis import Redis as async_redis_client
from redis import Redis as sync_redis_client
from starlette.testclient import TestClient

from app.core.app import Application, AppBuilder
from app.core.config import Config
from app.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from app.utils.constants.config import CONFIG_TEST_PATH


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def config() -> Config:
    config_path = os.environ.get("CONFIG", CONFIG_TEST_PATH)
    return Config(file=config_path)


@pytest.fixture(scope="session")
def app(config) -> Application:
    app = Application(config)
    app.full_init()

    return app


@pytest.fixture(scope="session")
def client(app) -> Generator:
    with TestClient(app.fast_api_server) as client:
        yield client


@pytest.fixture(scope="session")
async def async_redis_client(config) -> async_redis_client:
    redis = await aioredis.Redis(host=config.redis.host, port=int(config.redis.port), db=config.redis.db)

    yield redis

    await redis.close()


@pytest.fixture(scope="session")
def redis_client(config) -> sync_redis_client:
    redis = sync_redis_client(host=config.redis.host, port=int(config.redis.port), db=config.redis.db)
    redis.flushdb(asynchronous=False)

    yield redis

    redis.close()


@pytest.fixture
def redis_data_factory(redis_client) -> Callable:
    def factory(
            key: str,
            name: str,
            value: int,
            history: list[int]
    ) -> None:
        data = {
            "name": name,
            "value": value,
            "history": history
        }
        json_data = json.dumps(data)
        redis_client.set(key, json_data)
        redis_client.save()

        return

    return factory
