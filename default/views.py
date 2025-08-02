from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarefa

class ListaDeTarefas(ListView):
    model = Tarefa
    context_object_name = 'tarefas'

class DetalhesDaTarefa(DetailView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'default/tarefa.html'
