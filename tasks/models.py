from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    due_date = models.DateTimeField('due date')
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content
        
    @property
    def fmt_due_date(self):
        return self.due_date.strftime("%m/%d/%Y")
        
    @property
    def fmt_completed(self):
        return "Yes" if self.completed else "No"