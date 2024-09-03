""""""

from pathlib import Path

from app.models.types import FileType

def get_app_path() -> Path:
    app_path = Path(__file__).parent.parent
    return app_path

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

    
def get_temp_dir() -> Path:
    
    try:
        tmp_dir = get_app_path().joinpath('tmp')
        if not tmp_dir.exists():
            tmp_dir.mkdir()
    except FileNotFoundError as e:
        pass
    
    return tmp_dir