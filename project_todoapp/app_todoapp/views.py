from datetime import date, datetime
from operator import imod
from django.shortcuts import redirect, render

from django.core.mail import send_mail

from .forms import LoginForm, RegisterForm, TaskCreateForm

from .models import Task

# Create your views here.
def user_register(request):
    if request.method == "POST":
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            # storing session
            request.session.setdefault('user_session', request.POST.get('email'))
            # request.session['user_session'] = request.POST.get('email')
            return redirect('task.list')
        else:
            return redirect('user.register')
    else:
        reg_form = RegisterForm()
        context = {'form': reg_form}
        return render(request, 'users/register.html', context)

def user_login(request):
    if request.method == "POST":
        return render(request, 'users/login.html')
    else:
        login_form = LoginForm()
        context = {'form': login_form}
        return render(request, 'users/login.html', context)

def task_index(request):
    if request.session.has_key('user_session'):
        tasks = Task.objects.all()
        context = {
            "tasks": tasks,
            "title" : "TASK List",
            "body_title": "Todo App | TASK List"
        }
        template = "tasks/index.html"
        return render(request, template, context)
    else:
        return redirect('user.login')

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
        return redirect('task.list')
    else:
        return redirect('task.list')

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

    return redirect('task.list')

def task_create(request):
    if request.method == "POST":
        # task = Task()
        # task.task_title = request.POST.get('task_title')
        # task.task_desc = request.POST.get('task_desc')
        # task.task_category = request.POST.get('task_category')
        # task.assigned_by = request.POST.get('assigned_by')
        # task.assigned_to = request.POST.get('assigned_to')
        # task.task_assign_date = request.POST.get('task_assign_date')
        # task.task_end_date = request.POST.get('task_end_date')
        # task.created_at = datetime.now()
        # task.save()
        try:
            form = TaskCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # email sending
                send_mail(
                    'Task Assignment:-' + form.task_title,
                    'You are assgined to new task. Assigned date:- ' + str(form.created_at),
                    'c4crypt@gmail.com',
                    [form.assigned_to]
                )

                return redirect('task.list')
            else:
                return render(request, 'tasks/create.html', {'error': form})
        except:
            return render(request, 'tasks/create.html', {'error': form})
    else:
        template = "tasks/create.html"
        create_form = TaskCreateForm()
        context = {
            "title" : "TASK Create",
            "body_title": "Todo App | TASK CREATE",
            "form": create_form
        } # it is optional
        return render(request, template, context)
