from pydantic import BaseModel

class Entry(BaseModel):
    title: str = 'Title'
    content: str = 'This is content'
    user_name: str = 'User' 


class MessageResponse(BaseModel):
    message: str = 'This message is example'
