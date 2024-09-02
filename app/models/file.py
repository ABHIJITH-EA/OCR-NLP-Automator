from sqlalchemy import Column, Integer, String, Enum, Float
from database.connection import Base
from models.status import FileStatus

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    size = Column(Float)
    type = Column(String)
    status = Column(Enum(FileStatus), default=FileStatus.IN_PROGRESS)