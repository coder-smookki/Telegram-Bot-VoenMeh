import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from sqlalchemy.orm import close_all_sessions

from handlers.include import include_routers
from utils.enums import SlashCommand
from settings import Settings


async def on_startup(bot: Bot) -> None:
    user = await bot.me()
    logging.info(
        "Start polling for bot @%s id=%d - %r",
        user.username,
        user.id,
        user.full_name,
    )


async def on_shutdown(bot: Bot) -> None:
    close_all_sessions()

    user = await bot.me()
    logging.info(
        "Stop polling for bot @%s id=%d - %r",
        user.username,
        user.id,
        user.full_name,
    )


async def set_commands(bot: Bot) -> bool:
    commands: dict[str, str] = {
        SlashCommand.START: "Старт",
        SlashCommand.HELP: "Помощь",
    }

    return await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in commands.items()
        ],
        scope=BotCommandScopeAllPrivateChats(),
    )


def create_dispatcher(
    settings: Settings,
) -> Dispatcher:
    """Создаёт диспетчер и регистрирует все роуты."""
    dp = Dispatcher(
        settings=settings,
        name="__main__",
    )

    include_routers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    return dp


async def create_bot(bot_token: str, parse_mode: str = ParseMode.HTML) -> Bot:
    """Создаёт бота и устанавливает ему команды."""
    bot = Bot(
        token=bot_token,
        parse_mode=parse_mode,
        disable_web_page_preview=True,
    )
    await set_commands(bot)

    return bot