from fastapi import APIRouter

from app.api.bbs.thread.router import router as thread_router
from app.api.bbs.post.router import router as post_router
from app.api.bbs.comment.router import router as comment_router

router = APIRouter(prefix="/bbs")
router.include_router(thread_router)
router.include_router(post_router)
router.include_router(comment_router)