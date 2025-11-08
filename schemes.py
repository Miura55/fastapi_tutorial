from pydantic import BaseModel
from datetime import datetime

class EntryRequest(BaseModel):
    title: str = 'Title'
    content: str = 'This is content'
    user_name: str = 'User'


class MessageResponse(BaseModel):
    message: str = 'This message is example'


class CreateEntryResponse(BaseModel):
    id: int = 1
    created_at: datetime = datetime.now()


class Entry(BaseModel):
    id: int = 1
    title: str = 'Title'
    content: str = 'This is content'
    user_name: str = 'User'
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
