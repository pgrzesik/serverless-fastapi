from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def hello_world():
    return {'message': 'Hello from FastAPI'}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f'Hello from FastAPI, {name}!'}

handler = Mangum(app)
