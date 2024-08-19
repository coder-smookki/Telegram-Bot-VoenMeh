"""View-часть, передающая события в logic-часть."""

from aiogram import Dispatcher

from handlers import errors
from handlers.client import cancel_state_router, client_router

__all__ = ("include_routers",)


def include_routers(dp: "Dispatcher") -> None:
    """Включение роутов в главный dispatcher."""
    dp.include_routers(
        client_router,
        cancel_state_router,
        errors.router,
    )