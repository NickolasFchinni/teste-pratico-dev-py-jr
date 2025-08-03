import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from default.models import Tarefa

@pytest.fixture
def user_token():
    user = User.objects.create_user(username="user", password="123456")
    client = APIClient()
    res = client.post("/api-token-auth/", {"username": "user", "password": "123456"})
    token = res.data["token"]
    return user, token

@pytest.mark.django_db
def test_create_task(user_token):
    user, token = user_token
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token)

    response = client.post("/tarefas/", {
        "title": "Nova tarefa",
        "description": "descrição",
        "complete": False
    })

    assert response.status_code == 201
    assert Tarefa.objects.filter(user=user).count() == 1

@pytest.mark.django_db
def test_update_task(user_token):
    user, token = user_token
    tarefa = Tarefa.objects.create(user=user, title="Teste", description="desc")

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token)

    response = client.patch(f"/tarefas/{tarefa.id}/", {
        "complete": True
    })
    assert response.status_code == 200
    tarefa.refresh_from_db()
    assert tarefa.complete is True

@pytest.mark.django_db
def test_delete_task(user_token):
    user, token = user_token
    tarefa = Tarefa.objects.create(user=user, title="Tarefa", description="desc")

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token)

    response = client.delete(f"/tarefas/{tarefa.id}/")
    assert response.status_code == 204
    assert not Tarefa.objects.filter(id=tarefa.id).exists()
