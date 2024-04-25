import os
from contextlib import asynccontextmanager

import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin
from sqlalchemy.ext.asyncio import create_async_engine

from app.infrastructure.admin.bookings import BookingAdmin
from app.infrastructure.admin.hotels import HotelAdmin
from app.infrastructure.admin.rooms import RoomsAdmin
from app.infrastructure.admin.users import UsersAdmin
from app.infrastructure.di.main import container_factory
from app.infrastructure.persistence.redis_config import RedisSettings
from app.web_api.exc_handlers import init_exc_handlers
from app.web_api.router.v1.routers import default_router, v1_routers


def init_di(app: FastAPI) -> None:
    """Dependency injection by Dishka."""
    container = container_factory()
    setup_dishka(container, app)


def init_routers(app: FastAPI) -> None:
    """Active routes."""
    app.include_router(default_router)
    app.include_router(v1_routers)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Start up event."""
    aior = aioredis.from_url(RedisSettings(host="localhost", port=6379).url)
    FastAPICache.init(RedisBackend(aior), prefix="cache")
    yield
    await aior.close()


def init_admin_factory(app: FastAPI) -> None:
    """Init admin page."""
    admin = Admin(app, engine=create_async_engine(os.environ.get("DATABASE_URI")))
    admin.add_view(UsersAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(RoomsAdmin)
    admin.add_view(BookingAdmin)


def app_factory() -> FastAPI:
    """Entrypoint factory."""
    app = FastAPI(lifespan=lifespan)

    init_admin_factory(app)
    init_di(app)
    init_exc_handlers(app)
    init_routers(app)

    return app


if __name__ == "__main__":
    uvicorn.run("app.web_api.entrypoint:app_factory", reload=True, factory=True)
