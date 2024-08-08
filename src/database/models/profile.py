from sqlalchemy import Integer, String, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import AlchemyBaseModel


class Profile(AlchemyBaseModel):
    __tablename__ = "profile"

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
    name: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )
    photo: Mapped[LargeBinary] = mapped_column(
        LargeBinary,
        nullable=False,
    )