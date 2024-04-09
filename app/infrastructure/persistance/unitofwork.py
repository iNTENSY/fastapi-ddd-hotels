from psycopg import AsyncConnection

from app.application.protocols.unitofwork import IUnitOfWork


class UnitOfWorkImp(IUnitOfWork):
    __slots__ = ("connection",)

    def __init__(self, connection: AsyncConnection) -> None:
        self._connection = connection

    async def commit(self) -> None:
        await self._connection.commit()

    async def rollback(self) -> None:
        await self._connection.rollback()
