from fastapi import APIRouter

from app.api.bbs.comment.dto import SncCommentCreateDto
from app.api.bbs.comment.mapper import CommentMapper
from app.api.bbs.comment.model import BbsComment
from app.api.deps import SessionDep
from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/comment", tags=["comment"])

@router.get("/page", response_model=Result[PageDto[SncCommentCreateDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = CommentMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)

@router.get("/{id}", response_model=Result[SncCommentCreateDto])
def get_by_id(session: SessionDep, id: int):
    comment = session.get(BbsComment, id)
    return Result.ok(data=comment)

@router.post("/add", response_model=Result)
def add(session: SessionDep, comment: SncCommentCreateDto):
    """
    用户回复
    """
    pass

@router.post("/delete", response_model=Result)
def delete(session: SessionDep, id: int):
    """
    删帖
    """
    pass