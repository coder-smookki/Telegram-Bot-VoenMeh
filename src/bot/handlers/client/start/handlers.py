from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from middlewares.inner.save_user import SaveUpdateUserMiddleware
from database.repositories.repository import Repository
from utils.enums import TextCommand, SlashCommand


router = Router(name=__name__)
router.message.middleware(SaveUpdateUserMiddleware())


@router.message(F.text == TextCommand.START, StateFilter("*"))
@router.message(CommandStart(), StateFilter("*"))
async def start_handler(
    message: "Message",
    repo: "Repository",
    state: "FSMContext",
) -> None:
    """Обработчик команды "/start"."""
    await state.clear()
    await message.reply(
        text="START_TEXT",
    )

@router.message(F.text == TextCommand.HELP)
@router.message(Command(SlashCommand.HELP))
async def help_handler(message: "Message") -> None:
    """Обработчик команды "/help"."""
    await message.reply(text="HELP_TEXT")