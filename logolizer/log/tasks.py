import logging
from celery import task
from logolizer.log.models import Log
from logolizer.log.parsing import parse
from logolizer.line.models import Line
from django.db import connection, transaction

@task()
def parse(log_id):
  logger = logging.getLogger(__name__)
  cursor = connection.cursor()
  log = Log.objects.get(pk=log_id)
  for line in lines(log):
    try:
      cursor.execute(
        "INSERT INTO line_line(ip, time, request, code, host, agent, duration, is_parsed, log_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        parse(line) + (False, log_id)
      )
    except:
      logger.error("Can't parse log line: %s", line)

def lines(log):
  f = open(log.file.path)
  lines = f.readlines()
  f.close()
  return lines
