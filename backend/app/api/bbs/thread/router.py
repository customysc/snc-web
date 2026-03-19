from fastapi import APIRouter

from app.api.bbs.thread.dto import SncThreadCreateDto
from app.api.bbs.thread.mapper import ThreadMapper
from app.api.bbs.model import BbsThread
from app.api.deps import SessionDep
from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/thread", tags=["thread"])

@router.get("/page", response_model=Result[PageDto[SncThreadCreateDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = ThreadMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)

@router.get("/{id}", response_model=Result[SncThreadCreateDto])
def get_by_id(session: SessionDep, id: int):
    thread = session.get(BbsThread, id)
    return Result.ok(data=thread)

@router.post("/add", response_model=Result)
def add(session: SessionDep, thread: SncThreadCreateDto):
    """
    用户发帖
    """
    pass

@router.post("/delete", response_model=Result)
def delete(session: SessionDep, thread_id: int):
    """
    删帖
    """
    pass