#make request to /users endpoints
#to test the services

from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_login():
    payload={
        "email": "anjel@example.com",
        "password":"anjel"  
        }
    response=client.post(
        '/api/v1/auth/login',
        json=payload)
    
    assert response.status_code==200
