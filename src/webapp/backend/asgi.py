from typing import Annotated

from fastapi import FastAPI, UploadFile 

from backend.schemas import (
    RegisterUserScheme, UpdateUserScheme,
    ProfileForDatingScheme,)
from backend.dependencies import get_current_user, CurrendUser

app = FastAPI()

"""
+ уведомления через сокеты
"""


@app.post("/register_user")
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


@app.put("user")
async def update_user_data(
        user_data: UpdateUserScheme,
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    """Обновление полей юзера (без фотографии)

    Args:
        user_data (UpdateUserScheme): _description_
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        200: _description_
    """


@app.put("user_image")
async def update_user_image(
        user_image: UploadFile, 
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    """Обновление фотографии юзера

    Args:
        user_image (UploadFile): _description_
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        200: _description_
    """
    


@app.get("/profile_for_dating")
async def get_profile_for_dating(
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> ProfileForDatingScheme:
    """Возвращает случайный профиль для знакомства
    подходящий под критерии

    Args:
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        ProfileForDatingScheme: _description_
    """


@app.post("/reaction_to_profile") # если прислал, значит одобрил
async def reaction_to_profile(
        profile_id: int,
        current_user: Annotated[CurrendUser, get_current_user],
    ) -> 200:
    """Означает лайк на профиль
    + уведомления через сокеты

    Args:
        profile_id (int): _description_
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        200: _description_
    """


@app.get("/profiles_who_like_current_user") # патамушта
async def get_profiles_who_like_current_user(
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> list[ProfileForDatingScheme]:
    """Возвращает профили которые лайкнули текущего пользователя

    Args:
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        list[ProfileForDatingScheme]: _description_
    """


@app.post("/reaction_to_like")
async def reaction_to_reaction(
        reaction: str, # approved/not approved
        profile_id: int,
        current_user: Annotated[CurrendUser, get_current_user],
    ): # я хер знает что возвращать, профиль или создать для этого отдельный метод
    """Реакция на лайк, 
    нужно знать реакцию чтобы убрать первую реакцию из уведомлений
    + уведомления через сокеты

    Args:
        profile_id (int): _description_
        current_user (Annotated[CurrendUser, get_current_user]): _description_
    """