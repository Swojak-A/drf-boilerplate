from rest_framework.test import APIClient
from django.urls import reverse


def test_healthcheck_endpoint():
    client = APIClient()
    response = client.get(reverse("api:healthchecks:status"))
    assert response.status_code == 200
    assert response.json() == {"message": "drf-boilerplate app works!"}
