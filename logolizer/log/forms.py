from django import forms

class UploadForm(forms.Form):
  title = forms.CharField()
  file = forms.FileField()
