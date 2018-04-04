
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Task

def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'detail.html', {'task': task})
