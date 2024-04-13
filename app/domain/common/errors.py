class DomainError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(message, *args)


class DomainValidationError(DomainError):
    pass


# status_code = -1
#     detail: str = "Base HTTPException"
#
#     def __init__(self) -> None:
#         if self.status_code <= -1:
#             raise NotImplementedError("Override base status code")
#         super().__init__(detail=self.detail, status_code=self.status_code)