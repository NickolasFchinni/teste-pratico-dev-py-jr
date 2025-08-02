from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Tarefa

class CustomLoginView(LoginView):
    template_name = 'default/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tarefas')

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

class DeletarTarefa(DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    success_url = reverse_lazy('tarefas')
