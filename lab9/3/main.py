from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return  "Welcome to Dockerized FastAPI App!"
