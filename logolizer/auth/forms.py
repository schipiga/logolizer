from django import forms
from django.contrib.auth.forms import UserCreationForm

class SessionForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())

class UserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)
