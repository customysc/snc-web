from app.api.bbs.model import BbsThread
from app.utils.base_mapper import BaseMapper


class ThreadMapper(BaseMapper[BbsThread]):
    model = BbsThread