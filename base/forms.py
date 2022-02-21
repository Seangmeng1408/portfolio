from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Achievment

class AchievmentForm(ModelForm):
    class Meta:
        model=Achievment
        fields='__all__'
