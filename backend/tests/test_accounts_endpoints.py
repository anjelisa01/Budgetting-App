from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.mark.create
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"account_name": "shopee paylater"}, 200),
        ({"account_name": "bri credit"}, 200),
        ({"account_name": "bni debit"}, 200),
        ({"account_name": "to be delete"}, 200)
        # ({"account_name": "bri credit"}, 409), #exception test existed account
    ],
)
def test_create_account(authenticated_client,payload,expected_status):
    response=authenticated_client.post(
        "/api/v1/accounts",
        json=payload)
    assert response.status_code==expected_status


@pytest.mark.read
def test_read_one_account(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/accounts/18") #id of account has to be own by authenticated client
    assert response.status_code==200

@pytest.mark.read
def test_read_all_accounts(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/accounts")
    assert response.status_code==200

@pytest.mark.update
def test_update_account(authenticated_client):
    payload={
        "account_name": "bni junio debit", 
        }
    response=authenticated_client.patch(
        "/api/v1/accounts/20", #id of account has to be own by authenticated client
        json=payload)
    assert response.status_code==200

@pytest.mark.delete
def test_delete_account(authenticated_client):
    response=authenticated_client.delete(
        "/api/v1/accounts/21") #id of account has to be own by authenticated client
    assert response.status_code==200