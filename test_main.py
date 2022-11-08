from fastapi import FastAPI,HTTPException,Depends
from fastapi.testclient import TestClient
from main import app

test_client = TestClient(app)



def test_get_todos():
    response = test_client.get('/todo')
    assert response.status_code == 200
    # assert response.json() == {"message":"root read successful"}