from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
import json, asyncio
import os

app = FastAPI()

latest_metrics = {}

# Update folder path
DASHBOARD_FOLDER = "dashboard"

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (optional if you add charts, images)
if os.path.isdir(DASHBOARD_FOLDER):
    app.mount("/dashboard", StaticFiles(directory=DASHBOARD_FOLDER), name="dashboard")
else:
    raise RuntimeError(f"Directory '{DASHBOARD_FOLDER}' does not exist")



@app.post("/api/metrics")
async def receive_metrics(request: Request):
    data = await request.json()
    latest_metrics.update(data)
    return {"message": "Metrics received"}

@app.get("/")
async def root():
    index_path = os.path.join(DASHBOARD_FOLDER, "monitrix_dashboard.html")
    if not os.path.exists(index_path):
        return HTMLResponse("<h2>Dashboard file missing</h2>", status_code=404)
    html = open(index_path, encoding="utf-8").read()
    return HTMLResponse(content=html)

@app.websocket("/ws/metrics")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_text(json.dumps(latest_metrics))
        await asyncio.sleep(1)
