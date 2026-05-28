from app.api.xware.model import XWOrder
from app.utils.base_mapper import BaseMapper


class OrderMapper(BaseMapper[XWOrder]):
    model = XWOrder
