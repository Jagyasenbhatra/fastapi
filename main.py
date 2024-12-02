
from fastapi import FastAPI

app = FastAPI()

def calculate_square(x):
    return x * x

def calculate_cube(x):
    return x*x*x

@app.get("/square/{number}")
async def square(number: int):
    return {"result": calculate_square(number)}


@app.get("/cube/{number}")
async def cube(number: int):
    return {"result": calculate_cube(number)}