# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()


def utc_now():
    """Current time in UTC (replaces the deprecated datetime.utcnow)."""
    return datetime.now(timezone.utc)


class Post(db.Model):
    __tablename__ = 'post'  # same table name as before

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # question | achievement | performance
    # indexed because the feed is always ordered by newest first
    created_at = db.Column(db.DateTime, default=utc_now, index=True)

    def __repr__(self):
        return f'<Post {self.id} {self.name}>'