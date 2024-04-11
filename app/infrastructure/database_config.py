from dataclasses import dataclass

from app.infrastructure.settings import DATABASE_URI


@dataclass(frozen=True)
class DatabaseConfig:
    db_uri: str

    @staticmethod
    def from_env() -> "DatabaseConfig":
        uri = DATABASE_URI

        if not uri:
            raise RuntimeError("Missing DATABASE_URI environment variable")

        return DatabaseConfig(uri)
