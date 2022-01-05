# per https://sqla-wrapper.scaletti.dev/sqlalchemy-wrapper/
import os
from sqla_wrapper import SQLAlchemy

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"] 
db = SQLAlchemy("postgresql://" + DB_USERNAME + ":" + DB_PASSWORD + "@localhost:5432/geoconnections")

""" db = SQLAlchemy(
    dialect="postgresql",
    user="scott",
    password="tiger",
    host="localhost",
    name="test",
) """