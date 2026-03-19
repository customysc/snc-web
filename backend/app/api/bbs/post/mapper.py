from app.api.bbs.model import BbsThread, BbsPost
from app.utils.base_mapper import BaseMapper


class PostMapper(BaseMapper[BbsPost]):
    model = BbsThread