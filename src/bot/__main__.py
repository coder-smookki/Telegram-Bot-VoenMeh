import asyncio
import contextlib

import aiohttp

from factory import create_bot, create_dispatcher
from middlewares import include_global_middlewares
from utils.logging import setup_logger
from database.session import database_init
from settings import get_settings


async def main() -> None:
    logger = setup_logger()

    settings = get_settings()
    session_maker = await database_init(settings.db)

    bot = await create_bot(settings.bot.token)
    dp = create_dispatcher(settings)

    async with aiohttp.ClientSession() as session:
        include_global_middlewares(bot, dp, settings, session, session_maker, logger)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())