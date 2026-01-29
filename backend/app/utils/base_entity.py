from sqlalchemy import Integer, BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import Optional

from app.utils.snowflake import snowflake


class BaseEntity(DeclarativeBase):
    id: Mapped[Optional[int]] = mapped_column(BigInteger, primary_key=True, default=lambda: next(snowflake))
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    updated_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    del_flag: Mapped[Optional[int]] = mapped_column(Integer)
