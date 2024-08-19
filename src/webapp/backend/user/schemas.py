from datetime import date

from pydantic import BaseModel


class RegisterUserScheme(BaseModel):
    tg_username: str
    name: str
    birth_date: date
    gender: str # man/woman
    interest_gender:  str # man/woman/all


class UpdateUserScheme(BaseModel):
    name: str | None
    birth_date: date | None
    gender: str | None # man/woman
    interest_gender:  str | None # man/woman/all