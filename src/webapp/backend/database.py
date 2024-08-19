from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy.orm import DeclarativeBase

from settings import get_settings


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    db_settings = get_settings().db
    db_url = f"postgresql+asyncpg:// \
        {db_settings.user}:{db_settings.password}@ \
        {db_settings.host}:{db_settings.host_port}/{db_settings.db}"
    
    engine = create_async_engine(db_url, echo=True)
    async_session_maker = sessionmaker(
        bind=engine, 
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session_maker() as session:
        yield session