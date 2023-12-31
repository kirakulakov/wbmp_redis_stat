from app.schemas.base import BaseModel
from app.utils.factory import BaseFactory


class StatisticModel(BaseModel):
    key: str
    data: dict


class StatisticModelFactory(BaseFactory):
    @staticmethod
    def factory_method(key: str, data: dict) -> StatisticModel:
        return StatisticModel(
            key=key,
            data=data
        )
