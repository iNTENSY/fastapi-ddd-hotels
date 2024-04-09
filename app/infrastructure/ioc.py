from typing import AsyncGenerator

from dishka import provide, Scope, Provider, AsyncContainer, make_async_container
from psycopg import AsyncConnection
from psycopg.conninfo import conninfo_to_dict
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.application.protocols.unitofwork import IUnitOfWork
from app.application.usecase.hotels.get_hotel import GetHotelsUseCase
from app.domain.hotels.repository import IHotelRepository
from app.infrastructure.persistance.database import DatabaseSettings
from app.infrastructure.persistance.repositories.hotel_repository import HotelRepositoryImp
from app.infrastructure.persistance.unitofwork import UnitOfWorkImp
from app.infrastructure.settings import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT


class DatabaseSettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def db_settings(self) -> DatabaseSettings:
        return DatabaseSettings(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )


class DatabaseConfigurationProvider(Provider):
    @provide(scope=Scope.REQUEST, provides=AsyncConnection)
    async def provide_db_connection(self, db_settings: DatabaseSettings) -> AsyncGenerator[AsyncConnection, None]:
        connection = await AsyncConnection.connect(
            **conninfo_to_dict(db_settings.uri),
        )
        yield connection
        await connection.close()



class DatabaseAdaptersProvider(Provider):
    scope = Scope.REQUEST

    unit_of_work = provide(UnitOfWorkImp, provides=IUnitOfWork)
    hotels_repository = provide(HotelRepositoryImp, provides=IHotelRepository)


class UseCase(Provider):
    scope = Scope.REQUEST

    get_hotels = provide(GetHotelsUseCase)


def create_container() -> AsyncContainer:
    return make_async_container(
        DatabaseConfigurationProvider(),
        DatabaseAdaptersProvider(),
        UseCase()
    )
