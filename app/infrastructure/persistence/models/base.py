import datetime
import uuid
from typing import Annotated

from sqlalchemy import text, UUID
from sqlalchemy.orm import mapped_column, DeclarativeBase


intpk = Annotated[int, mapped_column(primary_key=True, index=True, nullable=False)]
uuidpk = Annotated[uuid.uuid4, mapped_column(UUID(as_uuid=True), primary_key=True, index=True, unique=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=True)]


class Base(DeclarativeBase):
    pass
