from abc import ABC, abstractmethod

from repository.base import BaseRepository


class BaseService(ABC):
    def __init__(self, repository: BaseRepository):
        self.repository = repository