from dataclasses import dataclass

from config.db import engine
from auth_jwt import models as auth_models


@dataclass
class Migrations:
    def __init__(self):
        self.create_table()

    def create_table(self):
        auth_models.Base.metadata.create_all(bind=engine)