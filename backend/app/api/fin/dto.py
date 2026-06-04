from typing import Optional

from app.utils.base_dto import BaseEntityDto

class ExpenditureCreateDto(BaseEntityDto):
    category: str
    amount: float
    approved_by: Optional[int] = None
    description: Optional[str] = None

class ExpenditureUpdateDto(BaseEntityDto):
    category: Optional[str] = None
    amount: Optional[float] = None
    approved_by: Optional[int] = None
    description: Optional[str] = None
class ExpenditureOutDto(BaseEntityDto):
    category: str
    amount: float
    approved_by: Optional[int] = None
    description: Optional[str] = None
