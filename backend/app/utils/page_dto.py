from typing import List, Optional

from pydantic import BaseModel


class PageDto[T](BaseModel):
    records: Optional[List[T]]
    current: Optional[int]
    size: Optional[int]
    pages: Optional[int]
    total: Optional[int]