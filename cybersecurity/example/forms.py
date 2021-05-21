from django import forms
from .models import Todo
from django.db import models

class TodoForm(forms.ModelForm):
    details = models.TextField()
    class Meta:
        model = Todo
        fields = '__all__'