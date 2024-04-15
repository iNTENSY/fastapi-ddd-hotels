from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteUserRequest:
    id: int