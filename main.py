from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Aria API+UI", version="0.1.0")

# CORS (open for demo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Ask(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/aria/ask")
def aria_ask(a: Ask):
    q = a.query.lower()
    if "gross" in q:
        return {"answer": "Gross margin dipped due to increased COGS. Consider supplier negotiations."}
    if "revenue" in q:
        return {"answer": "Revenue is up due to strong sales in Q2. Forecast remains positive."}
    return {"answer": f"You asked: '{a.query}'. Aria is thinking..."}

# Serve UI
@app.get("/")
def index():
    return FileResponse("index.html")
