from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task
from .processes import process_edit, process_complete, process_delete, process_create


def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'detail.html', {'task': task})


def edit(request, task_id):
    response = process_edit(request, task_id)
    return JsonResponse(response)


def complete(request, task_id):
    response = process_complete(request, task_id)
    return JsonResponse(response)


def delete(request, task_id):
    response = process_delete(request, task_id)
    return JsonResponse(response)


def create(request):
    response = process_create(request)
    return JsonResponse(response)
