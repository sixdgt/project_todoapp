from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import (TaskApiView,)

urlpatterns = [
    path('users/login/', views.user_login, name='user.login'),
    path('users/register/', views.user_register, name='user.register'),
    path('tasks/', views.task_index, name='task.list'),
    path('task/create/', views.task_create, name='task.create'),
    path('task/update/', views.task_update, name='task.update'),
    path('task/show/<int:id>', views.task_show, name='task.show'),
    path('task/edit/<int:id>', views.task_edit, name='task.edit'),
    path('task/delete/<int:id>', views.task_delete, name='task.delete'),

    # api urls
    path('api/v1/tasks/', TaskApiView.as_view())
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)