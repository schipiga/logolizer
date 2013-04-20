from django.db import models
from logolizer.log.models import Log

class Line(models.Model):
  ip = models.CharField(max_length=15)
  time = models.CharField(max_length=32)
  request = models.CharField(max_length=64)
  code = models.IntegerField()
  host = models.CharField(max_length=64)
  agent = models.CharField(max_length=128)
  duration = models.FloatField()
  log = models.ForeignKey(Log)
