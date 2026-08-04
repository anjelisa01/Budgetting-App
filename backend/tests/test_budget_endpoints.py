from fastapi.testclient import TestClient
from main import app

import pytest

@pytest.mark.create2
def test_create_budget(authenticated_client):
    payload={
            "limit": 200,
            "period":"monthly"
            }
    response=authenticated_client.post(
        "/api/v1/categories/28/budget", #category_id from authenticated client
        json=payload)
    assert response.status_code==200

@pytest.mark.read2
def test_read_one_budget(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/categories/28/budget")
    assert response.status_code==200

@pytest.mark.update2
def test_update_budget(authenticated_client):
    payload={
        "limit": "5000", # change
        }
    response=authenticated_client.patch(
        "/api/v1/categories/28/budget",
        json=payload)
    assert response.status_code==200

#dont need to provide budget id, since category and budget is 1to1, so select by category id is enough
@pytest.mark.delete2
def test_delete_budget(authenticated_client):
    response=authenticated_client.delete(
        "/api/v1/categories/28/budget")
    assert response.status_code==200    