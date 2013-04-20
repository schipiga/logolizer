from django.conf.urls import patterns, include, url
from logolizer.auth.views import *
from logolizer.log.views import *
from logolizer.line import urls

urlpatterns = patterns('',
  url(r'^$', login, name='login'),
  url(r'^profile/$', profile, name='profile'),
  url(r'^logout/$', logout, name='logout'),
  url(r'^upload/$', upload, name='upload'),
  url(r'^logs/', include(urls)),
)
