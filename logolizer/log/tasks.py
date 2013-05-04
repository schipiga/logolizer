import re
from celery import task
from logolizer.log.models import Log
from logolizer.line.models import Line
from django.db import connection, transaction

@task()
def parse(log_id):
  log = Log.objects.get(pk=log_id)
  f = open(log.file.path)
  lines = f.readlines()
  f.close()
  cursor = connection.cursor()
  # TODO: make it easier
  log_id = log.id
  for line in lines:
    ip = line.split(" ")[0]
    time = re.search('\[(.+)\]', line).group(1)
    elems = re.findall('"([^"]+)"', line)
    request = elems[0]
    host = elems[1]
    agent = elems[2]
    code = re.search('" (\d+) ', line).group(1)
    duration = re.search('" (\d+\.\d+)', line).group(1)
    cursor.execute("INSERT INTO line_line(ip, time, request, code, host, agent, duration, is_parsed, log_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", [ip, time, request, code, host, agent, duration, False, log_id])
#  log.is_parsed = True
#  log.save()
