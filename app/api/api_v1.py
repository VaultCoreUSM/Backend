# backend/app/api/api_v1.py
from fastapi import APIRouter

from app.api.endpoints import cameras # , events (cuando lo crees)
from app.api.endpoints import reporte

api_router = APIRouter()
api_router.include_router(cameras.router, prefix="/cameras", tags=["Cameras"])
api_router.include_router(reporte.router,prefix="/reporte", tags=["Reporte"])
# api_router.include_router(events.router, prefix="/events", tags=["Events"])