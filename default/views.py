from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarefa

class ListaDeTarefas(ListView):
    model = Tarefa
    context_object_name = 'tarefas'

