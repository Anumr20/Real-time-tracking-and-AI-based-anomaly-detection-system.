import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost/tracking_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

    # Anomaly Detection Thresholds
    PROLONGED_INACTIVITY_SECONDS = 3600  # 1 hour
    ROUTE_DEVIATION_METERS = 500         # 500 meters
    LOCATION_DROP_OFF_SECONDS = 1800     # 30 minutes
