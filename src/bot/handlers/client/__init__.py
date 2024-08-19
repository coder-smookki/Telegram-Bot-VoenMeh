from aiogram import Router

from .start import handlers as start_handlers

client_router = Router()

client_router.include_routers(
    start_handlers.router,
)

__all__ = (
    "client_router",
)