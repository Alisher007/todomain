from django.contrib import admin
from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

app_name = 'todoclass'
urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='delete'),
]
