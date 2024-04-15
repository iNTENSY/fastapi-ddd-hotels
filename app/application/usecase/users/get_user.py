from app.application.contracts.users.get_user_request import GetUserRequest, GetUserListRequest
from app.application.contracts.users.user_reponse import UserResponse, UserListResponse
from app.application.protocols.interactor import Interactor
from app.domain.users.repository import IUserRepository


class GetUserUseCase(Interactor[GetUserRequest, UserResponse]):
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    async def __call__(self, request: GetUserRequest) -> UserResponse | None:
        user = await self._user_repository.filter_by(id=request.id)
        if not user:
            return None
        return await UserResponse.create(user[0])


class GetUsersUseCase(Interactor[GetUserListRequest, UserListResponse]):
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    async def __call__(self, request: GetUserListRequest) -> UserListResponse:
        users = await self._user_repository.find_all(limit=request.limit, offset=request.offset)
        return await UserListResponse.create(users)
