from abc import abstractmethod
from typing import Type

from pydantic import BaseModel


class ResponseBase(BaseModel):
    class Config:
        use_enum_values = True


class ResponseFactoryBase:
    @staticmethod
    @abstractmethod
    def factory_method(*args, **kwargs) -> Type[ResponseBase]:
        pass
