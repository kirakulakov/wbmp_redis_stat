from schema.base import BaseModel
from util.factory import BaseFactory


class StatisticModel(BaseModel):
    data: dict

class StatisticModelFactory(BaseFactory):
    @staticmethod
    def factory_method(data: dict) -> StatisticModel:
        return StatisticModel(
            data=data
        )
