""" """

from fastapi import FastAPI

from app.api import file_endpoints

app = FastAPI()

app.include_router(file_endpoints.router, 
                   prefix="/api"
)
