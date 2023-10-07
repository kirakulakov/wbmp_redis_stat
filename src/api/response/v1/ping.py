import datetime

from pydantic import Field

from api.response.base import ResponseBase


class ResponsePing(ResponseBase):
    server_time: str = Field(...)


class ResponsePingFactory:
    @staticmethod
    def get_from_current_server_time(time: str) -> ResponsePing:
        return ResponsePing(server_time=time)
