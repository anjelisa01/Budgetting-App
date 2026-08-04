from fastapi.testclient import TestClient
from main import app

import pytest

@pytest.mark.create
@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({
            "goal_name":"buy iphone kuffi",
            "target_amount":1800,
            "saved_amount":200,
            "due_date":"2026-08-22T14:30:00Z" }, 
            200),
        ({
            "goal_name":"travel thailand",
            "target_amount":3000,
            "saved_amount":100,
            "due_date":"2026-12-22T14:30:00Z" }, 
            200),
        ({
            "goal_name":"to be deleted",
            "target_amount":3000,
            "saved_amount":200,
            "due_date":"2026-12-22T14:30:00Z" }, 
            200)
    ],
)
def test_create_goal(authenticated_client,payload,expected_status):
    response=authenticated_client.post(
        "/api/v1/goals",
        json=payload)
    assert response.status_code==expected_status


@pytest.mark.readonegoal
def test_read_one_goal(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/goals/111") #goal id has to be existed for authentucated client
    assert response.status_code==200

@pytest.mark.read
def test_read_all_goals(authenticated_client):
    response=authenticated_client.get(
        "/api/v1/goals")
    assert response.status_code==200

@pytest.mark.update
def test_update_goal(authenticated_client):
    payload={
        "saved_amount":400, # change 
        }
    response=authenticated_client.patch(
        "/api/v1/goals/9",
        json=payload)
    assert response.status_code==200

@pytest.mark.delete
def test_delete_goal(authenticated_client):
    response=authenticated_client.delete(
        "/api/v1/goals/11")
    assert response.status_code==200