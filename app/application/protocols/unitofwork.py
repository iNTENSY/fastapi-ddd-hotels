from typing import Protocol

from app.domain.common.entity import DomainModel


class IUnitOfWork(Protocol):
    async def commit(self) -> None: ...

    async def rollback(self) -> None: ...
