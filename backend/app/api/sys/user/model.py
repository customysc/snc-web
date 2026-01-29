from typing import Optional

from app.utils.base_entity import BaseEntity
from sqlalchemy import Integer, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class SysUser(BaseEntity):
    __tablename__ = "sys_user"

    email: Mapped[Optional[str]] = mapped_column(String(255), comment="邮箱")
    phone: Mapped[Optional[str]] = mapped_column(String(64), comment="电话")

    username: Mapped[Optional[str]] = mapped_column(String(64), comment="用户名")
    nickname: Mapped[Optional[str]] = mapped_column(String(64), comment="昵称")

    password: Mapped[Optional[str]] = mapped_column(String(255), comment="密码")
    salt: Mapped[Optional[str]] = mapped_column(String(64), comment="盐")

    avatar: Mapped[Optional[str]] = mapped_column(String(255), comment="头像")
    status: Mapped[Optional[str]] = mapped_column(String(64), comment="状态")

class SysRole(BaseEntity):
    __tablename__ = "sys_role"

    name: Mapped[Optional[str]] = mapped_column(String(64), comment="名称")
    description: Mapped[Optional[str]] = mapped_column(String(255), comment="描述")

class SysUserRole(BaseEntity):
    __tablename__ = "sys_user_role"

    user_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="用户id")
    role_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="角色id")

class SysPermission(BaseEntity):
    __tablename__ = "sys_permission"

    parent_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="父id")
    name: Mapped[Optional[str]] = mapped_column(String(64), comment="名称")

    url: Mapped[Optional[str]] = mapped_column(String(255), comment="路径")
    component: Mapped[Optional[str]] = mapped_column(String(64), comment="组件")

    menu_type: Mapped[Optional[str]] = mapped_column(String(64), comment="菜单类型(0:一级菜单; 1:子菜单:2:按钮权限)")
    perms: Mapped[Optional[str]] = mapped_column(String(255), comment="菜单权限编码")
    sort_order: Mapped[Optional[str]] = mapped_column(Integer, comment="排序")

class SysRolePermission(BaseEntity):
    __tablename__ = "sys_role_permission"

    role_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="角色id")
    permission_id: Mapped[Optional[int]] = mapped_column(BigInteger, comment="权限id")


