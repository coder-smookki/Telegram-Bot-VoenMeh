from typing import Annotated

from fastapi import APIRouter

from backend.profile.schemas import ProfileForDatingScheme
from backend.dependencies import get_current_user, CurrendUser


router = APIRouter(
    "/profile"
)



@router.get("/profile_for_dating")
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


@router.post("/reaction_to_profile") # если прислал, значит одобрил
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


@router.get("/profiles_who_like_current_user") # патамушта
async def get_profiles_who_like_current_user(
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> list[ProfileForDatingScheme]:
    """Возвращает профили которые лайкнули текущего пользователя

    Args:
        current_user (Annotated[CurrendUser, get_current_user]): _description_

    Returns:
        list[ProfileForDatingScheme]: _description_
    """


@router.post("/reaction_to_like")
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