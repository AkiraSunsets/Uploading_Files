from core.configs import settings

from sqlalchemy import Column, Integer, String, LargeBinary

class StoredFile(seetings.DBBaseModel):
    __tablename__ = "files"
    id: int = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    filename = Column(String(256), index=True)
    content_type = Column(String(256))
    content = Column(LargeBinary())
    