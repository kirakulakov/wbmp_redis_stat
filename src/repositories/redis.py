import json

from aioredis import Redis

from src.repositories.base import BaseRepository
from src.schemas.base import BaseModel
from src.schemas.statistic import StatisticModel, StatisticModelFactory
from src.utils.constants.server import UTF_8

TARGET_KEYS = ["Statistic:suppliers", "Statistic:brands", "Statistic:cards"]


class RedisRepository(BaseRepository):
    def __init__(self, model: BaseModel, db: Redis):
        super().__init__(model=model)
        self.db = db

    async def get_all(self) -> list[StatisticModel]:
        values = await self.db.mget(*TARGET_KEYS)
        return [
            StatisticModelFactory.factory_method(data=json.loads(value.decode(UTF_8)))
            for value in values if value is not None
        ]
