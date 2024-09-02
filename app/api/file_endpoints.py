
from fastapi import APIRouter, UploadFile, HTTPException, status

from app.database.connection import get_db
from app.services import file_service
from app.schemas.file import FileCreate
from app.models.status import FileStatus
from app.utils import helpers

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    valid_extension = helpers.check_allowed_extention(file.filename)

    if not valid_extension:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format"
        )
    
    try:
        file_data = FileCreate(
            file_name=file.filename,
            file_size=file.size,
            file_type=helpers.get_file_type(file.filename),
            file_status=FileStatus.IN_PROGRESS
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format"
        )
    
    db_file = file_service.create_file(db=get_db(), file_data=file_data)

    return {
        'file_id': db_file.id, 
        'file_name': db_file.name, 
        'file_size': db_file.size
    }


    

@router.get("/status/{file_id}")
async def processing_status():
    pass

@router.post("/result/{file_id}")
async def processing_result():
    pass