from aioredis import Redis

from app.repositories.redis import RedisRepository
from app.schemas.statistic import StatisticModel


class StatisticRepository(RedisRepository):
    def __init__(self, db: Redis, model: StatisticModel = StatisticModel):
        super().__init__(model=model, db=db)
