import yaml
from pydantic import BaseModel


class ServerConfig(BaseModel):
    docs_url: str = ...
    openapi_url: str = ...
    host: str = ...
    port: int = ...
    workers: int = ...


class ApplicationConfig(BaseModel):
    env: str = ...
    name: str = ...
    description: str = ...
    debug: bool = ...
    version: str = ...


class RedisConfig(BaseModel):
    host: str = ...
    port: str = ...
    db: str = ...


class Config(BaseModel):
    server: ServerConfig = ...
    app: ApplicationConfig = ...
    redis: RedisConfig = ...


class ConfigFactory:
    @staticmethod
    def get_from_path(config_path: str) -> Config:
        with open(config_path, 'r') as file:
            yml_content = file.read()
            yml_dict = yaml.safe_load(yml_content)
            config = Config.parse_obj(yml_dict)
            return config
