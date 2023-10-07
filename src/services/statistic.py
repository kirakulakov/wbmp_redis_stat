from repository.base import BaseRepository
from schema.statistic import StatisticModel
from services.base import BaseService


class StatisticService(BaseService):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository=repository)

    async def get_all(self) -> list[StatisticModel]:
        return await self.repository.get_all()
