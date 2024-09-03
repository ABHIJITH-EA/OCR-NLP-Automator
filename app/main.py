""" """
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import file_endpoints
from app.database import connection

@asynccontextmanager
async def lifepan(app: FastAPI):
    connection.Base.metadata.create_all(bind=connection.engine)
    yield

app = FastAPI(lifespan=lifepan)

app.include_router(file_endpoints.router, 
                   prefix="/api"
)
