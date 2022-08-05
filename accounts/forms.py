from django import forms
from django.contrib.auth import forms
from .models import User

class UserForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('phone','quiz','answer',)