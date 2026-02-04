from app.api.bbs.comment.model import BbsComment
from app.utils.base_mapper import BaseMapper


class CommentMapper(BaseMapper[BbsComment]):
    model = BbsComment