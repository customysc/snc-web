from typing import Optional

from app.utils.base_dto import BaseDto


class IvInterviewDto(BaseDto):
    name: Optional[str] = None