from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('todo_create', views.todo_create, name="todo_create"),
    path('todo_delete/<int:pk>', views.todo_delete, name="todo_delete")
]