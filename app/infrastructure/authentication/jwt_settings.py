from dataclasses import dataclass, field


@dataclass(frozen=True)
class JWTSettings:
    secret: str
    expires_in: int = field(default=10)
    algorithm: str = field(default="HS256")
