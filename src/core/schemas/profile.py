from core.schemas.base import BaseDTO


class ProfileDTO(BaseDTO):
    id: int
    user_id: int
    name: str
    age: int
    description: str
    photo: str
