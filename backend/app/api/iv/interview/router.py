from select import select
from typing import List

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.api.iv.interview.dto import IvInterviewDto
from app.api.iv.interview.mapper import IvInterviewMapper
from app.api.iv.model import IvInterview

from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/banner", tags=["banner"])

@router.get("/page", response_model=Result[PageDto[IvInterviewDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = IvInterviewMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)

@router.get("/listAll", response_model=Result[List[IvInterviewDto]])
def list_all(session: SessionDep):
    stmt = select(IvInterview)
    data = session.scalars(stmt).all()
    return Result.ok(data=data)

@router.post("/add", response_model=Result)
def add(session: SessionDep, banner: IvInterviewDto):
    data = banner.model_dump(exclude_unset=True)
    db_interview = IvInterview(**data)
    session.add(db_interview)
    session.commit()
    return Result.ok(msg="添加成功！")

@router.post("/update", response_model=Result)
def update(session: SessionDep, interview: IvInterviewDto):
    db_interview = session.get(IvInterview, interview.id)
    if db_interview is None:
        return Result.fail(msg="Interview 不存在")

    update_data = interview.model_dump(exclude_unset=True)
    for k, v in update_data.items():
        setattr(db_interview, k, v)
    session.commit()
    return Result.ok(msg="更新成功！")

@router.delete("/delete", response_model=Result)
def delete(session: SessionDep, interview: IvInterviewDto):
    db_interview = session.get(IvInterview, interview.id)
    if db_interview is None:
        return Result.fail(msg="Interview 不存在")
    session.delete(db_interview)
    session.commit()
    return Result.ok(msg="删除成功！")