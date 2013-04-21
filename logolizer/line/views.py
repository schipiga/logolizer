from django.http import HttpResponse

def top(request):
  return HttpResponse('hello')

def logs_addiction(request):
  return HttpResponse('hello')

def time_of_request(request, log_id):
  return HttpResponse('hello')

def status_count(request, log_id):
  return HttpResponse('hello')

def anomalies(request, log_id):
  return HttpResponse('hello')
