from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base_entity import BaseEntity

class BbsThread(BaseEntity):
    __tablename__ = "bbs_thread"

    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    title: Mapped[Optional[str]] = mapped_column(String(255))

    content: Mapped[Optional[str]] = mapped_column(Text)
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    status: Mapped[Optional[str]] = mapped_column(String(64))
