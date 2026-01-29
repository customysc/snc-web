from typing import Generic, TypeVar, Type

from sqlalchemy import select, func

from app.api.deps import SessionDep
from app.api.sys.user.model import SysUser
from app.utils.page_dto import PageDto

T = TypeVar('T')

class BaseMapper(Generic[T]):
    model = Type[T]

    @classmethod
    def page(cls, session: SessionDep, current_page: int = 1, page_size: int = 20):
        total_stmt = select(func.count()).select_from(cls.model)
        total: int = session.execute(total_stmt).scalar() or 0

        stmt = select(cls.model).order_by(cls.model.id).offset((current_page - 1) * page_size).limit(page_size)
        items = session.scalars(stmt).all()
        pages = (total + page_size - 1) // page_size if page_size else 0
        return PageDto(
            records=items,
            current=current_page,
            size=page_size,
            pages=pages,
            total=total,
        )

