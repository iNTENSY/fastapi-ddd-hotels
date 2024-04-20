from dataclasses import dataclass


@dataclass(frozen=True)
class RedisSettings:
    host: str
    port: int

    @property
    def url(self) -> str:
        return f"redis://{self.host}:{self.port}"
