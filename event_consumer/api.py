from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from .database import Database
from .models import Event

app = FastAPI()

class EventPayload(BaseModel):
    event_type: str
    event_payload: str

def init_api(database: Database):
    @app.post("/event")
    async def receive_event(
        event: EventPayload,
        session: Session = Depends(database.get_session)
    ):
        db_event = Event(
            event_type=event.event_type,
            event_payload=event.event_payload
        )
        session.add(db_event)
        session.commit()
        return {"status": "success"}