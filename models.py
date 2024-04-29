from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    user_name = Column(String)
    created_at = Column(DateTime, server_default='now()')
