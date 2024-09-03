from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
from app.models.status import FileStatus, FileActiveStatus
from app.models.types import FileType

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    size = Column(Float)
    type = Column(Enum(FileType))
    status = Column(Enum(FileStatus), default=FileStatus.IN_PROGRESS)
    
    temp_files = relationship("TempFile", back_populates="file")


class TempFile(Base):
    __tablename__ = "temp_files"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    status = Column(Enum(FileActiveStatus), default=FileActiveStatus.ACTIVE)
    
    file = relationship("File", back_populates="temp_files")