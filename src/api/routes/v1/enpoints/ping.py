from fastapi import APIRouter

from api.response.v1.ping import ResponsePing, ResponsePingFactory

ping_router = APIRouter(
    prefix="/ping"
)


@ping_router.get("", response_model=ResponsePing)
async def ping(
):
    return ResponsePingFactory.get_from_timestamp(current_timestamp='11111')
