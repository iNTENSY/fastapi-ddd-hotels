from dataclasses import dataclass


@dataclass
class RegisterRequest:
    email: str
    password: str
