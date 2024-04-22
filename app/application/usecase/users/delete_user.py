from app.application.contracts.users.delete_user_request import DeleteUserRequest
from app.application.contracts.users.user_reponse import UserResponse
from app.application.protocols.interactor import Interactor
from app.application.protocols.unitofwork import IUnitOfWork
from app.domain.users.repository import IUserRepository


class DeleteUserUseCase(Interactor[DeleteUserRequest, UserResponse]):
    def __init__(self, uow: IUnitOfWork, user_repository: IUserRepository):
        self.__uow = uow
        self._user_repository = user_repository

    async def __call__(self, request: DeleteUserRequest) -> UserResponse: ...
