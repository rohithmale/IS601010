from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Project_model(forms.Form):
        title = forms.CharField(max_length=100)
        description = forms.CharField(max_length=1000)
        year = forms.DateField()

class UserRegistationForm(UserCreationForm):
        email = forms.EmailField()
        first_name = forms.CharField(max_length=50)
        last_name = forms.CharField(max_length=50)

class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
