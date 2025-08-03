from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CustomAuthToken,
    UserCreate,
    TarefaListCreate,
    TarefaRetrieveUpdateDestroy
)

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('register/', UserCreate.as_view(), name='register'),
    
    path('tarefas/', TarefaListCreate.as_view(), name='tarefa-list'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroy.as_view(), name='tarefa-detail'),
]