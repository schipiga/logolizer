import re
from django.shortcuts import *
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from logolizer.log.forms import UploadForm
from logolizer.log.models import Log
from logolizer.line.models import Line

@login_required
def upload(request):
  if request.method == "POST":
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
      log = Log(title=form.cleaned_data['title'],
                file=form.cleaned_data['file'],
                user=request.user)
      log.save()
      parse(log)
      messages.info(request, "File was upload successfully")
    else:
      messages.error(request, "Invalid title or file")
  else:
    messages.error(request, "Use POST request")
  return redirect(reverse('profile'))

def parse(log):
  f = open(log.file.path)
  lines = f.readlines()
  f.close()
  for line in lines:
    l = Line()
    l.ip = line.split(" ")[0]
    l.time = re.search('\[(.+)\]', line).group(1)
    elems = re.findall('"([^"]+)"', line)
    l.request = elems[0]
    l.host = elems[1]
    l.agent = elems[2]
    l.code = re.search('" (\d+) ', line).group(1)
    l.duration = re.search('" (\d+\.\d+)', line).group(1)
    l.log = log
    l.save()
