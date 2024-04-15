from app.domain.common.errors import DomainError


class InvalidTokenError(DomainError):
    def __init__(self):
        super().__init__(message="Invalid token")