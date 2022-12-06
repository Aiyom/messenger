import sqlalchemy

from config.db import Base


class User(Base):
    __tablename__ = "user"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    username = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String)
    url = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about_me = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    create_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    is_delete = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    delete_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
