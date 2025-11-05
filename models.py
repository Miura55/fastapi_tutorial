from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
# from database import Base
from sqlmodel import SQLModel, Field
from datetime import datetime

class Entry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    user_name: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now})
