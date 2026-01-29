from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base_entity import BaseEntity


class SncBanner(BaseEntity):
    __tablename__ = "snc_banner"

    image_url: Mapped[Optional[str]] = mapped_column(String(255))
    target_url: Mapped[Optional[str]] = mapped_column(String(255))
    target_type: Mapped[Optional[str]] = mapped_column(String(64))

    sort_order: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[str]] = mapped_column(String(64))

    start_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    end_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
