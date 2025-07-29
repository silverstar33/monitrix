import time
import psutil
import requests
import socket

SERVER_URL = "http://localhost:8000/api/metrics"
HOSTNAME = socket.gethostname()

def get_metrics():
    return {
        "hostname": HOSTNAME,
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "timestamp": time.time()
    }

while True:
    try:
        data = get_metrics()
        requests.post(SERVER_URL, json=data, timeout=5)
        print(f"Sent metrics: {data}")
    except Exception as e:
        print("Error sending metrics:", e)
    time.sleep(3)
