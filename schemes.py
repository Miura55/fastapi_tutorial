from pydantic import BaseModel
from datetime import datetime

class EntryRequest(BaseModel):
    title: str = 'Title'
    content: str = 'This is content'
    user_name: str = 'User'


class MessageResponse(BaseModel):
    message: str = 'This message is example'


class CreateEntryResponse(BaseModel):
    id: int
    created_at: datetime


class Entry(BaseModel):
    id: int
    title: str
    content: str
    user_name: str
    created_at: datetime
    updated_at: datetime
