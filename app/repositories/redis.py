import json

from aioredis import Redis

from app.repositories.base import BaseRepository
from app.schemas.base import BaseModel
from app.schemas.statistic import StatisticModel, StatisticModelFactory
from app.utils.constants.server import UTF_8

_TARGET_KEYS = ["Statistic:suppliers", "Statistic:brands", "Statistic:cars"]


class RedisRepository(BaseRepository):
    def __init__(self, model: BaseModel, db: Redis):
        super().__init__(model=model)
        self.db = db

    async def get_all(self) -> list[StatisticModel]:
        values = await self.db.mget(*_TARGET_KEYS)
        statistics = []

        for key, value in zip(_TARGET_KEYS, values):
            if value is not None:
                try:
                    data = json.loads(value.decode(UTF_8))

                except (json.JSONDecodeError, UnicodeDecodeError, AttributeError) as e:
                    # logging/sentry here can be for `e` exception case.
                    continue
                else:
                    statistic = StatisticModelFactory.factory_method(data=data, key=key)
                    statistics.append(statistic)

        return statistics
