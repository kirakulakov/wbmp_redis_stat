from abc import ABC, abstractmethod
from typing import Type

from ..config import BaseConfig


class Application(ABC):
    config: Type[BaseConfig]

    @abstractmethod
    def __post_init__(self):
        pass

    @abstractmethod
    def init_server(self) -> None:
        raise NotImplementedError


class ApplicationFactory:
    @staticmethod
    def get_from_config(config: Type[BaseConfig]) -> Application:
        raise NotImplementedError
