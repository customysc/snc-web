from app.api.xware.model import XWAttendance
from app.utils.base_mapper import BaseMapper


class AttendanceMapper(BaseMapper[XWAttendance]):
    model = XWAttendance
