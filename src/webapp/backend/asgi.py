from fastapi import FastAPI 

from backend.user import router as user_router
from backend.profile import router as profile_router


"""
+ уведомления через сокеты
"""

app = FastAPI()

app.include_router(user_router)
app.include_router(profile_router)


