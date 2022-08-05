from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_title', 'task_desc', 'task_category', 'task_assign_date',\
             'task_end_date', 'assigned_by', 'assigned_to', 'task_file')