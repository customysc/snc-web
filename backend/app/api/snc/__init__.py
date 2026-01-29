from fastapi import APIRouter

from app.api.snc.banner.router import router as banner_router

router = APIRouter(prefix="/snc")
router.include_router(banner_router)