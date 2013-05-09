from django import forms
from logolizer.log.fields import LogField

class UploadForm(forms.Form):
  title = forms.CharField(min_length=5, max_length=40)
  file = LogField(max_size=(200 * 1024 * 1024))
