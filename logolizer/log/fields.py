from django import forms
from django.utils.translation import ugettext_lazy as _
from logolizer.log.parsing import parse

def is_parsable(log):
  return parse(log.readline())

class LogField(forms.FileField):
  default_error_messages = {
    'no_file': _("No file was submitted."),
    'no_format': _("File has invalid format."),
    'unparsable': _("File is not parsable."),
    'too_large': _("File size exceeded."),
  }

  def __init__(self, *args, **kwargs):
    self.max_size = kwargs.pop('max_size', None)
    super(LogField, self).__init__(*args, **kwargs)

  def to_python(self, data):
    if super(LogField, self).to_python(data) is None:
      raise forms.ValidationError(self.error_messages['no_file'])
    if data.content_type.split('/')[0] != 'text':
      raise forms.ValidationError(self.error_messages['no_format'])
    if self.max_size is not None and data.size > self.max_size:
      raise forms.ValidationError(self.error_messages['too_large'])

    try:
      is_parsable(data)
    except:
      raise forms.ValidationError(self.error_messages['unparsable'])

    return data
