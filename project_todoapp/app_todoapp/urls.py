from django.urls import path
from . import views

urlpatterns = [
    path('task/create/', views.task_create, name='task.create'),
]