from fastapi import FastAPI
from chat.chat import chat_router

app = FastAPI()
app.include_router(chat_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
