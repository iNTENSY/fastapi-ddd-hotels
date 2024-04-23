from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from app.domain.common.value_object import DomainValueObject

EntityId = TypeVar("EntityId", bound=DomainValueObject)


@dataclass
class DomainEntity(Generic[EntityId]):
    id: EntityId

    async def raw(self) -> dict[str, Any]:
        return {key: value.value for key, value in vars(self).items()}
