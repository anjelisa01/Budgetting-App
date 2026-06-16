#to test the services
#strictly to test auth endpoint, even tho in conftest do the same thing but dynamic

from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

import pytest
@pytest.mark.login
def test_login():
    payload={
        "email": "anjeli@example.com",
        "password":"anjeli"  
        }
    response=client.post(
        '/api/v1/auth/login',
        json=payload)
    
    assert response.status_code==200
