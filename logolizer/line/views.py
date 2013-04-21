from django.shortcuts import *
from django.db.models import Count
from logolizer.log.models import Log
from logolizer.line.models import Line

def top(request, log_id):
  log = Log.objects.get(pk=log_id)
  ips = Line.objects.filter(log=log).values('ip').annotate(dcount=Count('ip')).order_by("-dcount")[:10]
  hosts = Line.objects.filter(log=log).values('host').annotate(dcount=Count('host')).order_by("-dcount")[:10]
  return render(request, 'top.html', {'ips': ips, 'hosts': hosts})

def logs_addiction(request):
  return HttpResponse('hello')

def time_of_request(request, log_id):
  return HttpResponse('hello')

def status_count(request, log_id):
  return HttpResponse('hello')

def anomalies(request, log_id):
  return HttpResponse('hello')
