from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_tables():
    from app.utils.base_entity import BaseEntity
    import app.api.xware.model  # noqa: F401
    BaseEntity.metadata.create_all(bind=engine)

