from aioredis import Redis

from src.repositories.redis import RedisRepository
from src.schemas.statistic import StatisticModel


class StatisticRepository(RedisRepository):
    def __init__(self, db: Redis, model: StatisticModel = StatisticModel):
        super().__init__(model=model, db=db)
