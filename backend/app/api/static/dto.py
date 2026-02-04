from typing import Optional

from pydantic import BaseModel


class FileDto(BaseModel):
    name: Optional[str] = None