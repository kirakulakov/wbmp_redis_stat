import datetime

from pydantic import Field

from api.response.base import ResponseBase


class ResponsePing(ResponseBase):
    current_timestamp: str = Field(...)


class ResponsePingFactory:
    @staticmethod
    def get_from_timestamp(current_timestamp: datetime.datetime) -> ResponsePing:
        return ResponsePing(current_timestamp=current_timestamp)
