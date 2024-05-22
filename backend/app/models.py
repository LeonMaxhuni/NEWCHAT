from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    tickets = relationship("Ticket", back_populates="users")
    messages = relationship("Message", back_populates="users")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates="tickets")
    messages = relationship("Message", back_populates="tickets")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)
    room_id = Column(Integer, ForeignKey("tickets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates="messages")
    tickets = relationship("Ticket", back_populates="messages")