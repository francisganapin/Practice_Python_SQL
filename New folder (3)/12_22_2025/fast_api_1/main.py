from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal,engine
from models import Item,Base


from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class ItemSchema(BaseModel):
    name:str
    price:float

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/items')
def get_items(db:Session = Depends(get_db)):
    return db.query(Item).all()

@app.post('/items')
def create_item(item: ItemSchema,db:Session = Depends(get_db)):
    new_item = Item(name=item.name,price=item.price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {'message':'Item added','data':new_item}


@app.get('/search')
def search_item(name:str,db:Session = Depends(get_db)):
    result = db.query(Item).filter(Item.name.like(f'%{name}%')).all()
    return result