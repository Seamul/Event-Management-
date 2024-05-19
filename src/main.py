from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from .database import SessionLocal, engine, Base
from . import models, schemas
from sqlalchemy import func
import pandas as pd

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)


# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


import io
import json
import pandas as pd
from pytz import timezone

# Dictionary mapping cities to their respective timezones
city_timezones = {
    "New York": "America/New_York",
    "Los Angeles": "America/Los_Angeles",
    "Chicago": "America/Chicago",
    "San Francisco": "America/Los_Angeles",
    "Houston": "America/Chicago",
    "Miami": "America/New_York",
    "Seattle": "America/Los_Angeles",
    "Boston": "America/New_York",
    "Denver": "America/Denver",
    "Atlanta": "America/New_York",
    "Dallas": "America/Chicago",
    "Austin": "America/Chicago",
    "San Diego": "America/Los_Angeles",
    "Orlando": "America/New_York",
    "Las Vegas": "America/Los_Angeles",
    "New Orleans": "America/Chicago",
    "Philadelphia": "America/New_York",
    "Phoenix": "America/Phoenix",
    "Portland": "America/Los_Angeles",
    "San Antonio": "America/Chicago",
    "Nashville": "America/Chicago",
    "Detroit": "America/Detroit",
    "Indianapolis": "America/Indiana/Indianapolis",
    "Charlotte": "America/New_York",
    "Memphis": "America/Chicago",
    "Salt Lake City": "America/Denver",
    "Oklahoma City": "America/Chicago",
    "Cleveland": "America/New_York",
    "Milwaukee": "America/Chicago",
    "Kansas City": "America/Chicago",
}


def convert_to_local_time(row):
    city = row["city"]
    utc_time = row["event_time_utc"]
    local_tz = timezone(city_timezones[city])
    utc_time = utc_time.tz_localize("UTC")
    local_time = utc_time.tz_convert(local_tz)
    return local_time


@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.filename.endswith(".csv"):
        contents = await file.read()
        try:
            csv_file = io.BytesIO(contents)
            df = pd.read_csv(csv_file, parse_dates=["event_time_utc"])
            # Applying the conversion function to each row

            df["local_time"] = df.apply(convert_to_local_time, axis=1)

            events_data = df.to_dict(orient="records")
            for event_data in events_data:
                event = models.Event(**event_data)
                db.add(event)
            db.commit()
            return {"message": "CSV uploaded successfully and data saved to database"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")


# done
@app.get("/events", response_model=List[schemas.Event])
def get_events(city: str = None, date: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Event)
    if city:
        query = query.filter(models.Event.city == city)
    if date:
        query = query.filter(func.DATE(models.Event.local_time) == date)
    return query.all()


# done
@app.get("/event/{event_id}", response_model=schemas.Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


# done
@app.post("/events/add", response_model=schemas.Event)
def add_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# done
@app.put("/event/{event_id}", response_model=schemas.Event)
def update_event(
    event_id: int, event: schemas.EventUpdate, db: Session = Depends(get_db)
):
    db_event = db.query(models.Event).filter(models.Event.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event.dict().items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event


# done
@app.delete("/event/{event_id}", response_model=schemas.Event)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(models.Event).filter(models.Event.event_id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return db_event
