from dataclasses import dataclass
from typing import Generic, TypeVar

from app.domain.common.value_object import DomainValueObject


EntityId = TypeVar("EntityId", bound=DomainValueObject)


@dataclass
class DomainEntity(Generic[EntityId]):
    id: EntityId