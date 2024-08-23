
from fastapi import APIRouter, UploadFile

from app.utils import helpers

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    valid_extension = helpers.check_allowed_extention(file.filename)

    if not valid_extension:
        pass
    

@router.get("/status/{file_id}")
async def status():
    pass

@router.post("/result/{file_id}")
async def result():
    pass