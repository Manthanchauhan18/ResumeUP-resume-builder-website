from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ResumeData, CoverLetter


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeData
        fields = "__all__"


class CoverForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = "__all__"

