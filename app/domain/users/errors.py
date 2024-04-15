from app.domain.common.errors import DomainError


class InvalidTokenError(DomainError):
    def __init__(self):
        super().__init__(message="Invalid token")


class UserNotFoundError(DomainError):
    def __init__(self):
        super().__init__(message="User not found")


class InvalidUserDataError(DomainError):
    def __init__(self):
        super().__init__(message="Invalid user data")
