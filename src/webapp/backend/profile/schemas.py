from datetime import date

from pydantic import BaseModel


class ProfileForDatingScheme(BaseModel):
    id: int
    tg_username: str
    name: str
    birth_date: date
    gender: str # man/woman