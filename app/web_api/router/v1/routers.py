from fastapi import APIRouter

from .hotels import router as router_hotels


v1_routers = APIRouter(prefix="/api/v1")
v1_routers.include_router(router_hotels)
