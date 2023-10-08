from abc import ABC, abstractmethod


class BaseFactory(ABC):
    @staticmethod
    @abstractmethod
    def factory_method(*args, **kwargs):
        pass
