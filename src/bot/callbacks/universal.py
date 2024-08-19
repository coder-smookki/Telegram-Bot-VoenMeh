from aiogram.filters.callback_data import CallbackData


class OpenMenu(CallbackData, prefix="open_menu"):
    """Фабрика для открытия разных меню бота."""

    menu: str
    date: str | None = None
