from aioredis import Redis

from repository.redis import RedisRepository
from schema.statistic import StatisticModel


class StatisticRepository(RedisRepository):
    def __init__(self, db: Redis, model: StatisticModel = StatisticModel):
        super().__init__(model=model, db=db)
