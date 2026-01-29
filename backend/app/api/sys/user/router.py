from typing import List

from fastapi import APIRouter
from sqlalchemy import select, func

from app.api.deps import SessionDep
from app.api.sys.user.dto import SysUserReadDto, SysUserCreateDto
from app.api.sys.user.mapper import SysUserMapper
from app.api.sys.user.model import SysUser
from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/page", response_model=Result[PageDto[SysUserReadDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = SysUserMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)

@router.get("/listAll", response_model=Result[List[SysUserReadDto]])
def list_all(session: SessionDep):
    stmt = select(SysUser)
    users = session.scalars(stmt).all()
    return Result.ok(data=users)

@router.post("/add", response_model=Result)
def add(session: SessionDep, user: SysUserCreateDto):
    data = user.model_dump()
    db_user = SysUser(**data)
    session.add(db_user)
    session.commit()
    return Result.ok(msg="添加成功！")

