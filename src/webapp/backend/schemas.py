from datetime import date

from pydantic import BaseModel


class RegisterUserScheme(BaseModel):
    tg_username: str
    name: str
    birth_date: date
    gender: str # man/woman
    interest_gender:  str # man/woman/all


class UpdateUserScheme(BaseModel):
    name: str
    birth_date: date
    gender: str # man/woman
    interest_gender:  str # man/woman/all


class ProfileForDatingScheme(BaseModel):
    id: int
    tg_username: str
    name: str
    birth_date: date
    gender: str # man/woman