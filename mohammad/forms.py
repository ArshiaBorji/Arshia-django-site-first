from django import forms
from django.forms import ModelForm
from .models import *
from django.db import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'