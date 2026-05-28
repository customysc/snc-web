from datetime import time, date
from typing import Optional

from app.utils.base_dto import BaseDto


class XWAttendanceDto(BaseDto):
    user_id: Optional[int] = None
    event_date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    effective_duration: Optional[int] = None
