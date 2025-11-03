from fastapi import APIRouter
router = APIRouter()

@router.get("/healthz")
def healthz():
    return {"ok": True}

@router.get("/readyz")
def readyz():
    return {"ready": True}
