
import shutil
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.file import File, TempFile
from app.utils.helpers import get_temp_dir, get_file_type
from app.models.status import FileActiveStatus, FileStatus


def prepare_for_processing(db: Session, file: UploadFile):
    db_file = File(
        name = file.filename,
        size = file.size,
        type = get_file_type(file.filename),
        status = FileStatus.IN_PROGRESS
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    file_name = f'{uuid.uuid4()}_{file.filename}'

    with open(get_temp_dir().joinpath(file_name), 'wb') as f:
        shutil.copyfileobj(file.file, f)

        db_tempfile = TempFile(
            file_id = db_file.id,
            status = FileActiveStatus.ACTIVE
        )
        db.add(db_tempfile)
        db.commit()
        db.refresh(db_tempfile)
        
    return db_file
       