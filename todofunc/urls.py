from django.contrib import admin
from django.urls import path
from .views import (
    home, 
    todoList, 
    createTodo, 
    updateTodo, 
    deleteTodo,
    detailTodo
    )

app_name = 'todofunc'
urlpatterns = [
    path('', home, name='home'),
    path('list/', todoList, name='list'),
    path('create/', createTodo, name='create'),
    path('update/<int:id>/', updateTodo, name='update'),
    path('deleteTodo/<int:id>/', deleteTodo, name='delete'),
    path('<int:id>/', detailTodo, name='detail'),
]
