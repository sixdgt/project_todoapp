from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_index, name='task.list'),
    path('task/create/', views.task_create, name='task.create'),
    path('task/show/<int:id>', views.task_show, name='task.show'),
    path('task/edit/<int:id>', views.task_edit, name='task.edit'),
    path('task/delete/<int:id>', views.task_delete, name='task.delete'),
]