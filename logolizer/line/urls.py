from django.conf.urls import *
from logolizer.line.views import *

urlpatterns = patterns('',
  url(r'^(?P<log_id>\d+)/top/$', top, name='top'),
  url(r'^addiction/$', addiction, name='addiction'),
  url(r'^(?P<log_id>\d+)/time_of_request/$', time_of_request, name='time_of_request'),
  url(r'^(?P<log_id>\d+)/hits_per_sec/$', hits_per_sec, name='hits_sec'),
  url(r'^(?P<log_id>\d+)/status_count/$', status_count, name='status_count'),
  url(r'^(?P<log_id>\d+)/anomalies/$', anomalies, name='anomalies'),
)
