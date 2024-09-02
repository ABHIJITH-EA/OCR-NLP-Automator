from sqlalchemy import Column, Integer, String, Enum, Float
from app.database.connection import Base
from app.models.status import FileStatus
from app.models.types import FileType

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    size = Column(Float)
    type = Column(Enum(FileType))
    status = Column(Enum(FileStatus), default=FileStatus.IN_PROGRESS)