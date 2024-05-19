from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    city: str
    event_time_utc: datetime
    local_time: datetime
    description: str
    attendees: int

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    event_id: int
    # created_at: datetime
    # updated_at: datetime

    class Config:
        orm_mode = True
