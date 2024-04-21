import uuid
from typing import Sequence

from sqlalchemy import select, delete, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository
from app.infrastructure.persistence.mappers.hotel_mapper import hotel_from_dict_to_entity
from app.infrastructure.persistence.models import HotelsModel


class HotelRepositoryImp(IHotelRepository):
    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def create(self, domain: Hotels) -> None:
        """Создание в БД."""
        statement = insert(HotelsModel).values(await domain.raw())
        await self.connection.execute(statement)


    async def find_all(self, limit: int, offset: int) -> list[Hotels]:
        """Выбрать все отели из БД."""
        statement = select(HotelsModel).limit(limit).offset(offset)
        result = (await self.connection.execute(statement)).scalars().all()
        return [await hotel_from_dict_to_entity(vars(hotel)) for hotel in result]

    async def filter_by(self, **parameters) -> list[Hotels]:
        """Выбрать отели из БД с определенными параметрами."""
        statement = select(HotelsModel).filter_by(**parameters)
        result = (await self.connection.execute(statement)).scalars().all()
        return [await hotel_from_dict_to_entity(hotel.__dict__) for hotel in result]

    async def delete(self, **parameters) -> Hotels | None:
        """Удалить отель по уникальному идентификатору из базы данных"""
        statement = delete(HotelsModel).filter_by(**parameters).returning(HotelsModel)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await hotel_from_dict_to_entity(result.__dict__)

    async def update(self, data: dict, id: uuid.UUID) -> Hotels | None:
        """Обновить отель по уникальному идентификатору"""
        statement = update(HotelsModel).where(HotelsModel.id == id).values(**data).returning(HotelsModel)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await hotel_from_dict_to_entity(result.__dict__)
