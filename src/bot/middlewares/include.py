from aiogram import Bot, Dispatcher
from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from structlog.typing import FilteringBoundLogger

from .outer.answer import CallbackAnswerMiddleware
from .outer.logging import LoggingMiddleware
from .outer.repository import RepositoryMiddleware
from .outer.throttling import ThrottlingMiddleware
from .request.retry import RetryRequestMiddleware


def include_global_middlewares(
    bot: Bot,
    dp: Dispatcher,
    aiohttp_session: ClientSession,
    session_maker: async_sessionmaker[AsyncSession],
    logger: FilteringBoundLogger,
) -> None:
    """Регистрация мидлварей в боте и диспетчере."""
    bot.session.middleware(RetryRequestMiddleware())

    dp.message.outer_middleware(LoggingMiddleware(logger))
    dp.callback_query.outer_middleware(LoggingMiddleware(logger))

    dp.callback_query.outer_middleware(CallbackAnswerMiddleware())

    dp.message.outer_middleware(ThrottlingMiddleware())
    dp.callback_query.outer_middleware(ThrottlingMiddleware())

    dp.message.outer_middleware(RepositoryMiddleware(session_maker))
    dp.callback_query.outer_middleware(RepositoryMiddleware(session_maker))
    