from typing import Optional

from app.utils.base_dto import BaseDto


class SncThreadCreateDto(BaseDto):
    title: Optional[str] = None
    content: Optional[str] = None