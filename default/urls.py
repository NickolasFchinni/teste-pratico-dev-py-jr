from django.urls import path
from .views import ListaDeTarefas, DetalhesDaTarefa

urlpatterns = [
  path('', ListaDeTarefas.as_view(), name='tarefas'),
  path('tarefa/<int:pk>/', DetalhesDaTarefa.as_view(), name='tarefas'),
]