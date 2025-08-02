from django.urls import path
from .views import ListaDeTarefas, DetalhesDaTarefa, CriarTarefa

urlpatterns = [
  path('', ListaDeTarefas.as_view(), name='tarefas'),
  path('tarefa/<int:pk>/', DetalhesDaTarefa.as_view(), name='tarefa'),
  path('criar-tarefa/', CriarTarefa.as_view(), name='criar-tarefa'),
]