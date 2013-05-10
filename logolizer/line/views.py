from django.shortcuts import *
from django.utils import simplejson
from django.db.models import Count
from logolizer.line.anomalies import anomalies as aanomalies
from logolizer.line.anomalies import avg, deviation
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

def requests_per_second(request, log_id):
  pass

def status_count(request, log_id):
  log = Log.objects.get(pk=log_id)
  statuses = Line.objects.filter(log=log).values('code').annotate(data=Count('code'))
  for status in statuses:
    status['data'] = [status['data']]
    status['name'] = status['code']
  return HttpResponse(simplejson.dumps(list(statuses)), mimetype="application/json")

def anomalies(request, log_id):
  log = Log.objects.get(pk=log_id)
  lines = Line.objects.filter(log=log).values('time').annotate(Count('time'))
  points = []
  for line in lines:
    points.append(line['time__count'])
  anomal_points = aanomalies(points)
  anomal_times = []
  for line in lines:
    if line['time__count'] in anomal_points:
      anomal_times.append(line)

  normal_points = [item for item in points if item not in anomal_points]

  avg_points = avg(normal_points)
  dev_points = round(3*deviation(normal_points))

  return render(request, 'anomalies.html', {'anomalies': anomal_times,
                                            'avg': avg_points,
                                            'dev': dev_points})
