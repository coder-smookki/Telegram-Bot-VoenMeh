import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Notifie
from core.schemas.notifie import NotifieDTO

from datetime import datetime


class NotifyRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save_notifie(
        self,
        user_id: int,
        chat_id: int,
        message_id: int,
        text: str,
        time_send: datetime,
    ) -> NotifieDTO:
        notify = Notifie(
            user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            text=text,
            time_send=time_send,
        )
        self._session.add(notify)
        await self._session.flush()
        return NotifieDTO.model_validate(notify)

    async def get_notifies(self, limit: int = 100) -> list[NotifieDTO]:
        query = (
            sa.select(Notifie).order_by(Notifie.is_readed, Notifie.id.desc()).limit(limit)
        )
        result = await self._session.execute(query)
        return [NotifieDTO.model_validate(notify) for notify in result.scalars()]

    async def read_notifie(self, notify_id: int) -> None:
        query = (
            sa.update(Notifie).where(Notifie.id == notify_id).values(is_readed=True)
        )
        await self._session.execute(query)
        await self._session.flush()