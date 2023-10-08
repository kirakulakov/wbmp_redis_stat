from abc import ABC

from src.repositories.base import BaseRepository


class BaseService(ABC):
    def __init__(self, repository: BaseRepository):
        self.repository = repository
