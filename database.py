from fastapi import FastAPI
import sqlalchemy
from databases import Database 
from datetime import datetime



DATABASE_URL = "sqlite:///./store.db"

metadata = sqlalchemy.MetaData()

database = Database(DATABASE_URL)

todo = sqlalchemy.Table(
    "Todo",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True),
    sqlalchemy.Column("task",sqlalchemy.String(500)),
    sqlalchemy.Column("description",sqlalchemy.String(500),nullable=True),
    sqlalchemy.Column("date_created",sqlalchemy.DateTime)
)

# user = sqlalchemy.Table(
#     "User",
#     metadata,
#     sqlalchemy.Column("id",sqlalchemy.Integer,primary_key = True,autoincrement= True),
#     sqlalchemy.Column("name",sqlalchemy.String(300))

# )
engine = sqlalchemy.create_engine(DATABASE_URL,connect_args={"check_same_thread": False})



def get_database() -> Database:
    return database


