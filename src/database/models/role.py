from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import AlchemyBaseModel


class Role(AlchemyBaseModel):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False,
    )
    role: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )