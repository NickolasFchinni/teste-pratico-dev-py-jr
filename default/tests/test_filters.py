import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from default.models import Tarefa
from datetime import date

@pytest.fixture
def user_token():
    user = User.objects.create_user(username="user", password="123456")
    client = APIClient()
    res = client.post("/api-token-auth/", {"username": "user", "password": "123456"})
    assert res.status_code == 200, res.content
    token = res.data["token"]
    client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
    return client, user

@pytest.mark.django_db
def test_filter_by_complete(user_token):
    client, user = user_token
    Tarefa.objects.create(user=user, title="T1", complete=False)
    Tarefa.objects.create(user=user, title="T2", complete=True)

    res = client.get("/tarefas/?complete=true")
    assert all(t["complete"] is True for t in res.data["results"])

@pytest.mark.django_db
def test_filter_by_date(user_token):
    client, user = user_token
    today = date.today()
    Tarefa.objects.create(user=user, title="Hoje", create=today)
    Tarefa.objects.create(user=user, title="Outro dia", create="2020-01-01")

    res = client.get(f"/tarefas/?create={today}")
    assert all(t["create"] == today.isoformat() for t in res.data["results"])
