from pydantic import BaseModel
from models.types import FileType

class FileCreate(BaseModel):
    file_name: str
    file_size: float
    file_type: FileType