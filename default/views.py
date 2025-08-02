from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Tarefa

class ListaDeTarefas(ListView):
    model = Tarefa
    context_object_name = 'tarefas'

class DetalhesDaTarefa(DetailView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'default/tarefa.html'

class CriarTarefa(CreateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')

class AtualizarTarefa(UpdateView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
