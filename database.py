from fastapi import FastAPI,depends
import sqlalchemy
import databases
from datetime import datetime
from pydantic import BaseModel,Field
from main import app

DATABASE_URL = "sqlite:///./store.db"

metadata = sqlalchemy.MetaData()

db = databases.Database(DATABASE_URL)

todo = sqlalchemy.table(
    "Todo",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("task",sqlalchemy.String(500)),
    sqlalchemy.Column("description",sqlalchemy.String(500),nullable=True),
    sqlalchemy.Column("date_created",sqlalchemy.DateTime)
)

engine = sqlalchemy.create_engine(DATABASE_URL,connect_args={"check_same_thread": False})

metadata.create_all(engine)


