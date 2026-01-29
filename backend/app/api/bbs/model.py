from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, BigInteger, String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base_entity import BaseEntity

class BbsThread(BaseEntity):
    __tablename__ = "bbs_thread"

    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    title: Mapped[Optional[str]] = mapped_column(String(255))

    content: Mapped[Optional[str]] = mapped_column(Text)
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    status: Mapped[Optional[str]] = mapped_column(String(64))


class BbsPost(BaseEntity):
    __tablename__ = "bbs_post"

    thread_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)

    content: Mapped[Optional[str]] = mapped_column(Text)
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    sort_order: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[str]] = mapped_column(String(64))


class BbsComment(BaseEntity):
    __tablename__ = "bbs_comment"

    post_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    parent_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)

    content: Mapped[Optional[str]] = mapped_column(Text)
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    sort_order: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[str]] = mapped_column(String(64))
