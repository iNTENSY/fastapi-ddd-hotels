from app.domain.common.errors import DomainError


class HotelNotFound(DomainError):
    def __init__(self):
        super().__init__(message="The hotel is currently not found")
