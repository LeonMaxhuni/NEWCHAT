from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username = user.username, email = user.email, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()

def get_tickets(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).where(models.Ticket.owner_id == owner_id).offset(skip).limit(limit).all()

def create_user_ticket(db: Session, user_id: int):
    db_ticket = models.Ticket(owner_id = user_id)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_messages(db: Session, room_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Message).filter(models.Message.room_id == room_id).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(message = message.message, room_id = message.room_id, user_id = message.user_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item