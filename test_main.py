from fastapi import FastAPI,HTTPException,Depends
from fastapi.testclient import TestClient
from main import app

test_client = TestClient(app)



def test_get_todo():
    response = test_client.get('/todo/2')
    assert response.status_code == 200
    assert response.json() == {
    "id": 2,
    "task": "read a book",
    "description": "Finish a book for the month",
    "date_created": "2022-11-08T13:44:47.900453"
}