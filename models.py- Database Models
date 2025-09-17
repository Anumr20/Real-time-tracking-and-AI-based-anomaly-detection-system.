from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geography
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    # ... other fields

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    coordinates = db.Column(Geography(geometry_type='POINT', srid=4326), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False)

class Route(db.Model):
    __tablename__ = 'routes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    path = db.Column(Geography(geometry_type='LINESTRING', srid=4326), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

class Alert(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    alert_type = db.Column(db.String(50), nullable=False)
    location_id = db.Column(db.BigInteger, db.ForeignKey('locations.id'))
    details = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
