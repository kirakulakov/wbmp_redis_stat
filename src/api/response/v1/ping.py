from pydantic import Field

from src.api.response.base import ResponseBase


class ResponseCurrentServerTime(ResponseBase):
    current_server_time: str = Field(...)


class ResponseCurrentServerTimeFactory:
    @staticmethod
    def factory_method(time: str) -> ResponseCurrentServerTime:
        return ResponseCurrentServerTime(current_server_time=time)
