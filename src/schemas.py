from pydantic import BaseModel
from datetime import datetime
from typing import List

class EventBase(BaseModel):
    city: str
    event_time_utc: datetime
    local_time: datetime
    description: str
    attendees: int  # Change to List[str]

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    event_id: int

    class Config:
        from_attributes = True  # Use from_attributes for Pydantic v2 compatibility
