from django.urls import path
from . import views

urlpatterns = [
  path('', views.listaDeTarefas, name='tarefas'),
]