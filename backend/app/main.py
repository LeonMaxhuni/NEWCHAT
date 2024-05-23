from typing import List
from fastapi import Depends, FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.active_chat: List = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            self.active_chat.append(message)
            await connection.send_json(self.active_chat)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast("A client disconnected.")


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

@app.get("/users/{user_id}/ticket/", response_model=List[schemas.Ticket])
def read_tickets(user_id:int, db: Session = Depends(get_db)):
    return crud.get_tickets(db = db, owner_id = user_id)

@app.post("/users/{user_id}/ticket/", response_model=schemas.Ticket)
def create_user_ticket(user_id: int, db: Session = Depends(get_db)):
    return crud.create_user_ticket(db = db, user_id = user_id)

@app.get("/users/{user_id}/ticket/{room_id}", response_model=List[schemas.Message])
def read_messages(user_id: int, room_id: int, db: Session = Depends(get_db)):
    tickets = crud.get_messages(db = db, room_id = room_id)
    if tickets is None:
        raise HTTPException(status_code=404, detail="No tickets found")
    return tickets

@app.post("/users/{user_id}/ticket/{room_id}", response_model=schemas.Message)
def create_message(user_id: int, room_id: int, message: str, db: Session = Depends(get_db)):

    message_data = message.model_dump()
    message_data['user_id'] = user_id
    message_data['room_id'] = room_id
    message_data['message'] = message
    new_message = schemas.MessageCreate(**message_data)
    
    return crud.create_message(db = db, message=new_message)