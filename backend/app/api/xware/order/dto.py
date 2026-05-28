from datetime import datetime
from typing import Optional

from app.utils.base_dto import BaseDto


class XWOrderDto(BaseDto):
    name: Optional[str] = None
    student_no: Optional[str] = None
    department: Optional[str] = None
    phone: Optional[str] = None
    computer: Optional[str] = None
    issue: Optional[str] = None
    images: Optional[str] = None
    appointment_time: Optional[datetime] = None
    customer_notes: Optional[str] = None
    attend_time: Optional[datetime] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: Optional[str] = None
    result: Optional[str] = None
    resolution_method: Optional[str] = None
    resolution_process: Optional[str] = None
    resolution_images: Optional[str] = None
    customer_feedback: Optional[str] = None
