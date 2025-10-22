import os

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "metrics-api")
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    ENABLE_WORKLOAD: bool = os.getenv("ENABLE_WORKLOAD", "false").lower() == "true"
    METRICS_NAMESPACE: str = os.getenv("METRICS_NAMESPACE", "metrics_api")

settings = Settings()
