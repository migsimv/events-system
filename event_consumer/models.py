from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    event_type = Column(String, nullable=False)
    event_payload = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
