from typing import Any, Optional

from sqlalchemy import String, Text, DECIMAL
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base_entity import BaseEntity

class Expenditure(BaseEntity):
    __tablename__ = "fin_expenditure"

    category: Mapped[Optional[str]] = mapped_column(String(50), nullable=False)
    amount: Mapped[Optional[float]] = mapped_column(DECIMAL[Any](10, 2), nullable=False)
    approved_by: Mapped[Optional[int]] = mapped_column(BIGINT)
    description: Mapped[Optional[str]] = mapped_column(Text)