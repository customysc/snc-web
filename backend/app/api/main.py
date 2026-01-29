from fastapi import APIRouter

from app.api.sys import router as sys_router
from app.api.snc import router as snc_router

api_router = APIRouter()
api_router.include_router(sys_router)
api_router.include_router(snc_router)