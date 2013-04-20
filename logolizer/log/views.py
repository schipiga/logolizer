from django.shortcuts import *
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from logolizer.log.forms import UploadForm
from logolizer.log.models import Log

@login_required
def upload(request):
  if request.method == "POST":
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
      log = Log(title=form.cleaned_data['title'],
                file=form.cleaned_data['file'],
                user=request.user)
      log.save()
      messages.info(request, "File was upload successfully")
    else:
      messages.error(request, "Invalid title or file")
  else:
    messages.error(request, "Use POST request")
  return redirect(reverse('profile'))
