from fastapi import APIRouter

from app.api.sys import router as sys_router
from app.api.snc import router as snc_router
from app.api.bbs import router as bbs_router
from app.api.static.router import router as static_router

api_router = APIRouter()
api_router.include_router(sys_router)
api_router.include_router(snc_router)
api_router.include_router(bbs_router)
api_router.include_router(static_router)