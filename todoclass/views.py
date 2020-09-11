from django.shortcuts import render, get_object_or_404
from todofunc.models import TodoItem
from todofunc.forms import TodoForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class TodoListView(ListView):
    template_name = 'todoclass/todoclass-list.html'
    context_object_name = 'object'
    queryset = TodoItem.objects.order_by('complete')

class TodoDetailView(DetailView):
    template_name = 'todoclass/todoclass-detail.html'
    queryset = TodoItem.objects.all()

class TodoCreateView(CreateView):
    template_name = 'todoclass/todoclass-create.html'
    form_class = TodoForm
    queryset = TodoItem.objects.all() # <blog>/<modelname>_list.html
    success_url = reverse_lazy('todoclass:list' ) # default will redirect to get_absolute_url

    def form_valid(self, form):
        return super().form_valid(form)

class TodoUpdateView(UpdateView):
    template_name = 'todoclass/todoclass-update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todoclass:list' ) # default will redirect to get_absolute_url

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(TodoItem, id=pk)

    def form_valid(self, form):
        return super().form_valid(form)

class TodoDeleteView(DeleteView):
    template_name = 'todoclass/todoclass-delete.html'
    success_url = reverse_lazy('todoclass:list' ) # default will redirect to get_absolute_url

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(TodoItem, id=pk)