from datetime import time, date, datetime
from typing import Optional

from app.utils.base_entity import BaseEntity
from sqlalchemy import BigInteger, DateTime, Date, Integer, String, Text, Time
from sqlalchemy.orm import Mapped, mapped_column


class XWAttendance(BaseEntity):
    __tablename__ = "xw_Attendance"

    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户ID")

    event_date: Mapped[Optional[date]] = mapped_column(Date, comment="活动日期")
    start_time: Mapped[Optional[time]] = mapped_column(Time, comment="到场时间")
    end_time: Mapped[Optional[time]] = mapped_column(Time, comment="离场时间")
    effective_duration: Mapped[Optional[int]] = mapped_column(Integer, comment="有效时长（单位：小时）")


# 该表一定程度上为快照表，故有部分重复数据
class XWOrder(BaseEntity):
    __tablename__ = "xw_order"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="姓名")
    student_no: Mapped[Optional[str]] = mapped_column(String(64), comment="学工号")
    department: Mapped[Optional[str]] = mapped_column(String(64), comment="部门")
    phone: Mapped[Optional[str]] = mapped_column(String(64), comment="联系电话")
    computer: Mapped[Optional[str]] = mapped_column(String(64), comment="电脑型号")
    issue: Mapped[Optional[str]] = mapped_column(String(255), comment="用户问题描述")
    images: Mapped[Optional[str]] = mapped_column(String(255), comment="问题图片描述")
    appointment_time: Mapped[Optional[datetime]] = mapped_column(DateTime, comment="预约时间")
    customer_notes: Mapped[Optional[str]] = mapped_column(String(255), comment="客户备注")
    attend_time: Mapped[Optional[datetime]] = mapped_column(DateTime, comment="到场时间")
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, comment="处理开始时间")
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, comment="处理结束时间")
    status: Mapped[Optional[str]] = mapped_column(String(64), comment="状态（New,Ready,Running,Blocked,Terminated）")
    result: Mapped[Optional[str]] = mapped_column(String(64), comment="结果（已解决，未解决）")
    resolution_method: Mapped[Optional[str]] = mapped_column(String(255), comment="处理方式")
    resolution_process: Mapped[Optional[str]] = mapped_column(String(255), comment="处理过程")
    resolution_images: Mapped[Optional[str]] = mapped_column(String(255), comment="处理图片")
    customer_feedback: Mapped[Optional[str]] = mapped_column(String(255), comment="客户反馈")

class XWOrderUser(BaseEntity):
    __tablename__ = "xw_order_user"
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户ID")
    order_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="工单ID")