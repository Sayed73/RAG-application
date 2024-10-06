from fastapi import FastAPI,APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1",# The prefix in APIRouter is used to specify a common path prefix for all the routes defined in this router.
    tags=["Base API"],# The tags in APIRouter are used to group routes by functionality
)

@base_router.get("/")
async def read_root():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    
    return {
        "APP_Name": app_name,
        "APP_Version": app_version
    }