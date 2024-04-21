from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute, inject
from fastapi import APIRouter, Depends

from app.application.contracts.users.get_user_request import (
    GetUserListRequest,
    GetUserRequest,
)
from app.application.contracts.users.user_reponse import UserListResponse, UserResponse
from app.application.usecase.users.get_user import GetUsersUseCase, GetUserUseCase
from app.domain.users.errors import UserNotFoundError

router = APIRouter(prefix="/users", tags=["Users"], route_class=DishkaRoute)


@router.get(path="/", response_model=UserListResponse)
@inject
async def get_users(
    request: Annotated[GetUserListRequest, Depends()], interactor: FromDishka[GetUsersUseCase]
) -> UserListResponse:
    return await interactor(request)


@router.get(path="/{id}", response_model=UserResponse)
@inject
async def get_user(
    request: Annotated[GetUserRequest, Depends()], interactor: FromDishka[GetUserUseCase]
) -> UserResponse:
    response = await interactor(request)
    if response is None:
        raise UserNotFoundError
    return response
