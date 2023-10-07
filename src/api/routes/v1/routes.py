from fastapi import APIRouter

from api.routes.v1.enpoints.ping import ping_router

from core.constants.server import V1

routers = APIRouter()
router_list = [
    ping_router
]

for router in router_list:
    router.tags = routers.tags.append(V1)
    routers.include_router(router)
