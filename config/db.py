import logging
import typing
from contextlib import contextmanager, AbstractContextManager
from typing import Callable

import databases as databases
import sqlalchemy
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base, as_declarative
from sqlalchemy.orm import Session, sessionmaker, declared_attr

from config.settings import *

# from settings import *

#подключение к postgresql
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PWD}@{DB_IP}:{DB_PORT}/{DB_NAME}"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()