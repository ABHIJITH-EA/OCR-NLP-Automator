from pydantic import BaseModel
from app.models.types import FileType
from app.models.status import FileStatus

class File(BaseModel):
    file_name: str

class FileCreate(File):
    file_size: float
    file_type: FileType 
    file_status: FileStatus


class TempFileCreate(File):
    pass