from fastapi import FastAPI

from app.routers import info

app = FastAPI(title="metrics-api")
app.include_router(info.router)

@app.get("/healthz")
def healthz():
    return {"ok": True}
