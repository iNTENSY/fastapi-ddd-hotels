from app.domain.common.errors import DomainError


class BookingAlreadyExistError(DomainError):
    def __init__(self):
        super().__init__(message="Booking already exist")
