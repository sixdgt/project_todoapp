from django.contrib import admin

from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_desc', 'task_category', 'task_assign_date', \
        'task_end_date', 'assigned_by', 'assigned_to')
    list_filter = ('task_title', 'task_assign_date')
    search_fields = ('task_title', 'task_assign_date')

admin.site.register(Task, TaskAdmin)

# customizing site titles
admin.site.site_header = "Todo App" # brand name
admin.site.site_title = "Admin Dashboard" # title
admin.site.index_title = "Todo App" # page title

