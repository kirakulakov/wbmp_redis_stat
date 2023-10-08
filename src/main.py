import os

from src.core.app import Application
from src.core.config import Config
from src.core.custom_route_classes.redis_stat import RedisStatCustomRoute
from src.utils.constants.config import CONFIG_LOCAL_PATH


def _get_config() -> Config:
    config_path = os.environ.get("CONFIG", CONFIG_LOCAL_PATH)
    return Config(file=config_path)


def _get_app(config: Config) -> Application:
    app = Application(config)
    RedisStatCustomRoute.set_app(app)

    app.init_server()
    app.init_redis()
    app.include_routers()
    app.add_middleware()
    return app


config = _get_config()
app = _get_app(config=config)
