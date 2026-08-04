#strictly to test auth endpoint, 
#even tho in conftest do the same thing but dynamic
from fastapi.testclient import TestClient
from main import app
import pytest

client=TestClient(app)

@pytest.mark.signup 
def test_create_user(): 
    payload={
        "name": "erling haaland",
        "email": "erling@example.com",
        "password": "erling",
        "currency":"usd"
        }
    response=client.post(
        "/api/v1/users/signup",
        json=payload)
    assert response.status_code==200

@pytest.mark.login
def test_login():
    payload={
        "email": "erling@example.com",
        "password":"erling"  
        }
    response=client.post(
        '/api/v1/auth/login',
        json=payload)
    assert response.status_code==200
