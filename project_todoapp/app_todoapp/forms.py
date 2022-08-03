from django import forms
from .models import AppUser, Task

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_desc', 'task_category', 'task_assign_date',\
             'task_end_date', 'assigned_by', 'assigned_to', 'task_file')
        # fields = "__all__" - loads all attributes as input field

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AppUser
        fields = ('email', 'password')

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AppUser
        fields = ('name', 'email', 'password')

        