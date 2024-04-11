import uvicorn
from dishka.integrations.fastapi import setup_dishka

from fastapi import FastAPI

from app.infrastructure.di.main import container_factory
from app.web_api.router.hotels import router


app = FastAPI()
container = container_factory()
setup_dishka(container, app)


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("app.web_api.entrypoint:app", reload=True)
