from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task
from .processes import process_edit, process_complete, process_delete, process_create
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'index.html', context)


@login_required
def edit(request, task_id):
    response = process_edit(request, task_id)
    return JsonResponse(response)


@login_required
def complete(request, task_id):
    response = process_complete(request, task_id)
    return JsonResponse(response)


@login_required
def delete(request, task_id):
    response = process_delete(request, task_id)
    return JsonResponse(response)


@login_required
def create(request):
    response = process_create(request)
    return JsonResponse(response)
