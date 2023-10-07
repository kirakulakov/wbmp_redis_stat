from pydantic import Field

from api.response.base import ResponseBase, ResponseFactoryBase
from schema.statistic import StatisticModel


class ResponseStatistic(ResponseBase):
    data: dict = Field(...)


class ResponseStatisticFactory(ResponseFactoryBase):
    @staticmethod
    def factory_method(statistic_model: StatisticModel) -> ResponseStatistic:
        return ResponseStatistic(data=statistic_model.data)


    @classmethod
    def get_many_from_models(cls, statistic_models: list[StatisticModel]) -> list[ResponseStatistic]:
        return [cls.factory_method(statistic_model=statistic_model) for statistic_model in statistic_models]
