from dataclasses import dataclass, field


@dataclass(frozen=True)
class GetUserListRequest:
    limit: int = field(default=20)
    offset: int = field(default=0)


@dataclass(frozen=True)
class GetUserRequest:
    id: int = field(default=0)
