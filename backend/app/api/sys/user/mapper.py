from app.api.sys.user.model import SysUser
from app.utils.base_mapper import BaseMapper


class SysUserMapper(BaseMapper[SysUser]):
    model = SysUser