
from fastapi.testclient import TestClient
from main import app

import pytest

@pytest.mark.create2
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({
            "title": "give money to sibling",
            "amount": 25,
            "note": "feeling good",
            "transaction_type":"expense",
            "category_id":28},
            200),
        ({
            "title": "buy some lipstick",
            "amount": 30,
            "note": "happpppyyyy",
            "transaction_type":"expense"},
            200),
        ({
            "title": "get some money from granpa",
            "amount": 50,
            "note": "thanks god",
            "transaction_type":"income",
            "category_id":26},
            200),
        ({
            "title": "to be delete",
            "amount": 0,
            "note": "string",
            "transaction_type":"expense"},
            200),
    ],
)
def test_create_transaction(authenticated_client,payload,expected_status):
    response=authenticated_client.post(
        "/api/v1/accounts/19/transactions",
        json=payload)
    assert response.status_code==expected_status

@pytest.mark.read2
def test_read_one_transaction(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/accounts/19/transactions/39")
    assert response.status_code==200

@pytest.mark.read2
def test_read_all_transaction(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/accounts/19/transactions")
    assert response.status_code==200

@pytest.mark.update2
def test_update_transaction(authenticated_client):
    payload={
        "title": "i changed", # change category id to 3, oreviously null(default)
        }
    response=authenticated_client.patch(
        "/api/v1/accounts/19/transactions/41",
        json=payload)
    
    assert response.status_code==200
 
@pytest.mark.delete2
def test_delete_transaction(authenticated_client):
    response=authenticated_client.delete("/api/v1/accounts/19/transactions/42")
    assert response.status_code==200