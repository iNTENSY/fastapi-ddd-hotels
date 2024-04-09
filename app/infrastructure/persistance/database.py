from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseSettings:
    database: str
    user: str
    password: str
    host: str
    port: int


    @property
    def uri(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
