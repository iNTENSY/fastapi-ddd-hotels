import uuid
from collections.abc import Sequence

from sqlalchemy import delete, select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.common.value_object import DomainValueObject
from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository
from app.infrastructure.persistence.mappers.hotel_mapper import (
    hotel_from_dict_to_entity,
)
from app.infrastructure.persistence.models import HotelsModel


class HotelRepositoryImp(IHotelRepository):
    def __init__(self, connection: AsyncSession):
        self.__connection = connection

    async def create(self, domain: Hotels) -> None:
        """Создание в БД."""
        statement = insert(HotelsModel).values(await domain.raw())
        await self.__connection.execute(statement)

    async def find_all(self, limit: int, offset: int) -> list[Hotels]:
        """Выбрать все отели из БД."""
        statement = select(HotelsModel).limit(limit).offset(offset)
        result = (await self.__connection.execute(statement)).scalars().all()
        return [await hotel_from_dict_to_entity(vars(hotel)) for hotel in result]

    async def filter_by(self, **parameters) -> list[Hotels]:
        """Выбрать отели из БД с определенными параметрами."""
        statement = select(HotelsModel).filter_by(**{key: value_object.value for key, value_object in parameters.items()})
        result = (await self.__connection.execute(statement)).scalars().all()
        return [await hotel_from_dict_to_entity(vars(hotel)) for hotel in result]

    async def delete(self, **parameters) -> Hotels | None:
        """Удалить отель по уникальному идентификатору из базы данных"""
        statement = (
            delete(HotelsModel)
            .filter_by(
                **{key: value_object.value for key, value_object in parameters.items()}
            )
            .returning(HotelsModel))
        result = (await self.__connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await hotel_from_dict_to_entity(vars(result))

    async def update(self, domain: Hotels) -> Hotels | None:
        """Обновить отель по уникальному идентификатору"""
        statement = update(HotelsModel).where(HotelsModel.id == domain.id.value).values(await domain.raw()).returning(HotelsModel)
        result = (await self.__connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await hotel_from_dict_to_entity(vars(result))
