from sqlalchemy import BigInteger, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models import Role
from database.models.base import AlchemyBaseModel


class User(AlchemyBaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
    )
    nickname: Mapped[str | None] = mapped_column(
        String(128),
        default=None,
        nullable=True,
    )
    role: Mapped[list["Role"]] = relationship(
        secondary="users_roles",
        lazy="selectin",
        default="User"
    )