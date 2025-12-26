from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Allow CORS (just like in Flask)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/data")
async def get_data():
    # FastAPI is built for async! 
    # await asyncio.sleep(2) is the non-blocking version of time.sleep(2)
    await asyncio.sleep(2)
    return {"message": "This was an async response!", "status": "success"}

# Feature: Automatic Data Validation with Pydantic
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/api/items")
async def create_item(item: Item):
    return {"message": f"Created item {item.name} with price {item.price}"}
