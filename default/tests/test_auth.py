import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    response = client.post("/register/", {
        "username": "testuser",
        "password": "strongpassword123"
    })
    assert response.status_code == 201
    assert User.objects.filter(username="testuser").exists()

@pytest.mark.django_db
def test_user_login_returns_token():
    User.objects.create_user(username="testuser", password="testpass")
    client = APIClient()
    response = client.post("/api-token-auth/", {
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "token" in response.data