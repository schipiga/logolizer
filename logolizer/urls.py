from django.conf.urls import patterns, include, url
from logolizer.auth.views import *

urlpatterns = patterns('',
  url(r'^$', login),
  url(r'^profile', profile),
  url(r'^logout', logout, name='logout'),
)
