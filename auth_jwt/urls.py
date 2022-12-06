#db = SessionLocal()
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth_jwt import schemas
from auth_jwt.views import userView
from config.db import get_db

router_user = APIRouter()


@router_user.post("/create_user", response_model=schemas.UserBase)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """api для создание нового юзера"""
    db_user = await userView.has(
        db,
        username=user.username
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Такая отделание уже создана")
    return await userView.create(db=db, user=user)


@router_user.put("/update_user", response_model=schemas.UserBase)
async def create_user(user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """api для изменение юзера"""
    db_user = await userView.has(
        db,
        username=user.username
    )
    if not db_user:
        raise HTTPException(status_code=400, detail="Пользователь не найден")
    return await userView.update(db=db, user=user)


@router_user.delete("/delete_user", response_model=schemas.UserBase)
async def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    """api для отклю юзера"""
    db_user = await userView.has(
        db,
        username=user.username
    )
    if not db_user:
        raise HTTPException(status_code=400, detail="Пользователь не найден")
    return await userView.delete(db=db, user=user)