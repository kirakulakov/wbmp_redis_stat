from pydantic import Field

from src.api.response.base import ResponseBase, ResponseFactoryBase
from src.schemas.statistic import StatisticModel


class ResponseStatistic(ResponseBase):
    key: str = Field(...)
    data: dict = Field(...)


class ResponseStatisticFactory(ResponseFactoryBase):
    @staticmethod
    def factory_method(statistic_model: StatisticModel) -> ResponseStatistic:
        return ResponseStatistic(
            key=statistic_model.key,
            data=statistic_model.data)

    @classmethod
    def get_many_from_models(cls, statistic_models: list[StatisticModel]) -> list[ResponseStatistic]:
        return [cls.factory_method(statistic_model=statistic_model) for statistic_model in statistic_models]
