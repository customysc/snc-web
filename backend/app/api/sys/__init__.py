from fastapi import APIRouter

from app.api.sys.user.router import router as user_router
from app.api.sys.login.router import router as login_router

router = APIRouter(prefix="/sys")
router.include_router(user_router)
router.include_router(login_router)