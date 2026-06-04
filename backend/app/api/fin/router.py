from fastapi import APIRouter
from app.api.deps import SessionDep
from app.api.fin.dto import ExpenditureCreateDto, ExpenditureUpdateDto, ExpenditureOutDto
from app.api.fin.mapper import FinMapper
from app.api.fin.model import Expenditure
from app.utils.page_dto import PageDto
from app.utils.result import Result
from sqlalchemy import func

router = APIRouter(prefix="/fin", tags=["financial"])

@router.get("/page", response_model=Result[PageDto[ExpenditureOutDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    """分页获取支出记录列表"""
    result = FinMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)

@router.get("/{id}", response_model=Result[ExpenditureOutDto])
def get_by_id(session: SessionDep, id: int):
    """根据ID获取支出记录详情"""
    expenditure = session.get(Expenditure, id)
    return Result.ok(data=expenditure)

@router.post("/add", response_model=Result[ExpenditureOutDto])
def add(session: SessionDep, exp: ExpenditureCreateDto):
    """新增支出记录"""
    db_exp = Expenditure(**exp.model_dump())
    session.add(db_exp)
    session.commit()
    session.refresh(db_exp)
    return Result.ok(msg="添加成功", data=db_exp)

@router.post("/update", response_model=Result[ExpenditureOutDto])
def update(session: SessionDep, id: int, exp: ExpenditureUpdateDto):
    """更新支出记录"""
    db_exp = session.get(Expenditure, id)
    if not db_exp:
        return Result.fail(msg="记录不存在")
    update_data = exp.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_exp, key, value)
    session.commit()
    session.refresh(db_exp)
    return Result.ok(msg="更新成功", data=db_exp)

@router.post("/delete", response_model=Result)
def delete(session: SessionDep, id: int):
    """删除支出记录"""
    db_exp = session.get(Expenditure, id)
    if not db_exp:
        return Result.fail(msg="记录不存在")
    session.delete(db_exp)
    session.commit()
    return Result.ok(msg="删除成功")

