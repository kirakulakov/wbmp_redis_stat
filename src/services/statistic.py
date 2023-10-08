from src.repositories.base import BaseRepository
from src.schemas.statistic import StatisticModel
from src.services.base import BaseService


class StatisticService(BaseService):
    def __init__(self, repository: BaseRepository):
        super().__init__(repository=repository)

    async def get_all(self) -> list[StatisticModel]:
        return await self.repository.get_all()
