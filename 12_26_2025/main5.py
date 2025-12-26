from fastapi import FastAPI

app = FastAPI()

@app.get('/users')
async def get_users():
    return ['Rick','Morty','Summer','Beth','Jerry']

@app.get('/users')
async def read_user2():
    return ['Bean','Elfo']