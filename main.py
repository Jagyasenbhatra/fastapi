
from fastapi import FastAPI

app = FastAPI()

def calculate_square(x):
    return x * x

@app.get("/square/{number}")
async def square(number: int):
    return {"result": calculate_square(number)}