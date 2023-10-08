from fastapi import APIRouter

from src.api.routes.v1.enpoints.ping import ping_router
from src.api.routes.v1.enpoints.statistic import statistic_router

from src.utils.constants.server import V1

routers = APIRouter()
router_list = [
    ping_router,
    statistic_router
]

for router in router_list:
    router.tags = routers.tags.append(V1)
    routers.include_router(router)
