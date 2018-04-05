from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    due_date = models.DateTimeField('due date')
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content
