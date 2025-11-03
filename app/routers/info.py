from fastapi import APIRouter, Query
from app.services import sysstats
from app.config import settings

router = APIRouter()

@router.get("/info")
def info(full: bool = Query(False)):
    base = {"app": settings.APP_NAME, "env": settings.APP_ENV}
    return base | ({"stats": sysstats.snapshot()} if full else {})
