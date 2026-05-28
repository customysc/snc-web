from fastapi import APIRouter

from app.api.xware.model import XWAttendance
from app.api.xware.attendance.dto import XWAttendanceDto
from app.api.xware.attendance.mapper import AttendanceMapper
from app.api.deps import SessionDep
from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/attendance", tags=["xware-attendance"])


@router.get("/page", response_model=Result[PageDto[XWAttendanceDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = AttendanceMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)


@router.get("/{id}", response_model=Result[XWAttendanceDto])
def get_by_id(session: SessionDep, id: int):
    attendance = session.get(XWAttendance, id)
    return Result.ok(data=attendance)


@router.post("/add", response_model=Result)
def add(session: SessionDep, dto: XWAttendanceDto):
    attendance = XWAttendance(**dto.model_dump(exclude_unset=True))
    session.add(attendance)
    session.commit()
    session.refresh(attendance)
    return Result.ok(data=attendance.id)


@router.post("/update", response_model=Result)
def update(session: SessionDep, dto: XWAttendanceDto):
    attendance = session.get(XWAttendance, dto.id)
    if not attendance:
        return Result.fail(msg="考勤记录不存在")
    for key, value in dto.model_dump(exclude_unset=True).items():
        setattr(attendance, key, value)
    session.commit()
    return Result.ok()


@router.post("/delete", response_model=Result)
def delete(session: SessionDep, id: int):
    attendance = session.get(XWAttendance, id)
    if not attendance:
        return Result.fail(msg="考勤记录不存在")
    session.delete(attendance)
    session.commit()
    return Result.ok()
