from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base_entity import BaseEntity


class IvInterview(BaseEntity):
    __tablename__ = "iv_interview"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="面试名称")


class IvRegistration(BaseEntity):
    __tablename__ = "iv_registration"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="姓名")
    information: Mapped[Optional[str]] = mapped_column(Text, comment="其他学生信息，JSON格式")
    interview_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="面试ID")
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户ID")


class IvInterviewRound(BaseEntity):
    __tablename__ = "iv_interview_round"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="轮次名称")
    sort_order: Mapped[Optional[int]] = mapped_column(Integer, comment="用于区分一面二面")
    department_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="部门ID")
    current_group_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="当前分组ID")
    interview_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="面试ID")


class IvInterviewUser(BaseEntity):
    __tablename__ = "iv_interview_user"

    interview_round_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="面试轮次ID")
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户ID")


class IvAttendance(BaseEntity):
    __tablename__ = "iv_attendance"

    attend_time: Mapped[Optional[datetime]] = mapped_column(DateTime, comment="签到时间")
    status: Mapped[Optional[str]] = mapped_column(String(64), comment="签到状态")
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户ID")
    interview_round_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="面试轮次ID")


class IvGroup(BaseEntity):
    __tablename__ = "iv_group"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="分组名称")
    sort_order: Mapped[Optional[int]] = mapped_column(Integer, comment="排序")
    interview_round_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="面试轮次ID")
    seat_number: Mapped[Optional[int]] = mapped_column(Integer, comment="座位号")


class IvComment(BaseEntity):
    __tablename__ = "iv_comment"

    content: Mapped[Optional[str]] = mapped_column(String(255), comment="评价内容")
    score: Mapped[Optional[int]] = mapped_column(Integer, comment="评分")
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户ID")
    interview_round_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="面试轮次ID")