from django.shortcuts import *
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from logolizer.auth.forms import *
from logolizer.log.forms import UploadForm
from logolizer.log.models import Log
from logolizer.auth.decorators import logout_required

@logout_required
def login(request):
  if request.method == 'POST':
    form = SessionForm(request.POST)
    if form.is_valid():
      user = auth.authenticate(username=form.cleaned_data['username'],
                               password=form.cleaned_data['password'])
      if user is not None:
        auth.login(request, user)
        messages.info(request, "You logged in successfully")
        return redirect(reverse('profile'))
      else:
        messages.error(request, "Invalid login or password")
    else:
      messages.error(request, "Invalid login or password")
  form = SessionForm()
  return render(request, 'login.html', {'form': form})

@logout_required
def registration(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      messages.info(request, "You were registered successfully and can log in now")
      return redirect(reverse('login'))
    else:
      messages.error(request, "Invalid registration data")
  form = UserCreationForm()    
  return render(request, "registration.html", {"form": form})

@login_required
def logout(request):
  auth.logout(request)
  messages.info(request, "You logged out successfully")
  return redirect(reverse('login'))

@login_required
def profile(request):
  logs = Log.objects.filter(user=request.user)
  form = UploadForm()
  ids = ["status_count", "top", "time_of_request", "anomalies"]
  return render(request, 'profile.html', {'user': request.user,
                                          'form': form,
                                          'ids': ids,
                                          'logs': logs})
