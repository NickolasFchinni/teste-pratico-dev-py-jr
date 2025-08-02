from django.urls import path
from .views import ListaDeTarefas, DetalhesDaTarefa, CriarTarefa, AtualizarTarefa, DeletarTarefa

urlpatterns = [
  path('', ListaDeTarefas.as_view(), name='tarefas'),
  path('tarefa/<int:pk>/', DetalhesDaTarefa.as_view(), name='tarefa'),
  path('editar-tarefa/<int:pk>/', AtualizarTarefa.as_view(), name='editar-tarefa'),
  path('deletar-tarefa/<int:pk>/', DeletarTarefa.as_view(), name='deletar-tarefa'),
  path('criar-tarefa/', CriarTarefa.as_view(), name='criar-tarefa'),
]