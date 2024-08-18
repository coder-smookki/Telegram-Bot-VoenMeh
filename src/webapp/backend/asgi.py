from typing import Annotated

from fastapi import FastAPI, UploadFile 

from backend.schemas import (
    RegisterUserScheme, UpdateUserScheme,
    ProfileForDatingScheme,)
from backend.dependencies import get_current_user, CurrendUser

app = FastAPI()

"""
тут не решен вопрос с откатом просмотренных анкет, 
создать поле история?
"""


@app.post("/register_user")
async def register_user(
        user_data: RegisterUserScheme, 
        user_image: UploadFile, 
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    ...


@app.put("user")
async def update_user_data(
        user_data: UpdateUserScheme,
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    ...


@app.put("user_image")
async def update_user_image(
        user_image: UploadFile, 
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> 200:
    ...


@app.get("/profile_for_dating")
async def get_profile_for_dating(
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> ProfileForDatingScheme:
    ...


@app.post("/reaction_to_profile") # если прислал, значит одобрил
async def reaction_to_profile(
        profile_id: int,
        current_user: Annotated[CurrendUser, get_current_user],
    ) -> 200:
    ...


@app.get("/profiles_who_like_current_user") # патамушта
async def get_profiles_who_like_current_user(
        current_user: Annotated[CurrendUser, get_current_user]
    ) -> list[ProfileForDatingScheme]:
    ...


@app.post("/reaction_to_reaction") # если прислал, значит одобрил
async def reaction_to_reaction(
        profile_id: int,
        current_user: Annotated[CurrendUser, get_current_user],
    ): # я хер знает что возвращать, профиль или создать для этого отдельный метод
    ...