from fastapi import APIRouter

from app.api.xware.order.router import router as order_router
from app.api.xware.attendance.router import router as attendance_router

router = APIRouter(prefix="/xware")
router.include_router(order_router)
router.include_router(attendance_router)
