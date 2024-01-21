"""healthchecks app tests."""
from rest_framework.test import APIClient


def test_healthcheck_endpoint():
    """Ensure health check endpoint returns 200 response"""
    client = APIClient()
    response = client.get("/healthchecks/status?format=json")
    assert response.status_code == 200
    assert response.json() == {"message": "drf-boilerplate app works!"}
