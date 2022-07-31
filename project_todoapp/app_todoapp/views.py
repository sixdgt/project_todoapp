from datetime import date, datetime
from operator import imod
from django.shortcuts import render

from django.core.mail import send_mail

from .forms import TaskCreateForm

from .models import Task

# Create your views here.
def task_index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
        "title" : "TASK List",
        "body_title": "Todo App | TASK List"
    }
    template = "tasks/index.html"
    return render(request, template, context)

def task_show(request, id):
    task = Task.objects.get(id=id)
    context = {
        "task": task,
        "title" : "TASK Show",
        "body_title": "Todo App | TASK Show"
    }
    template = "tasks/show.html"
    return render(request, template, context)

def task_update(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST.get('id'))
        task.task_title = request.POST.get('task_title')
        task.task_desc = request.POST.get('task_desc')
        task.task_category = request.POST.get('task_category')
        task.assigned_by = request.POST.get('assigned_by')
        task.assigned_to = request.POST.get('assigned_to')
        task.task_assign_date = request.POST.get('task_assign_date')
        task.task_end_date = request.POST.get('task_end_date')
        task.updated_at = datetime.now()
        task.save()

        tasks = Task.objects.all()
        template = "tasks/index.html"
        context = {
            "tasks": tasks,
            "title" : "TASK List",
            "body_title": "Todo App | TASK List"
        }
        return render(request, template, context)
    else:
        tasks = Task.objects.all()
        template = "tasks/index.html"
        context = {
            "tasks": tasks,
            "title" : "TASK List",
            "body_title": "Todo App | TASK List"
        }
        return render(request, template, context)

def task_edit(request, id):
    task = Task.objects.get(id=id)
    context = {
        "task": task,
        "title" : "TASK Edit",
        "body_title": "Todo App | TASK Edit"
    }
    template = "tasks/edit.html"
    return render(request, template, context)

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
        "title" : "TASK List",
        "body_title": "Todo App | TASK List"
    }
    template = "tasks/index.html"
    return render(request, template, context)

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

        # email sending
        send_mail(
            'Task Assignment:-' + task.task_title,
            'You are assgined to new task. Assigned date:- ' + str(task.created_at),
            'c4crypt@gmail.com',
            [task.assigned_to]
        )

        tasks = Task.objects.all()
        template = "tasks/index.html"
        context = {
            "tasks": tasks,
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
