from fastapi import APIRouter

from app.api.sys.user import router as user_router
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(user_router.router)