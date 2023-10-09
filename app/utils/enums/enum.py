from enum import Enum


class BaseEnum(str, Enum):
    pass


class DriverEnum(BaseEnum):
    redis_stat = "redis_stat"
