import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class AuthResponse:
    id: uuid.UUID
    email: str
