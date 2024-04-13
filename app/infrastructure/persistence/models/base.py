import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column, DeclarativeBase


intpk = Annotated[int, mapped_column(primary_key=True, index=True, nullable=False)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=True)]


class Base(DeclarativeBase):
    pass
