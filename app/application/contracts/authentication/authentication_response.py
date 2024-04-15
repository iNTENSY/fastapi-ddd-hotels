from dataclasses import dataclass


@dataclass(frozen=True)
class AuthResponse:
    id: int
    email: str
