from sqlalchemy import select, delete, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.rooms.entity import Rooms
from app.domain.rooms.repository import IRoomRepository
from app.infrastructure.persistence.mappers.room_mapper import room_from_dict_to_entity
from app.infrastructure.persistence.models import RoomsModel


class RoomRepositoryImp(IRoomRepository):
    def __init__(self, connection: AsyncSession):
        self.connection = connection

    async def create(self, data: dict) -> Rooms:
        """Create room in the hotel using hotel_id."""
        statement = insert(RoomsModel).values(**data).returning(RoomsModel)
        result = (await self.connection.execute(statement)).scalar_one()
        return await room_from_dict_to_entity(vars(result))

    async def find_all(self, hotel_id: int, limit: int, offset: int) -> list[Rooms] | None:
        statement = select(RoomsModel).where(RoomsModel.hotel_id == hotel_id).limit(limit).offset(offset)
        result = (await self.connection.execute(statement)).scalars().all()
        return [await room_from_dict_to_entity(room.__dict__) for room in result]

    async def filter_by(self, **parameters) -> list[Rooms]:
        """Выбрать номер из БД с определенными параметрами."""
        statement = select(RoomsModel).filter_by(**parameters)
        result = (await self.connection.execute(statement)).scalars().all()
        return [await room_from_dict_to_entity(room.__dict__) for room in result]

    async def delete(self, **parameters) -> Rooms | None:
        """Удалить номер по уникальному идентификатору из базы данных"""
        statement = delete(RoomsModel).filter_by(**parameters).returning(RoomsModel)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await room_from_dict_to_entity(result.__dict__)

    async def update(self, data: dict, id: int) -> Rooms | None:
        """Обновить номер по уникальному идентификатору"""
        statement = update(RoomsModel).where(RoomsModel.id == id).values(**data).returning(RoomsModel)
        result = (await self.connection.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await room_from_dict_to_entity(result.__dict__)

