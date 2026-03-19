from fastapi import APIRouter

from app.api.iv.interview.router import router as interview_router

router = APIRouter(prefix="/iv")
router.include_router(interview_router)