import os

from dotenv import load_dotenv

load_dotenv()

#доступ для подключение к бд
DB_USER = os.getenv('DB_USER')
DB_PWD = os.getenv('DB_PWD')
DB_NAME = os.getenv('DB_NAME')
DB_IP = os.getenv('DB_IP')
DB_PORT = os.getenv('DB_PORT')