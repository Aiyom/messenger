from fastapi import FastAPI

from auth_jwt.urls import router_user
from config import migrations


app = FastAPI()


@app.on_event("startup")
async def startup():
    migrations.Migrations()


app.include_router(router_user, prefix="/users", tags=["users"])


@app.on_event("shutdown")
async def shutdown():
    ...
