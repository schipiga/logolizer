from django.shortcuts import *
from django.db.models import Count
from logolizer.log.models import Log
from logolizer.line.models import Line

def top(request, log_id):
  log = Log.objects.get(pk=log_id)
  ips = Line.objects.filter(log=log).values('ip').annotate(dcount=Count('ip')).order_by("-dcount")[:10]
  hosts = Line.objects.filter(log=log).values('host').annotate(dcount=Count('host')).order_by("-dcount")[:10]
  return render(request, 'top.html', {'ips': ips, 'hosts': hosts})

def addiction(request):
  logs = Log.objects.filter(user=request.user).only('title', 'created_at')
  return render(request, 'logs_addiction.html', {'logs': logs})

def time_of_request(request, log_id):
  log = Log.objects.get(pk=log_id)
  durations = Line.objects.filter(log=log).only('duration')
  return render(request, 'time_of_request.html', {'durations': durations})

def status_count(request, log_id):
  log = Log.objects.get(pk=log_id)
  statuses = Line.objects.filter(log=log).values('code').annotate(dcount=Count('code'))
  return render(request, 'status_count.html', {'statuses': statuses})

def anomalies(request, log_id):
  return HttpResponse('hello')
