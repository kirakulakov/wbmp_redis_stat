import os

from app.core.app import AppBuilder
from app.core.config import ConfigFactory
from app.utils.constants.config import CONFIG_LOCAL_PATH

# init config
config_path = os.environ.get("CONFIG", CONFIG_LOCAL_PATH)
config = ConfigFactory.get_from_path(config_path=config_path)

# init app
app = AppBuilder().with_config(config).build()
app.full_init()
