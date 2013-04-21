from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
  title = models.CharField(max_length=64)
  file = models.FileField(upload_to='tmp/')
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(default=datetime.now())
