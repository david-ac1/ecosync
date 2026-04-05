from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="EcoSync API", version="1.0.0")

# Enable CORS for the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InventoryItem(BaseModel):
    id: Optional[str] = None
    title: str
    category: str
    bought_year: str
    resale_value: str
    health_score: int
    image_url: Optional[str] = None

# In-memory mock store for now (until Supabase is connected)
items_db = [
    {"title": "Arc'teryx Alpha SV", "category": "Apparel", "bought_year": "2023", "resale_value": "$245", "health_score": 88, "image_url": "https://api.dicebear.com/7.x/identicon/svg?seed=arc"},
    {"title": "iPad Pro 12.9\" M2", "category": "Tech", "bought_year": "2022", "resale_value": "$680", "health_score": 62, "image_url": "https://api.dicebear.com/7.x/identicon/svg?seed=ipad"},
    {"title": "Uniqlo Down Parka", "category": "Apparel", "bought_year": "2021", "resale_value": "$110", "health_score": 41, "image_url": "https://api.dicebear.com/7.x/identicon/svg?seed=uniqlo"},
]

@app.get("/api/inventory", response_model=List[InventoryItem])
async def get_inventory():
    return items_db

@app.post("/api/audit/start")
async def start_audit():
    # This will trigger the AI parsing engine in future steps
    return {"status": "success", "message": "Audit started", "items_scanned": 24}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
