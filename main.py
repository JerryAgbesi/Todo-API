from datetime import datetime
from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel,Field
from database import todo,get_database,database,Database,metadata,engine




app = FastAPI(title="Todo API")


class TodoIn(BaseModel):
    task: str
    description: str
    date_created: datetime = datetime.utcnow()

class Todo(BaseModel):
    id: int 
    task: str
    description: str
    date_created: datetime
  


   

async def get_todo_or_404(id: int, database: Database = Depends(get_database)) -> Todo :
    select_query = todo.select().where(todo.c.id == id)
    print(select_query)
    raw_post = await database.fetch_one(select_query)
   

    if raw_post is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

    return Todo(**raw_post)  

async def pagination(skip: int = 0,limit: int = 3)-> tuple[int,int]:
    return (skip,limit)


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

@app.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(t:TodoIn,database: Database = Depends(get_database)):
    post_query = todo.insert().values(t.dict())
    record_id = await database.execute(post_query)
    row = await get_todo_or_404(record_id,database)

    return row

@app.get("/todo/{id}",response_model=Todo)
async def get_todos(todoDB: Todo = Depends(get_todo_or_404), database: Database = Depends(get_database)) -> Todo:
    select_query = todo.select().where(todo.c.id == todoDB.id)
    row =  await database.fetch_one(select_query)
    

    return Todo(**row)  
     

@app.get("/todo")
async def get_todos(pagination: tuple[int,int] = Depends(pagination),database: Database = Depends(get_database)) -> list[Todo]:
    skip,limit = pagination
    select_query = todo.select().offset(skip).limit(limit)
    rows =  await database.fetch_all(select_query)
    result = [Todo(**row) for row in rows ] 

    return result


#Update a todo
@app.patch("/todo/{id}")
async def update_todo(t: TodoIn,todoDB:Todo = Depends(get_todo_or_404),database: Database = Depends(get_database))-> Todo:
    update_query = todo.update().where(todo.c.id == todoDB.id).values(t.dict(exclude_unset=True))
    todo_id = await database.execute(update_query)

    response = await get_todo_or_404(todo_id,database)

    return response

@app.delete("/todo/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todoDB: Todo = Depends(get_todo_or_404),database: Database = Depends(get_database)):
    delete_query = todo.delete().where(todo.c.id == todoDB.id)
    await database.execute(delete_query)



