from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from .forms import TodoForm

def home(request):
    return render(request, 'home.html')

def todoList(request):
    all_todo_items = TodoItem.objects.order_by('complete')
    context = {
                'object': all_todo_items
            }
    return render(request, 'todofunc/todofunc-list.html', context)

def createTodo(request):
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todofunc:list')
    context = {'form':form}
    return render(request, 'todofunc/todofunc-create.html', context)

def updateTodo(request, id):
    todo = TodoItem.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method =='POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todofunc:list')
    context = {'form':form}
    return render(request, 'todofunc/todofunc-update.html', context)

def detailTodo(request, id):
    todo = TodoItem.objects.get(id=id)
    context = {'object':todo}
    return render(request, 'todofunc/todofunc-detail.html', context)

def deleteTodo(request, id):
    todo = TodoItem.objects.get(id=id)

    if request.method == 'POST':
        todo.delete()
        return redirect('todofunc:list')

    context = {'object':todo}
    return render(request, 'todofunc/todofunc-delete.html', context)