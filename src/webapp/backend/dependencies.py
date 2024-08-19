from pydantic import BaseModel


class CurrendUser(BaseModel):
    id: int
    tg_username: str
    name: str

def get_current_user(session) -> CurrendUser:
    ...