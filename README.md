Real-time Tracking & Anomaly Detection Backend (Demo)
----------------------------------------------------
This FastAPI backend demonstrates a focused implementation of:
- Opt-in real-time tracking (subscribe/unsubscribe)
- Receiving location updates (/tracking/update)
- Anomaly detection on updates:
  - sudden_location_jump (large displacement in short time)
  - prolonged_dwell (immobile for long time)
  - route_deviation (far from planned route)
  - panic button recording
- Simple alerts store and retrieval

How to run:
1. python -m venv venv
2. source venv/bin/activate   # Windows: venv\Scripts\activate
3. pip install -r requirements.txt
4. uvicorn app:app --reload --port 8000

API Endpoints (examples):
- POST /subscribe  JSON: { "tracker_id":"t1", "contacts":["+91..."], "route":[[lat,lon],[lat,lon],...] }
- POST /tracking/update  JSON: {"tracker_id":"t1","lat":28.6,"lon":77.2,"timestamp":"2025-09-17T09:00:00Z","speed_m_s":1.2}
- POST /panic  JSON: {"tracker_id":"t1","message":"help","timestamp":"2025-09-17T09:10:00Z"}
- GET /alerts/{tracker_id}
- GET /status/{tracker_id}

Notes:
- This is intentionally kept lightweight and in-memory for demo. For production use:
  - persist trackers and alerts in a database (Postgres, MongoDB)
  - use background workers (Celery, RQ) for scheduled missing checks and notification dispatch
  - secure endpoints with authentication & rate limiting
  - integrate with map services for nearest police dispatch logic
