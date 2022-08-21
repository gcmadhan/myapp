import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/{name}")

async def post_method(name: str):
    return {"message":name}
