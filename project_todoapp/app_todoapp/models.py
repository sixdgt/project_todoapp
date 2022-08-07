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
    assigned_to = models.EmailField(unique=True, default=None)
    task_file = models.FileField(default=None, null=True, blank=True)
    is_removed = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    removed_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.task_title

    class Meta:
        db_table = "tbl_task" 

class AppUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_user'

