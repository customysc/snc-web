from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

class BaseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseEntityDto(BaseDto):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    created_by: Optional[int]
    updated_by: Optional[int]
    del_flag: Optional[int]