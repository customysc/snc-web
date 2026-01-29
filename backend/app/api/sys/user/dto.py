from typing import Optional

from app.utils.base_dto import BaseEntityDto


class UserDto(BaseEntityDto):
    email: Optional[str]
    phone: Optional[str]
    username: Optional[str]
    nickname: Optional[str]
    avatar: Optional[str]


class SysUserReadDto(BaseEntityDto):
    email: Optional[str]
    username: Optional[str]

class SysUserCreateDto(BaseEntityDto):
    email: Optional[str]
    phone: Optional[str]
    username: Optional[str]
    nickname: Optional[str]
    avatar: Optional[str]
