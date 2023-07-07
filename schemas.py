from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Sort(str, Enum):
    created_at = "created_at"
    priority = "priority"


class Priority(str, Enum):
    high = "high"
    mid = "mid"
    low = "low"


class TaskCreate(BaseModel):
    content: str
    priority: Priority = Priority.low


class TaskRead(BaseModel):
    id: int
    content: str
    priority: Priority
    created_at: datetime
    # user_id: int

    class Config:
        orm_mode = True
