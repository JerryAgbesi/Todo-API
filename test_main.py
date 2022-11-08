from fastapi import FastAPI,HTTPException,Depends
from fastapi.testclient import TestClient
from main import app

test_client = TestClient(app)



#test the post route for a status code of 200
def test_create_todo():
    response = test_client.post("/todo",json={
        
    "task":"Buy a wireless keyboard",
    "description":""

    })
    assert response.status_code == 201
    
#test the get route for a status code of 200
def test_get_todo():
    response = test_client.get('/todo/2')
    assert response.status_code == 200
    assert response.json() == {
    "id": 2,
    "task": "read a book",
    "description": "Finish a book for the month",
    "date_created": "2022-11-08T13:44:47.900453"
}

#Test the update of a todo item 
def test_update_todo():
    response = test_client.patch("/todo/3",json={
        "task":"Walk the dog",
        "description":"Walk the dog"
    })
    assert response.status_code == 200

#Test the delete enpoint for a 204 status code
def test_delete_todo():
    response = test_client.delete("/todo/5")
    assert response.status_code == 204