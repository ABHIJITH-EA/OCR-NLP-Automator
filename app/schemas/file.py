from pydantic import BaseModel
from app.models.types import FileType
from app.models.status import FileStatus

class FileCreate(BaseModel):
    file_name: str
    file_size: float
    file_type: FileType
    file_status: FileStatus