from django.conf.urls import *
from logolizer.line.views import *

urlpatterns = patterns('',
  url(r'^(?P<log_id>\d+)/top/$', top, name='top'),
  url(r'^logs_addiction/$', logs_addiction, name='logs_addiction'),
  url(r'^(?P<log_id>\d+)/time_of_request/$', time_of_request, name='time_of_request'),
  url(r'^(?P<log_id>\d+)/status_count/$', status_count, name='status_count'),
  url(r'^(?P<log_id>\d+)/anomalies/$', anomalies, name='anomalies'),
)
