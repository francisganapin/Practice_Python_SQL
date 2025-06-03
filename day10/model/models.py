from sqlmodel import Session,SQLModel,create_engine,select,Field
from typing import Optional


class GymMember(SQLModel,table=True):
    id:Optional[int] = Field(default=None,primary_key=True)
    key_code:str = Field(unique=True)
    first_name:str
    last_name:str
    phone:str
    membership_type:str
    is_active:bool = True
    expiry:str


DATABASE_URL = 'sqlite:///gym_members.db'
engine = create_engine(DATABASE_URL,echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)

create_table() 
