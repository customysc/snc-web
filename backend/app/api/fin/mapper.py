from app.api.fin.model import Expenditure
from app.utils.base_mapper import BaseMapper

class FinMapper(BaseMapper[Expenditure]):
    model = Expenditure