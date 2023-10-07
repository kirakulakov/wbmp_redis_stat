from abc import abstractmethod
from typing import Type

from pydantic import BaseModel

from util.factory import BaseFactory


class ResponseBase(BaseModel):
    class Config:
        use_enum_values = True


class ResponseFactoryBase(BaseFactory):
    @staticmethod
    @abstractmethod
    def factory_method(*args, **kwargs) -> Type[ResponseBase]:
        pass
