from typing import Optional

from app.utils.base_dto import BaseDto


class SncBannerReadDto(BaseDto):
    name: Optional[str] = None
    image_url: Optional[str] = None
    target_url: Optional[str] = None
    target_type: Optional[str] = None
    sort_order: Optional[int] = None

class SncBannerCreateDto(BaseDto):
    name: Optional[str] = None
    image_url: Optional[str] = None
    target_url: Optional[str] = None
    target_type: Optional[str] = None
    sort_order: Optional[int] = None
    status: Optional[str] = None