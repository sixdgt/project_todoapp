from datetime import datetime
from django.db import models

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=500)
    task_category = models.CharField(max_length=100)
    task_assign_date = models.DateField(default=0, null=True)
    task_end_date = models.DateField(default=0, null=True)
    assigned_by = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200)
    is_removed = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=0, null=True, blank=True)
    removed_at = models.DateTimeField(default=0, null=True, blank=True)

    class Meta:
        db_table = "tbl_task"

    

