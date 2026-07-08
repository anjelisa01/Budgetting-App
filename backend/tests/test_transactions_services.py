
from fastapi.testclient import TestClient
from main import app

import pytest

# client=TestClient(app)

@pytest.mark.cr
def test_create_transaction(authenticated_client):
    payload={
        "title": "string",
        "amount": 0,
        "note": "string"
        }
    response=authenticated_client.post(
        "/api/v1/transactions",
        json=payload)
    assert response.status_code==200

@pytest.mark.cr
def test_read_one_transaction(authenticated_client):
    response=authenticated_client.get("/api/v1/transactions/13")
    assert response.status_code==200

@pytest.mark.cr
def test_read_all_transaction(authenticated_client):
    response=authenticated_client.get("/api/v1/transactions")
    assert response.status_code==200

@pytest.mark.cr
def test_update_transaction(authenticated_client):
    payload={
        "note": "changed", # change name to 'changed'  
        }
    response=authenticated_client.patch(
        "/api/v1/transactions/13",
        json=payload)
    
    assert response.status_code==200

@pytest.mark.cr
def test_delete_transaction(authenticated_client):
    response=authenticated_client.delete("/api/v1/transactions/25")
    assert response.status_code==200