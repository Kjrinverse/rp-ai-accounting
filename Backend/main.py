
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI()

# Enable CORS for frontend (e.g., Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def read_root():
    return {"message": "Backend is working"}

# Ping test
@app.get("/ping")
def ping():
    return {"response": "pong"}

# ========== Journal POST Route ==========

class JournalEntry(BaseModel):
    date: datetime.date
    account_code: str
    description: str
    debit: float
    credit: float
    reference: str

@app.post("/journals")
def post_journals(entries: List[JournalEntry]):
    # In real use, you'd save this to a DB or file here
    return {"status": "success", "received": len(entries), "entries": entries}
