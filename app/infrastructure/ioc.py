from dishka import provide, Scope, Provider, AsyncContainer, make_async_container

from app.application.protocols.unitofwork import IUnitOfWork
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase
from app.infrastructure.persistance.database import Database
from app.infrastructure.persistance.unitofwork import UnitOfWork
from app.infrastructure.settings import POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT, POSTGRES_DB


class UseCase(Provider):
    scope = Scope.REQUEST

    get_hotels = provide(GetHotelsUseCase)


def create_container() -> AsyncContainer:
    return make_async_container(
        UseCase()
    )
