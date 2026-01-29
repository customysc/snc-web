from app.api.snc.banner.model import SncBanner
from app.utils.base_mapper import BaseMapper


class BannerMapper(BaseMapper[SncBanner]):
    model = SncBanner