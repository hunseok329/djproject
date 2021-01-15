from django.shortcuts import render
from .models import ToDoList


def todo_list(request):
    todolist = ToDoList.objects.all()
    return render(request, 'todolist/todo_list.html', {"todolist": todolist})


def todo_create(request):
    
# Create your views here.
