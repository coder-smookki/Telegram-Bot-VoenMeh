from pydantic import BaseModel


class CurrendUser(BaseModel):
    tg_username: str
    name: str

def get_current_user(session) -> CurrendUser:
    ...