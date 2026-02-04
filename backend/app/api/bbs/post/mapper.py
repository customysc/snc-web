from app.api.bbs.post.model import BbsPost
from app.api.bbs.thread.model import BbsThread
from app.utils.base_mapper import BaseMapper


class PostMapper(BaseMapper[BbsPost]):
    model = BbsThread