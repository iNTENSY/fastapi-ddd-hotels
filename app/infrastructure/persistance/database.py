import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

logger = logging.getLogger(__name__)


class Database:

    def __init__(self, db_url: str) -> None:
        self._engine = create_async_engine(url=db_url)
        self.__session_factory = async_sessionmaker(bind=self._engine, class_=AsyncSession, expire_on_commit=False)

    @property
    async def session(self):
        async with self.__session_factory() as session:
            yield session
