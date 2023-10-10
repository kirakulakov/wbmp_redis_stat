import yaml
from pydantic import BaseModel, Field


class ServerConfig(BaseModel):
    docs_url: str = Field(...)
    openapi_url: str = Field(...)
    host: str = Field(...)
    port: int = Field(...)
    workers: int = Field(...)


class ApplicationConfig(BaseModel):
    env: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    debug: bool = Field(...)
    version: str = Field(...)


class RedisConfig(BaseModel):
    host: str = Field(...)
    port: str = Field(...)
    db: str = Field(...)


class Config(BaseModel):
    server: ServerConfig = Field(...)
    app: ApplicationConfig = Field(...)
    redis: RedisConfig = Field(...)


class ConfigFactory:
    @staticmethod
    def get_from_path(config_path: str) -> Config:
        with open(config_path, 'r') as file:
            yml_content = file.read()
            yml_dict = yaml.safe_load(yml_content)
            config = Config.parse_obj(yml_dict)
            return config
