from django.conf.urls import *
from logolizer.line.views import *

urlpatters = patterns('',
  url(r'^top/$', top, name='top'),
  url(r'^logs_addiction/$', logs_addiction, name='logs_addiction'),
  url(r'^(?P<log_id>)/time_of_request/$', time_of_request, name='time_of_request'),
  url(r'^(?P<log_id>)/status_count/$', status_count, name='status_count'),
  url(r'^(?P<log_id>)/anomalies/$', anomalies, name='anomalies'),
)
