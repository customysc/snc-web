from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base_entity import BaseEntity


class SncBanner(BaseEntity):
    __tablename__ = "snc_banner"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="名称")
    image_url: Mapped[Optional[str]] = mapped_column(String(255), comment="图片链接")
    target_url: Mapped[Optional[str]] = mapped_column(String(255), comment="跳转链接")
    target_type: Mapped[Optional[str]] = mapped_column(String(64))

    sort_order: Mapped[Optional[int]] = mapped_column(Integer, comment="排序")
    status: Mapped[Optional[str]] = mapped_column(String(64), comment="状态")

    start_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    end_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
