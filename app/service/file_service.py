from sqlalchemy.orm import Session
from app.schemas.file import FileCreate

def create_file(db: Session, file: FileCreate):
    pass