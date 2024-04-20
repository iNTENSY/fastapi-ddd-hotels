from dataclasses import dataclass

from app.infrastructure.authentication.jwt_settings import JWTSettings
from app.infrastructure.persistence.database_config import DatabaseConfig
from app.infrastructure.persistence.redis_config import RedisSettings


@dataclass(frozen=True)
class Settings:
    db: DatabaseConfig
    jwt: JWTSettings
    redis: RedisSettings
