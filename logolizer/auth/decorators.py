from django.shortcuts import *
from django.conf import settings

def logout_required(func):
  def wrapper(request, *args, **kwargs):
    if request.user.is_authenticated():
      return redirect(settings.PROFILE_URL)
    else:
      return func(request, *args, **kwargs)
  return wrapper
