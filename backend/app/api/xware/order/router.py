from fastapi import APIRouter
from sqlalchemy import select, distinct

from app.api.xware.model import XWOrder, XWOrderUser
from app.api.xware.order.dto import XWOrderDto
from app.api.xware.order.mapper import OrderMapper
from app.api.deps import SessionDep
from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/order", tags=["xware-order"])


@router.get("/page", response_model=Result[PageDto[XWOrderDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = OrderMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)


@router.get("/{id}", response_model=Result[XWOrderDto])
def get_by_id(session: SessionDep, id: int):
    order = session.get(XWOrder, id)
    return Result.ok(data=order)


@router.post("/add", response_model=Result)
def add(session: SessionDep, dto: XWOrderDto):
    order = XWOrder(**dto.model_dump(exclude_unset=True))
    session.add(order)
    session.commit()
    session.refresh(order)
    return Result.ok(data=order.id)


@router.post("/update", response_model=Result)
def update(session: SessionDep, dto: XWOrderDto):
    order = session.get(XWOrder, dto.id)
    if not order:
        return Result.fail(msg="工单不存在")
    for key, value in dto.model_dump(exclude_unset=True).items():
        setattr(order, key, value)
    session.commit()
    return Result.ok()


@router.post("/delete", response_model=Result)
def delete(session: SessionDep, id: int):
    order = session.get(XWOrder, id)
    if not order:
        return Result.fail(msg="工单不存在")
    session.delete(order)
    session.commit()
    return Result.ok()


@router.get("/suggestions", response_model=Result)
def suggestions(session: SessionDep, field: str):
    column_map = {
        "name": XWOrder.name,
        "student_no": XWOrder.student_no,
        "department": XWOrder.department,
        "computer": XWOrder.computer,
    }
    col = column_map.get(field)
    if not col:
        return Result.fail(msg="不支持的字段")
    stmt = select(distinct(col)).where(col.isnot(None)).limit(100)
    values = [row for row in session.scalars(stmt).all() if row]
    return Result.ok(data=values)

