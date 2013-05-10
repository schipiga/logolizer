import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "logolizer.settings")

import sys
import magic
from shutil import copyfile
from getpass import getpass
from django.contrib import auth
from django.core.files.uploadedfile import UploadedFile
from logolizer.log.models import Log
from logolizer.log.forms import UploadForm

login = raw_input("login: ")
pswd = getpass()

user = auth.authenticate(
  username=login,
  password=pswd
)

if user is not None:
  title = raw_input("title: ")
  path = raw_input("path to file: ")
  
  try:
    mime = magic.Magic(mime=True)
    content_type = mime.from_file(path)
    size = os.path.getsize(path)

    log_file = UploadedFile(open(path), path, content_type, size)
  except Exception, e:
    print e
    exit(1)

  form = UploadForm({"title": title}, {"file": log_file})

  if form.is_valid():
    log = Log(title=form.cleaned_data['title'],
              file=form.cleaned_data['file'],
              user=user)
    log.save()
    print "Successfully uploaded. Parse results are available via web interface"
    exit(0)
  else:
    print "There are some errors:\n", form.errors.as_text()
    exit(1)
else:
  print "Invalid login or password"
  exit(1)
