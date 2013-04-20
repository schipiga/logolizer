from django.shortcuts import *
from django.core.urlresolvers import reverse

def logout_required(func):
  def wrapper(request, *args, **kwargs):
    if request.user.is_authenticated():
      return redirect(reverse('profile'))
    else:
      return func(request, *args, **kwargs)
  return wrapper
