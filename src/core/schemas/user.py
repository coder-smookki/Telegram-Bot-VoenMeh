from core.schemas.base import BaseDTO
from core.schemas.role import RoleDTO


class UserDTO(BaseDTO):
    id: int
    user_id: int
    name: str | None
    role: list[RoleDTO]