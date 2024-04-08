from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.protocols.unitofwork import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    __slots__ = ("connection",)

    def __init__(self, connection: AsyncConnection) -> None:
        self.connection = connection

    async def commit(self) -> None:
        await self.connection.commit()

    async def rollback(self) -> None:
        await self.connection.rollback()
