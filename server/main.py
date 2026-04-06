from fastapi import FastAPI, HTTPException, BackgroundTasks, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
from dotenv import load_dotenv
import random

from services.market import market_service
from services.predictor import predictor_engine
from services.sustainability import shi_service
from services.matchmaker import matchmaker_service
from services.database import database_service
from services.coordinator import coordinator_service
from services.parsing import parsing_service

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
    market_trend: Optional[str] = "Stable"
    peak_prediction: Optional[str] = None
    matching_action: Optional[str] = None
    action_label: Optional[str] = None
    co2_saved: Optional[str] = None

class FeedItem(BaseModel):
    source: str
    message: str
    time: str
    status: Optional[str] = None

# In-memory mock store for now (until Supabase is connected)
items_db = []

feed_db = [
    {"source": "SYSTEM", "message": "EcoSync Engine Online. Ready for ingestion.", "time": "JUST NOW", "status": "ACTIVE"}
]

@app.get("/api/inventory", response_model=List[InventoryItem])
async def get_inventory():
    print(f"Debug: items_db size: {len(items_db)}")
    # Use Supabase if configured, otherwise fall back to mock store
    db_items = database_service.get_inventory()
    source_items = db_items if db_items is not None else items_db
    
    dynamic_items = []
    for item in source_items:
        price, trend = market_service.get_floor_price(item["title"])
        prediction = predictor_engine.predict_peak_window(item["title"], item["category"], item["bought_year"])
        
        # New Phase 3 Logic
        health, co2 = shi_service.calculate_shi(item["category"], item["bought_year"], item["resale_value"])
        matching_action, action_label = matchmaker_service.get_recommendation(item["category"], health, trend, prediction)
        
        dynamic_items.append({
            **item,
            "resale_value": price,
            "market_trend": trend,
            "peak_prediction": prediction,
            "health_score": health,
            "matching_action": matching_action,
            "action_label": action_label,
            "co2_saved": co2
        })
    return dynamic_items

@app.get("/api/feed", response_model=List[FeedItem])
async def get_feed():
    return feed_db

@app.post("/api/audit/start")
async def start_audit():
    new_item = {
        "title": "Peak Design Travel Backpack",
        "category": "Apparel",
        "bought_year": "2023",
        "resale_value": "$180",
        "health_score": 95,
        "image_url": "https://api.dicebear.com/7.x/identicon/svg?seed=peak"
    }
    
    if database_service.client:
        database_service.add_item(new_item)
    else:
        items_db.insert(0, new_item)
        
    feed_db.insert(0, {"source": "GMAIL CONNECTOR", "message": f"Found receipt: {new_item['title']}", "time": "JUST NOW", "status": "SYNCED"})

    return {"status": "success", "message": "Audit started", "items_scanned": 1}

@app.post("/api/redistribute/{item_idx}")
async def redistribute_item(item_idx: int):
    # Fetch original item to get context
    if item_idx < 0 or item_idx >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    
    item = items_db[item_idx]
    
    # Trigger the autonomous coordinator
    result = await coordinator_service.orchestrate_redistribution(item)
    
    return {
        "status": "success",
        "item": item["title"],
        "redistribution": result
    }

@app.post("/api/audit/start")
async def start_audit():
    # This will trigger the AI parsing engine in future steps
    return {"status": "success", "message": "Audit started", "items_scanned": 24}

@app.post("/api/ingest/upload")
async def upload_receipt(file: UploadFile = File(...)):
    contents = await file.read()
    media_type = file.content_type
    
    # 1. Parse image into structured data
    parsed_data = parsing_service.parse_receipt(contents, media_type)
    
    # 2. Enrich with Phase 2 & 3 intelligence
    price, trend = market_service.get_floor_price(parsed_data["title"])
    prediction = predictor_engine.predict_peak_window(parsed_data["title"], parsed_data["category"], parsed_data["bought_year"])
    health, co2 = shi_service.calculate_shi(parsed_data["category"], parsed_data["bought_year"], parsed_data["resale_value"])
    matching_action, action_label = matchmaker_service.get_recommendation(parsed_data["category"], health, trend, prediction)
    
    new_item = {
        "title": parsed_data["title"],
        "category": parsed_data["category"],
        "bought_year": str(parsed_data["bought_year"]),
        "resale_value": price if price else parsed_data["resale_value"],
        "health_score": health,
        "image_url": f"https://api.dicebear.com/7.x/identicon/svg?seed={parsed_data['title'].replace(' ', '')}"
    }
    
    # 3. Save to database or mock store
    if database_service.client:
        database_service.add_item(new_item)
    else:
        items_db.insert(0, new_item)
        
    feed_db.insert(0, {"source": "VISION ENGINE", "message": f"Parsed new asset: {new_item['title']}", "time": "JUST NOW", "status": "VERIFIED"})
        
    return {

        "status": "success", 
        "item": {
            **new_item,
            "market_trend": trend,
            "peak_prediction": prediction,
            "matching_action": matching_action,
            "action_label": action_label,
            "co2_saved": co2
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
