from psycopg import AsyncConnection
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.protocols.unitofwork import IUnitOfWork


class UnitOfWorkImp(IUnitOfWork):
    __slots__ = ("connection",)

    def __init__(self, connection: AsyncSession) -> None:
        self.connection = connection

    async def commit(self) -> None:
        await self.connection.commit()

    async def rollback(self) -> None:
        await self.connection.rollback()
