from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from app.api.deps import SessionDep
from app.api.snc.SncConstant import SncConstant
from app.api.snc.banner.dto import SncBannerReadDto, SncBannerCreateDto
from app.api.snc.banner.mapper import BannerMapper
from app.api.snc.banner.model import SncBanner
from app.utils.page_dto import PageDto
from app.utils.result import Result

router = APIRouter(prefix="/banner", tags=["banner"])

@router.get("/published", response_model=Result[List[SncBannerReadDto]])
def published(session: SessionDep):
    stmt = select(SncBanner).where(SncBanner.status==SncConstant.BANNER_STATUS_PUBLISHED).order_by(SncBanner.sort_order)
    banners = session.scalars(stmt).all()
    return Result.ok(data=banners)

@router.get("/page", response_model=Result[PageDto[SncBannerReadDto]])
def page(session: SessionDep, current_page: int = 1, page_size: int = 20):
    result = BannerMapper.page(session=session, current_page=current_page, page_size=page_size)
    return Result.ok(data=result)

@router.post("/add", response_model=Result)
def add(session: SessionDep, banner: SncBannerCreateDto):
    data = banner.model_dump(exclude_unset=True)
    db_banner = SncBanner(**data)
    session.add(db_banner)
    session.commit()
    return Result.ok(msg="添加成功！")

@router.post("/update", response_model=Result)
def update(session: SessionDep, banner: SncBannerCreateDto):
    db_banner = session.get(SncBanner, banner.id)
    if db_banner is None:
        return Result.fail(msg="Banner 不存在")

    update_data = banner.model_dump(exclude_unset=True)
    for k, v in update_data.items():
        setattr(db_banner, k, v)
    session.commit()
    return Result.ok(msg="更新成功！")