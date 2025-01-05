import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

@app.get("/api/chat")
def getVars():
  return {"test": "hello, world"}

app.mount("/", StaticFiles(directory=Path("html").resolve(), html=True), name="static")

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)