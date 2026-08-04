from fastapi.testclient import TestClient
from main import app

import pytest

@pytest.mark.create
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"category_name": "gift"}, 200),
        ({"category_name": "salary"}, 200),
        ({"category_name": "charity"}, 200),
        ({"category_name": "shopping"},200),
        ({"category_name": "to be delete"}, 200)
        # ({"account_name": "bri credit"}, 409), #exception test existed account
    ],
)
def test_create_category(authenticated_client,payload,expected_status):
    response=authenticated_client.post(
        "/api/v1/categories",
        json=payload)
    assert response.status_code==expected_status


@pytest.mark.read
def test_read_one_category(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/categories/26") #category_id has to belong to the authenticated client
    assert response.status_code==200

@pytest.mark.read
def test_read_all_categories(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/categories")
    assert response.status_code==200


@pytest.mark.update
def test_update_category(authenticated_client):
    payload={
        "category_name": "side income",
        }
    response=authenticated_client.patch(
        "/api/v1/categories/27", #category_id has to belong to the authenticated client
        json=payload) 
    assert response.status_code==200

@pytest.mark.delete  
def test_delete_category(authenticated_client):
    response=authenticated_client.delete(
        "/api/v1/categories/30") #category_id has to belong to the authenticated client
    assert response.status_code==200