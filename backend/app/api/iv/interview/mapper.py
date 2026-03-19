from app.api.iv.model import IvInterview
from app.utils.base_mapper import BaseMapper


class IvInterviewMapper(BaseMapper[IvInterview]):
    model = IvInterview