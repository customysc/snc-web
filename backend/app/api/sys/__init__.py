from fastapi import APIRouter

from app.api.sys.user.router import router as user_router

router = APIRouter(prefix="/sys")
router.include_router(user_router)