from datetime import date, datetime
from operator import imod
from django.shortcuts import render

from .forms import TaskCreateForm

from .models import Task

# Create your views here.
def task_create(request):
    if request.method == "POST":
        task = Task()
        task.task_title = request.POST.get('task_title')
        task.task_desc = request.POST.get('task_desc')
        task.task_category = request.POST.get('task_category')
        task.assigned_by = request.POST.get('assigned_by')
        task.assigned_to = request.POST.get('assigned_to')
        task.task_assign_date = request.POST.get('task_assign_date')
        task.task_end_date = request.POST.get('task_end_date')
        task.created_at = datetime.now()
        task.save()

        template = "tasks/index.html"
        context = {
            "title" : "TASK List",
            "body_title": "Todo App | TASK List"
        }
        return render(request, template, context)
    else:
        template = "tasks/create.html"
        create_form = TaskCreateForm()
        context = {
            "title" : "TASK Create",
            "body_title": "Todo App | TASK CREATE",
            "form": create_form
        } # it is optional
        return render(request, template, context)
