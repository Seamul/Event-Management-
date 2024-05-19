from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    event_time_utc = Column(DateTime)
    local_time = Column(DateTime)
    description = Column(String)
    attendees = Column(Integer)
    # created_at = Column(DateTime, default=func.now())
    # updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
