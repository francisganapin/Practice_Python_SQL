from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    id:int
    name:str
    price:float

@app.get('/items')
def get_item():
    return items

@app.post('/items')
def create_item(item:Item):
    items.append(item)
    return {'message':'Item added','data':item}

@app.put('/items/{item_id}')
def update_item(item_id: int,new_item:Item):
    for i, existing in enumerate(items):
        if existing.id == item_id:
            items[i] = new_item
            return {'message':'Item updated','data':new_item}
    return {'error':'Item not Found'}