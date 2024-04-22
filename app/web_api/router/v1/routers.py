from fastapi import APIRouter
from starlette.responses import RedirectResponse

from .auth import router as router_auth
from .bookings import router as router_bookings
from .hotels import router as router_hotels
from .users import router as router_users

default_router = APIRouter()


@default_router.get("/")
async def redirect_to_doct():
    return RedirectResponse("/docs", status_code=302)


v1_routers = APIRouter(prefix="/api/v1")
v1_routers.include_router(router_auth)
v1_routers.include_router(router_hotels)
v1_routers.include_router(router_users)
v1_routers.include_router(router_bookings)
