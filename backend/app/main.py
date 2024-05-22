from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def test_page():
    return {"message": "Hello World"}

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db = db, user = user)

@app.post("/users/{user_id}/ticket/")
def create_user_ticket(user_id: int, db: Session = Depends(get_db)):
    return crud.create_user_ticket(db = db, user_id = user_id)

@app.post("/users/{user_id}/ticket/{room_id}", response_model=schemas.Message)
def create_message(user_id: int, room_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    message.user_id = user_id
    message.room_id = room_id
    return crud.create_message(db=db, message=message)