from .models import Task
from datetime import datetime


def process_delete(request, task_id):
    result = Task.objects.filter(id=task_id).delete()
    return {"result": "success"} if result[0] == 1 else {"result": "failure"}


def process_edit(request, task_id):
    updated_content = request.POST['content']
    updated_due_date = datetime.strptime(request.POST['due_date'], "%m/%d/%Y")
    updated_completion_status = request.POST['completed']
    bool_completed_status = True if updated_completion_status == "Yes" else False
    count = Task.objects.filter(id=task_id).update(content=updated_content, due_date=updated_due_date,
                                                   completed=bool_completed_status)
    task = Task.objects.filter(id=task_id)
    return task if count == 1 else {"result": "failure"}


def process_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    result = Task.objects.filter(id=task_id).update(completed=not task.completed)
    return {"result": "success"} if result == 1 else {"result": "failure"}


def process_create(request):
    pass
