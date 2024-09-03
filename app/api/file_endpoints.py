
from fastapi import APIRouter, UploadFile, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services import file_service
from app.utils import helpers

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile, db: Session = Depends(get_db)):
    valid_extension = helpers.check_allowed_extention(file.filename)
    
    if not valid_extension:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format"
        )
    
    db_file = file_service.prepare_for_processing(db=db, file=file)
    
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