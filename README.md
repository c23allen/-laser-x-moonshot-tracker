# -laser-x-moonshot-tracker# Lasers X Moonshots Tracker

Phone-first starter for the Lasers X Moonshots live MLB tracker.

## What this first build does
- Runs a FastAPI service in the cloud.
- Provides `/health` and `/status` endpoints.
- Establishes the deployment foundation for the MLB watcher, odds bank, Discord posting, X posting, and replay system.

## Run locally / in Codespaces
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

Open:
- `/`
- `/health`
- `/status`

## Railway
Connect this GitHub repository to a Railway service. Railway can use the included `railway.json` start command.

## Next build stages
1. Live MLB home-run watcher
2. 105+ / 110+ / 400+ / 420+ qualification engine
3. Daily odds bank
4. Discord alerts
5. X alerts
6. Replay handling
7. Admin phone dashboard
