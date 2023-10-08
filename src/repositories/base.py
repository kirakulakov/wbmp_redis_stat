from abc import ABC, abstractmethod

from src.schemas.base import BaseModel


class BaseRepository(ABC):
    def __init__(self, model: BaseModel, *args, **kwargs):
        self.model = model

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError
