import uvicorn
from dishka.integrations.fastapi import setup_dishka

from fastapi import FastAPI

from app.infrastructure.di.main import container_factory
from app.web_api.exc_handlers import init_exc_handlers
from app.web_api.router.v1.routers import v1_routers


def init_di(app: FastAPI) -> None:
    """Dependency injection by Dishka."""
    container = container_factory()
    setup_dishka(container, app)


def init_routers(app: FastAPI) -> None:
    """Active routes."""
    app.include_router(v1_routers)


def app_factory() -> FastAPI:
    """Entrypoint factory."""
    app = FastAPI()

    init_di(app)
    init_exc_handlers(app)
    init_routers(app)
    return app


if __name__ == '__main__':
    uvicorn.run("app.web_api.entrypoint:app_factory", reload=True, factory=True)
