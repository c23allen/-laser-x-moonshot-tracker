import os
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Lasers X Moonshots Tracker")

STARTED_AT = datetime.now(timezone.utc)

@app.get("/")
def root():
    return {
        "name": "Lasers X Moonshots Tracker",
        "status": "online",
        "message": "Tracker foundation is running."
    }

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/status")
def status():
    now = datetime.now(timezone.utc)
    return {
        "status": "online",
        "started_at_utc": STARTED_AT.isoformat(),
        "checked_at_utc": now.isoformat(),
        "uptime_seconds": int((now - STARTED_AT).total_seconds()),
        "mlb_watcher": "not_connected_yet",
        "discord": "not_connected_yet",
        "x": "not_connected_yet",
        "odds_bank": "not_connected_yet",
    }
