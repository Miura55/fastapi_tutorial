from pydantic import BaseModel

class EntryRequest(BaseModel):
    title: str = 'Title'
    content: str = 'This is content'
    user_name: str = 'User'


class MessageResponse(BaseModel):
    message: str = 'This message is example'


class EntryBase(BaseModel):
    title: str
    content: str
    user_name: str


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True
