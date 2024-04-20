from app.domain.common.errors import DomainError


class RoomNotFoundError(DomainError):
    def __init__(self):
        super().__init__(message="Room not found in this hotel")
