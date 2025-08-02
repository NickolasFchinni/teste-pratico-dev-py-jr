from django.urls import path
from .views import ListaDeTarefas

urlpatterns = [
  path('', ListaDeTarefas.as_view(), name='tarefas'),
]