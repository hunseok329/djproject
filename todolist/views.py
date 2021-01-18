from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList
from django.utils import timezone


def todo_list(request):
    todolist = ToDoList.objects.all()
    return render(request, 'todolist/todo_list.html', {"todolist": todolist})


def todo_create(request):
    todolist = ToDoList.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        new_todo = ToDoList(title=title, content="전송 잘됨", created_date=timezone.now())
        new_todo.save()
    return redirect('todo_list')


def todo_delete(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    todo.delete()
    return redirect('todo_list')