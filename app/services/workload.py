import time
import threading

def burn_cpu(seconds: int = 5):
    end = time.time() + seconds
    x = 0
    while time.time() < end:
        x += 1

def allocate_mem(megabytes: int = 50, seconds: int = 5):
    blob = bytearray(megabytes * 1024 * 1024)
    time.sleep(seconds)
    del blob

def start_async(cpu_seconds: int = 5, mem_mb: int = 0, mem_seconds: int = 5):
    threads = []
    if cpu_seconds > 0:
        threads.append(threading.Thread(target=burn_cpu, args=(cpu_seconds,)))
    if mem_mb > 0:
        threads.append(threading.Thread(target=allocate_mem, args=(mem_mb, mem_seconds)))
    for t in threads:
        t.start()
    return len(threads)
