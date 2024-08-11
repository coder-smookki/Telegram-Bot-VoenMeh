from core.schemas.base import BaseDTO

from datetime import datetime

class RoleDTO(BaseDTO):
    id: int
    chat_id: int
    user_id: int
    message_id: int
    text: str
    time_send: datetime