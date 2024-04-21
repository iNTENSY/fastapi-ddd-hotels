import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class GetHotelListRequest:
    limit: int = field(default=20)
    offset: int = field(default=0)


@dataclass(frozen=True)
class GetHotelRequest:
    id: uuid.UUID
