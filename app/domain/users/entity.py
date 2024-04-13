from dataclasses import dataclass


@dataclass
class Users:
    id: int
    email: str
    hashed_password: str
