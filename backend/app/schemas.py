from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class TicketBase(BaseModel):
    owner_id: int

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        from_attributes = True


class MessageBase(BaseModel):
    message: str
    room_id: int

class MessageCreate(MessageBase):
    user_id: int

class Message(MessageBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True