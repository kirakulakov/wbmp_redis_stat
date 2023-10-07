import argparse
import os
import sys
from argparse import Namespace

import uvicorn

from core.app.app import RedisStatApplicationFactory
from core.app.base import Application
from core.config import Config
from core.constants.config import CONFIG_LOCAL_PATH
from enums.enum import DriverEnum


def _get_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver", nargs="?")
    return parser.parse_args(sys.argv[1:])


def _get_config() -> Config:
    config_path = os.environ.get("CONFIG", CONFIG_LOCAL_PATH)
    return Config(file=config_path)


def _get_app(args) -> Application:
    match args.driver:
        case DriverEnum.redis_stat:
            return RedisStatApplicationFactory.get_from_config(config)
        case _:
            return RedisStatApplicationFactory.get_from_config(config)


config = _get_config()
args = _get_args()
app = _get_app(args)

if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=config.server.host,
        port=config.server.port,
        workers=config.server.workers
    )
