import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.role import Role
from core.schemas.role import RoleDTO


class RoleRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_role_by_id(self, role_id: int) -> RoleDTO | None:
        query = sa.select(Role).where(Role.id == role_id)
        scalar: Role | None = await self._session.scalar(query)
        return RoleDTO.model_validate(scalar) if scalar is not None else None

    async def get_role_by_name(self, role_name: str) -> RoleDTO | None:
        query = sa.select(Role).where(Role.role == role_name)
        scalar: Role | None = await self._session.scalar(query)
        return RoleDTO.model_validate(scalar) if scalar is not None else None