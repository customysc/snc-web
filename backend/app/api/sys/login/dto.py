from typing import Optional

from app.utils.base_dto import dto


class LoginByEmailDto(dto):
    email: Optional[str]
    password: Optional[str]
    captcha: Optional[str]