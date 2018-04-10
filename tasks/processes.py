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
    if count == 1:
        task = Task.objects.get(id=task_id)
        return {"id": task.id, "content": task.content, "due_date": task.fmt_due_date, "completed": task.completed}
    else:
        return {"result": "failure"}


def process_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    result = Task.objects.filter(id=task_id).update(completed=not task.completed)
    return {"result": "success"} if result == 1 else {"result": "failure"}


def process_create(request):
    req_content = request.POST['task_content']
    req_due_date = datetime.strptime(request.POST['task_due_date'], "%m/%d/%Y")
    completion_status = True if request.POST['task_completed'] == "Yes" else False
    task = Task.objects.create(content=req_content, due_date=req_due_date, completed=completion_status, deleted=False, created_date=datetime.now())
    if task:
        return {"id": task.id, "content": task.content, "due_date": task.fmt_due_date, "completed": task.fmt_completed}