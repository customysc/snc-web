from collections.abc import Generator
from typing import Annotated, Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.db import engine
from app.api.sys.user.model import SysUser

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def get_current_user(session: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> Optional[SysUser]:
    # 简化实现：从 token 中提取用户信息
    # 实际项目中应该验证 JWT token 并获取用户
    # 这里为了演示，返回第一个用户作为当前用户
    user = session.query(SysUser).first()
    return user


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]
CurrentUserDep = Annotated[Optional[SysUser], Depends(get_current_user)]