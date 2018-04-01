
from django.http import HttpResponse
from django.template import loader
from .models import Task

def index(request):
    tasks_list = Task.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tasks_list': tasks_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, task_id):
    response = "Task %s: "
    return HttpResponse(response % task_id)
