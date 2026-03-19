from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

class dto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class BaseDto(dto):
    id: Optional[int] = None

class BaseEntityDto(BaseDto):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    del_flag: Optional[int] = None