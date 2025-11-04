from fastapi import APIRouter
from fastapi.responses import Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    Gauge,
    generate_latest,
)

from app.config import settings
from app.services import sysstats

router = APIRouter()

@router.get("/metrics")
def metrics():
    reg = CollectorRegistry()
    snap = sysstats.snapshot()

    g_cpu = Gauge(
        f"{settings.METRICS_NAMESPACE}_cpu_percent",
        "CPU percent",
        registry=reg,
    )
    g_cpu.set(snap["cpu_percent"])

    g_load = Gauge(
        f"{settings.METRICS_NAMESPACE}_load_avg",
        "Load average",
        ["window"],
        registry=reg,
    )
    for k, v in snap["load_avg"].items():
        g_load.labels(window=k).set(v)

    g_mem = Gauge(
        f"{settings.METRICS_NAMESPACE}_memory_bytes",
        "Memory bytes",
        ["type"],
        registry=reg,
    )
    g_mem.labels(type="total").set(snap["memory"]["total"])
    g_mem.labels(type="used").set(snap["memory"]["used"])

    g_mem_pct = Gauge(
        f"{settings.METRICS_NAMESPACE}_memory_percent",
        "Memory percent",
        registry=reg,
    )
    g_mem_pct.set(snap["memory"]["percent"])

    g_disk_pct = Gauge(
        f"{settings.METRICS_NAMESPACE}_disk_percent",
        "Disk percent",
        registry=reg,
    )
    g_disk_pct.set(snap["disk"]["percent"])

    return Response(generate_latest(reg), media_type=CONTENT_TYPE_LATEST)
