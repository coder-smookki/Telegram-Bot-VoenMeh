import os
from functools import lru_cache

from pydantic import BaseModel


class DBSettings(BaseModel):
    """Настройки подключения к базе данных."""

    host: str
    host_port: int
    db: str
    user: str
    password: str


class BotSettings(BaseModel):
    """Настройки телеграм-бота."""

    token: str


class Settings(BaseModel):
    """Сборник настроек :)."""

    db: DBSettings
    bot: BotSettings

@lru_cache
def get_settings() -> Settings:
    """
    Создание настроек из переменных среды.

    :return: Настройки.
    """
    db = DBSettings(
        host=os.environ["POSTGRES_HOST"],
        host_port=int(os.environ["POSTGRES_HOST_PORT"]),
        db=os.environ["POSTGRES_DB_NAME"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )
    bot = BotSettings(
        token=os.environ["BOT_TOKEN"],
    )

    return Settings(db=db, bot=bot)