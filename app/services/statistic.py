from app.repositories.base import BaseRepository
from app.schemas.statistic import StatisticModel
from app.services.base import BaseService


class StatisticsService(BaseService):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository=repository)

    async def get_all(self) -> list[StatisticModel]:
        return await self.repository.get_all()
