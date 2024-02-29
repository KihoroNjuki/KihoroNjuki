from .models import Tasks
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'completed']
