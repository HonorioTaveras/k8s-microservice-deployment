import psutil
from typing import Dict

def snapshot() -> Dict:
    vm = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    load1, load5, load15 = psutil.getloadavg()
    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "load_avg": {"1m": load1, "5m": load5, "15m": load15},
        "memory": {"total": vm.total, "used": vm.used, "percent": vm.percent},
        "disk": {"total": disk.total, "used": disk.used, "percent": disk.percent},
        "net": psutil.net_io_counters()._asdict(),
        "pids": len(psutil.pids()),
    }
