from sqlalchemy.orm import Session

from app.schemas.file import FileCreate
from app.models.file import File, FileStatus

def create_file(db: Session, file_data: FileCreate):
    db_file = File(
        name = file_data.file_name,
        size = file_data.file_size,
        type = file_data.file_type,
        status = file_data.file_status.IN_PROGRESS
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return db_file