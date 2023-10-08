from abc import abstractmethod
from typing import Type

from pydantic import BaseModel

from src.utils.factory import BaseFactory


class ResponseBase(BaseModel):
    class Config:
        use_enum_values = True
