from django.db import models

# Create your models here.
class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICE = (
        (TODO, 'ToDo'),
        (DONE, 'Done'),
    )
    title = models.CharField(verbose_name="Task Title", max_length=50, null=False)
    description = models.TextField(verbose_name="Task Description", null=False)
    status = models.CharField(verbose_name="Status", max_length=10, choices=STATUS_CHOICE, default=TODO, null=False)
    created_date = models.DateTimeField(verbose_name="When Created", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="When Modified", auto_now=True)

    def __str__(self):
        return self.title