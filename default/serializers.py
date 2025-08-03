from rest_framework import serializers
from .models import Tarefa
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Isso é essencial
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']  # Aqui deve usar create_user, não create
        )
        return user

class TarefaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'title', 'description', 'complete', 'create']
        read_only_fields = ['user', 'create']