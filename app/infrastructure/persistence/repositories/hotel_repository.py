from typing import Sequence, Any

from sqlalchemy import select, delete, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.hotels.entity import Hotels
from app.domain.hotels.repository import IHotelRepository


class HotelRepositoryImp(IHotelRepository):
    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def create(self, data: dict) -> Hotels:
        """Создание в БД."""
        statement = insert(Hotels).values(**data).returning(Hotels)
        result = (await self.connection.execute(statement)).scalar_one()
        return result

    async def find_all(self, limit: int, offset: int):
        """Выбрать все отели из БД."""
        statement = select(Hotels).limit(limit).offset(offset)
        result = (await self.connection.execute(statement)).scalars().all()
        return result

    async def filter_by(self, **parameters) -> Sequence[Hotels]:
        """Выбрать отели из БД с определенными параметрами."""
        statement = select(Hotels).filter_by(**parameters)
        result = (await self.connection.execute(statement)).scalars().all()
        return result

    async def delete(self, **parameters) -> Hotels:
        """Удалить отель по уникальному идентификатору из базы данных"""
        statement = delete(Hotels).filter_by(**parameters).returning(Hotels)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        return result

    async def update(self, data: dict, id: int) -> Hotels:
        """Обновить отель по уникальному идентификатору"""
        statement = update(Hotels).where(Hotels.id == id).values(**data).returning(Hotels)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        return result
