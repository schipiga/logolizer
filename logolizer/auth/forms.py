from django import forms

class SessionForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())

class RegistrationForm(forms.Form):
  email = forms.EmailField()
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
