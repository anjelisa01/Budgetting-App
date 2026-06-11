#make request to /users endpoints
#to test the services

from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_create_user():
    payload={
        "name": "anjelisa02",
        "email": "anjelisa02@example.com",
        "hashed_password": "anjelisa"
        }
    response=client.post(
        "/api/v1/users/signup",
        json=payload)
    assert response.status_code==200

def test_read_one_user(authenticated_client):
    response=authenticated_client.get("/api/v1/users/me")
    assert response.status_code==200

def test_update_user(authenticated_client):
    payload={
        "name": "changed", # change name to 'changed'  
        }
    response=authenticated_client.patch(
        "/api/v1/users/me",
        json=payload)
    
    assert response.status_code==200

def test_delete_user(authenticated_client):
    response=authenticated_client.delete("/api/v1/users/me")
    assert response.status_code==200
