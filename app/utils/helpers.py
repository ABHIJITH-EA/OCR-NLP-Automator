""""""

from app.models.types import FileType

def check_allowed_extention(file_name: str):
    allowed_extentions = ["pdf"]
    allowed_status = False
    ext = file_name.split('.')[-1]

    if ext in allowed_extentions:
        allowed_status = True

    return allowed_status

def get_file_type(file_name: str) -> FileType:
    ext = file_name.split('.')[-1]
    if ext == "pdf":
        return FileType.PDF
    else:
        raise ValueError("Unsuported type")