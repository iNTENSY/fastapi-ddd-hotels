from sqlalchemy import select, delete, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.hotels.entity import Hotels
from app.domain.users.entity import Users
from app.domain.users.repository import IUserRepository
from app.infrastructure.persistence.mappers.hotel_mapper import hotel_from_dict_to_entity
from app.infrastructure.persistence.mappers.user_mapper import user_from_dict_to_entity
from app.infrastructure.persistence.models import HotelsModel, UsersModel


class UsersRepositoryImp(IUserRepository):
    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def create(self, data: dict) -> Users:
        """Создание в БД."""
        statement = insert(UsersModel).values(**data).returning(UsersModel)
        result = (await self.connection.execute(statement)).scalar_one()
        return await user_from_dict_to_entity(result.__dict__)

    async def find_all(self, limit: int, offset: int) -> list[Users]:
        """Выбрать всех пользователей из БД."""
        statement = select(UsersModel).limit(limit).offset(offset)
        result = (await self.connection.execute(statement)).scalars().all()
        return [await user_from_dict_to_entity(hotel.__dict__) for hotel in result]

    async def filter_by(self, **parameters) -> list[Users]:
        """Выбрать пользователей из БД с определенными параметрами."""
        statement = select(UsersModel).filter_by(**parameters)
        result = (await self.connection.execute(statement)).scalars().all()
        return [await user_from_dict_to_entity(hotel.__dict__) for hotel in result]

    async def delete(self, **parameters) -> Users | None:
        """Удалить пользователя по уникальному идентификатору из базы данных"""
        statement = delete(UsersModel).filter_by(**parameters).returning(UsersModel)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await user_from_dict_to_entity(result.__dict__)

    async def update(self, data: dict, id: int) -> Users | None:
        """Обновить пользователя по уникальному идентификатору"""
        statement = update(UsersModel).where(UsersModel.id == id).values(**data).returning(UsersModel)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await user_from_dict_to_entity(result.__dict__)
