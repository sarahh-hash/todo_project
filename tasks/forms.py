from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите название'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Введите описание',
                'rows': 4
            }),
        }