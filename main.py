import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from chat import Database
from pydantic import BaseModel
from typing import List

database = Database()

app = FastAPI()

@app.get("/api/get_chats")
def get_chats(username: str):
  return database.get_chats(username)

@app.get("/api/get_chat")
def get_chat(id: int):
  return database.get_chat(id)

@app.post("/api/create_chat")
def create_chat(usernames: List[str]):
  database.create_chat(usernames)

class Message(BaseModel):
  id: int
  username: str
  text: str
  
@app.post("/api/send_message")
def send_message(message: Message):
  database.send_message(message.id, message.username, message.text)

app.mount("/", StaticFiles(directory=Path("site").resolve(), html=True), name="static")

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)