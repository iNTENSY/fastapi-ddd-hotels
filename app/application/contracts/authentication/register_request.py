from dataclasses import dataclass


@dataclass(frozen=True)
class RegisterRequest:
    email: str
    password: str
