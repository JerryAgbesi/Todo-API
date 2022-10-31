from fastapi import FastAPI,HTTPException,Form
from pydantic import BaseModel

app = FastAPI(title="Todo API")

class Todo(BaseModel):
    # todo_id: int
    name:str
    due_date:str
    description:str

fake_db = []


@app.get("/")
async def home():
    return {"route":"Home"}

@app.post("/todo/")
async def create_todo(todo:Todo):
    fake_db.append(todo)
    return todo

@app.get("/todo",response_model=list[Todo])
async def get_todos():
    return fake_db

@app.get("/todo/{id}")
async def get_todo(id:int):
    try:
        return fake_db[id]
    except:
        return HTTPException(status_code=404)   

@app.put("/todo/{id}")
async def update_todo(id:int,todo:Todo):
    try:
        fake_db[id] = todo
        return fake_db[id]
    except:
        return HTTPException(status_code=404,detail="Could not update Todo")

@app.delete("/todo/{id}")
async def delete_todo(id:int):
    try:
        victim = fake_db[id]
        fake_db.pop(id)
        return victim
    except:
        return HTTPException(status_code=404,detail="Could not delete Todo")

# @app.post("/meal")
# async def home(name:str = Form(...),origin:str = Form(...)):
#     return {"name":name,"origin":origin}



