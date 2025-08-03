import pytest
from default.serializers import UserSerializer, TarefaSerializer
from default.models import Tarefa
from django.contrib.auth.models import User
from datetime import datetime

@pytest.mark.django_db
def test_user_serializer_create():
    data = {
        "username": "testuser",
        "password": "strongpassword123"
    }
    serializer = UserSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert user.pk is not None
    assert user.username == data["username"]
    # A senha não fica exposta no serializer
    assert "password" not in serializer.data

@pytest.mark.django_db
def test_tarefa_serializer():
    user = User.objects.create_user(username="user1", password="pass")
    tarefa = Tarefa.objects.create(
        user=user,
        title="Minha tarefa",
        description="Descrição da tarefa",
        complete=False,
        create=datetime.now()
    )
    serializer = TarefaSerializer(instance=tarefa)
    data = serializer.data

    assert data["id"] == tarefa.id
    assert data["user"]["username"] == user.username
    assert data["title"] == tarefa.title
    assert data["description"] == tarefa.description
    assert data["complete"] == tarefa.complete
    # 'create' deve estar presente e ser uma string (isoformat)
    assert isinstance(data["create"], str)