from typing import Any, Dict

from fastapi import APIRouter, Query

from app.config import settings
from app.services import sysstats

router = APIRouter()


@router.get("/info")
def info(full: bool = Query(False)) -> Dict[str, Any]:
    base: Dict[str, Any] = {"app": settings.APP_NAME, "env": settings.APP_ENV}
    return base if not full else {**base, "stats": sysstats.snapshot()}
