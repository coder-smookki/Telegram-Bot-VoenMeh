from typing import Annotated

from fastapi import APIRouter, UploadFile

from backend.user.schemas import RegisterUserScheme, UpdateUserScheme
from backend.dependencies import get_current_user, CurrendUser


router = APIRouter(
    "/user"
)

@router.post("/register")
async def register_user(
        user_data: RegisterUserScheme, 
        user_image: UploadFile, 
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    """Регистрация фронта

    Args:
        user_data (RegisterUserScheme): _description_
        user_image (UploadFile): _description_
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        200: _description_
    """


@router.patch("")
async def update_user(
        user_image: UploadFile | None, 
        user_data: UpdateUserScheme,
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    """Обновление полей юзера

    Args:
        user_data (UpdateUserScheme): _description_
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        200: _description_
    """