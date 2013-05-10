from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SessionForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())

class UserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ("email", "username", "password1", "password2")


  def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user
