import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.profile import Profile
from core.schemas.profile import ProfileDTO


class ProfileRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_profile_by_id(self, profile_id: int) -> ProfileDTO | None:
        query = sa.select(Profile).where(Profile.id == profile_id)
        scalar: Profile | None = await self._session.scalar(query)
        return ProfileDTO.model_validate(scalar) if scalar is not None else None

    async def create_profile(self, profile_data: ProfileDTO) -> None:
        self._session.add(profile_data)
        await self._session.flush()

    async def update_profile(self, profile_id: int, **kwargs) -> None:
        query = sa.update(Profile).where(Profile.user_id == profile_id).values(**kwargs)
        await self._session.execute(query)
        await self._session.flush()