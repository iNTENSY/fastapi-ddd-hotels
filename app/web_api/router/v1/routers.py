from fastapi import APIRouter

from .hotels import router as router_hotels
from .auth import router as router_auth
from .users import router as router_users


v1_routers = APIRouter(prefix="/api/v1")
v1_routers.include_router(router_auth)
v1_routers.include_router(router_hotels)
v1_routers.include_router(router_users)
