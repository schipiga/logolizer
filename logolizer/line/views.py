from django.shortcuts import *
from django.utils import simplejson
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
  durations = Line.objects.filter(log=log).values_list('duration', flat=True)[:100]
  return HttpResponse(simplejson.dumps(list(durations)), mimetype="application/json")

def status_count(request, log_id):
  log = Log.objects.get(pk=log_id)
  statuses = Line.objects.filter(log=log).values('code').annotate(data=Count('code'))
  for status in statuses:
    status['data'] = [status['data']]
    status['name'] = status['code']
  return HttpResponse(simplejson.dumps(list(statuses)), mimetype="application/json")

def anomalies(request, log_id):
  return HttpResponse('hello anomalies')
