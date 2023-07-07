from sqlalchemy import Column, Integer, String, Enum, DateTime
from database import Base
from datetime import datetime
from schemas import Priority


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    priority = Column(Enum(Priority), default=Priority.low, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, nullable=False)
