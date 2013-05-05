from django import forms

class UploadForm(forms.Form):
  title = forms.CharField(min_length=5, max_length=40)
  file = forms.FileField()
