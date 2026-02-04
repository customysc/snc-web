from typing import Optional

from app.utils.base_dto import BaseDto


class SncPostCreateDto(BaseDto):
    content: Optional[str] = None