from datetime import datetime
from passlib.context import CryptContext
from sqlalchemy import update
from sqlalchemy.orm import Session

from auth_jwt import schemas, models


class UserView:

    def get_password_hash(self, password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(password)

    async def create(self, db: Session, user: schemas.UserCreate):
        """Сохраняем нового юзера в бд"""
        user_create = models.User(
            name=user.name,
            username=user.username,
            password=self.get_password_hash(user.password),
            photo=user.photo,
            phone=user.phone,
            url=user.url,
            about_me=user.about_me,
            create_at=datetime.now()
        )
        db.add(user_create)
        db.commit()
        db.refresh(user_create)
        return {"id": user_create.id, "name": user.name, "username": user.username}

    async def has(self, db: Session, username: str):
        """Проверяет есть ли такой юзер по username"""
        return db.query(models.User).filter(
            models.User.username == username
        ).first()

    async def update(self, db: Session, user: schemas.UserUpdate):
        """Изменить профильные данные"""
        db.execute(
            update(models.User)
            .where(models.User.id == user.id)
            .values(name=user.name,
                    photo=user.photo,
                    phone=user.phone,
                    url=user.url,
                    about_me=user.about_me
                    )
        )
        db.commit()
        # db.refresh(user_update)
        return {"id": user.id, "name": user.name, "username": user.username}

    async def delete(self, db: Session, user: schemas.UserUpdate):
        """Если пользователь удален мы его просто отключаем а не удаляем из бд"""
        db.execute(
            update(models.User)
            .where(models.User.id == user.id)
            .values(is_delete=True,
                    delete_date=datetime.now()
                    )
        )
        db.commit()
        return {"id": user.id, "name": user.name, "username": user.username}



userView = UserView()