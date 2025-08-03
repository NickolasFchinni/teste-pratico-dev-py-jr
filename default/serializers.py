from rest_framework import serializers
from .models import Tarefa
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TarefaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'title', 'description', 'complete', 'create']
        read_only_fields = ['user', 'create']