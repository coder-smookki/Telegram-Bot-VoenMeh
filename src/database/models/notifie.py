from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import AlchemyBaseModel


class Notifie(AlchemyBaseModel):
    __tablename__ = "notifie"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    chat_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    message_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    text: Mapped[str] = mapped_column(
        String(1024),
        nullable=False,
    )
    time_send: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False
    )