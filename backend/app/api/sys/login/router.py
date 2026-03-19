from fastapi import APIRouter

from app.api.deps import SessionDep
from app.api.sys.login.dto import LoginByEmailDto
from app.api.sys.user.dto import SysUserReadDto
from app.api.sys.user.model import SysUser
from app.utils.jwt_util import JwtUtil
from app.utils.result import Result

router = APIRouter(prefix="", tags=["login"])

@router.post("/login", response_model=Result)
def login(session: SessionDep, login: LoginByEmailDto):
    user = session.query(SysUser).filter_by(email=login.email).first()
    # TODO 验证验证码
    if not user:
        return Result.fail(msg="用户不存在！")

    # TODO 密码加密
    if user.password != login.password:
        return Result.fail(msg="密码错误！")

    # TODO 删除验证码

    data = userInfo(user)
    return Result.ok(msg="登录成功！", data=data)

def userInfo(user: SysUser) -> dict:
    obj = {}
    email = user.email
    password = user.password
    token = JwtUtil.sign(email, password)
    obj["token"] = token
    obj["userInfo"] = SysUserReadDto.model_validate(user)
    return obj