import logging

from fastapi import FastAPI

from app.routers import health, info, metrics


def create_app() -> FastAPI:
    app = FastAPI(title="metrics-api")
    app.include_router(health.router)
    app.include_router(info.router)
    app.include_router(metrics.router)
    return app


app = create_app()
logging.basicConfig(level=logging.INFO)
