import os
from pathlib import Path
from collections.abc import AsyncIterable

from dishka import Provider, Scope, provide
from dotenv import load_dotenv
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.application.protocols.date_time import DateTimeProcessor
from app.infrastructure.authentication.jwt_settings import JWTSettings
from app.infrastructure.persistence.database_config import DatabaseConfig
from app.infrastructure.persistence.date_time_config import (
    SystemDateTimeProvider,
    Timezone,
)
from app.infrastructure.persistence.redis_config import RedisSettings
from app.infrastructure.settings import Settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENV_FILE = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_FILE)


class SqlalchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self) -> DatabaseConfig:
        return DatabaseConfig.from_env()

    @provide(scope=Scope.APP)
    def provide_engine(self, config: DatabaseConfig) -> AsyncEngine:
        return create_async_engine(config.db_uri)

    @provide(scope=Scope.APP)
    def provide_sessionmaker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(self, sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session


class SettingsProvider(Provider):
    @provide(scope=Scope.APP, provides=JWTSettings)
    async def jwt_settings(self) -> JWTSettings:
        return JWTSettings(
            secret=os.environ.get("SECRET_KEY", default="useless-secret-key"),
            expires_in=int(os.environ.get("EXPIRE_IN")),
            algorithm=os.environ.get("ALGORITHM"),
        )

    @provide(scope=Scope.APP, provides=RedisSettings)
    async def provide_redis_settings(self) -> RedisSettings:
        return RedisSettings(host="localhost", port=6379)

    @provide(scope=Scope.APP, provides=Settings)
    async def main_settings(
        self, db_config: DatabaseConfig, jwt_config: JWTSettings, redis_config: RedisSettings
    ) -> Settings:
        return Settings(db=db_config, jwt=jwt_config, redis=redis_config)


class DateTimeProvider(Provider):
    @provide(scope=Scope.APP, provides=DateTimeProcessor)
    async def provide_date_time_processor(self) -> DateTimeProcessor:
        return SystemDateTimeProvider(Timezone.UTC)
