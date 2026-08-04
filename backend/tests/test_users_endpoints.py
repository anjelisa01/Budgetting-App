#make request to /users endpoints
#testing endpoints

import pytest
from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

'''
INFO:
authenticated_client: for protected endpoints

Must do:
    - change data on signup test (make sure no duplication
      with existing data in db)
'''
#create user on test_auth_endpoints.py

@pytest.mark.r1u  
def test_read_one_user(authenticated_client):
    response=authenticated_client.get("/api/v1/users/me")
    assert response.status_code==200

@pytest.mark.udu
def test_update_user(authenticated_client):
    payload={
        "name": "jobe",   
        }
    response=authenticated_client.patch(
        "/api/v1/users/me",
        json=payload)
    assert response.status_code==200

@pytest.mark.du
def test_delete_user(authenticated_client):
    response=authenticated_client.delete("/api/v1/users/me")
    assert response.status_code==200