from fastapi import FastAPI
from calculator import add
from utils import greet

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": greet("Sudheer")
    }


@app.get("/add")
def addition(a: int, b: int):
    return {
        "result": add(a, b)
    }