from typing import Optional

from app.utils.base_dto import BaseDto


class SncCommentCreateDto(BaseDto):
    content: Optional[str] = None