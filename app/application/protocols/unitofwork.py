from typing import Protocol


class IUnitOfWork(Protocol):
    async def commit(self) -> None: ...

    async def rollback(self) -> None: ...
