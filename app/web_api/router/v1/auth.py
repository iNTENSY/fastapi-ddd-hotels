from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute, inject
from fastapi import APIRouter, Depends
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordRequestForm

from app.application.contracts.authentication.authentication_response import (
    AuthResponse,
)
from app.application.contracts.authentication.login_request import LoginRequest
from app.application.contracts.authentication.register_request import RegisterRequest
from app.application.usecase.authentication.login import Login
from app.application.usecase.authentication.register import Register
from app.domain.users.entity import UserEmail, UserId
from app.infrastructure.authentication.jwt_processor import JwtTokenProcessorImp

router = APIRouter(prefix="/auth", tags=["Auth"], route_class=DishkaRoute)


@router.post("/login", response_model=AuthResponse)
@inject
async def login(
    response: Response,
    login_request: Annotated[OAuth2PasswordRequestForm, Depends()],
    interactor: FromDishka[Login],
    token_processor: FromDishka[JwtTokenProcessorImp],
) -> AuthResponse:
    user = await interactor(LoginRequest(email=login_request.username, password=login_request.password))
    token = await token_processor.generate_token(UserId(user.id), UserEmail(user.email))
    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
    return user


@router.post("/register", response_model=AuthResponse)
@inject
async def register(request: RegisterRequest, interactor: FromDishka[Register]) -> AuthResponse:
    return await interactor(request)


@router.post("/logout")
@inject
async def logout(response: Response) -> dict[str, str]:
    response.delete_cookie(key="access_token")
    return {"message": "Logout successfully"}
