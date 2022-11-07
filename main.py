from datetime import datetime
from fastapi import FastAPI,HTTPException,Depends
from fastapi.testclient import TestClient
from pydantic import BaseModel,Field
from database import todo,db



app = FastAPI(title="Todo API")

@app.get('/')
async def read_root():
    return {"message":"root read successful"}











# class Todo(BaseModel):
#     id: int 
#     task: str
#     description: str
#     date_created: datetime

# class TodoIn(BaseModel):
#     task: str = Field(...)
#     description: str  = Field(...)
   


# @app.on_event("startup")
# async def startup():
#     await db.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect() 

# @app.post("/todo/",response_model=Todo)
# async def create_todo(t:TodoIn):
#     post_query = todo.insert().values(
#         task = t.task,
#         description = t.description,
#         date_created = datetime.utcnow())
#     record_id = await db.execute(post_query)
#     query = todo.select().where(todo.c.id == record_id)
#     values = {"id": record_id,"task":t.task,"description":t.description,"date":datetime.utcnow()}
#     row = await db.fetch_one(query) 
#     type(row)
#     return row        


# @app.post("/todo/",response_model=Todo)
# async def create_todo(t:TodoIn = Depends()):
#     query = todo.insert().values(
#         task = t.task,
#         description = t.description,
#         date_created = datetime.utcnow()
# )
#     record_id = await db.execute(query)
#     query = todo.select().where(todo.c.id == record_id)
#     row = await db.fetch_one(query)
#     return Todo(**row)
   

# @app.get("/todo",response_model=list[Todo])
# async def get_todos():
#     return fake_db

# @app.get("/todo/{id}")
# async def get_todo(id:int):
#     try:
#         return fake_db[id]
#     except:
#         return HTTPException(status_code=404)   

# @app.put("/todo/{id}")
# async def update_todo(id:int,todo:Todo):
#     try:
#         fake_db[id] = todo
#         return fake_db[id]
#     except:
#         return HTTPException(status_code=404,detail="Could not update Todo")

# @app.delete("/todo/{id}")
# async def delete_todo(id:int):
#     try:
#         victim = fake_db[id]
#         fake_db.pop(id)
#         return victim
#     except:
#         return HTTPException(status_code=404,detail="Could not delete Todo")

# @app.post("/meal")
# async def home(name:str = Form(...),origin:str = Form(...)):
#     return {"name":name,"origin":origin}



