import yaml


class BaseConfig:
    def __init__(self, *, file: str | None = None, values: dict | None = None) -> None:
        if file is not None:
            self._load_from_file(file)
            return

        if values is not None:
            self._load_from_dict(values)
            return

        raise ValueError('Should be given file or values!')

    def _load_from_file(self, file: str):
        with open(file, 'r') as f:
            values: dict = yaml.load(f, yaml.Loader)
            self._load_from_dict(values)

    def _load_from_dict(self, values: dict) -> None:
        for key, value in values.items():
            if isinstance(value, dict):
                setattr(self, key, BaseConfig(values=value))
            else:
                setattr(self, key, value)


class ServerConfig(BaseConfig):
    docs_url: str = ...
    openapi_url: str = ...
    root_path: str = ...
    host: str = ...
    port: int = ...
    workers: int = ...


class ApplicationConfig(BaseConfig):
    env: str = ...
    name: str = ...
    description: str = ...
    debug: bool = ...
    version: str = ...


class Config(BaseConfig):
    server: ServerConfig = ...
    app: ApplicationConfig = ...
