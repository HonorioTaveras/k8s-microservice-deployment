import logging
from fastapi import FastAPI
from app.routers import info

def create_app() -> FastAPI:
    app = FastAPI(title="metrics-api")
    app.include_router(info.router)
    return app

app = create_app()
logging.basicConfig(level=logging.INFO)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/readyz")
def readyz():
    return {"ready": True}
