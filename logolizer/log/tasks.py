import re
from celery import task
from logolizer.log.models import Log
from logolizer.line.models import Line

@task()
def parse(log_id):
  log = Log.objects.get(pk=log_id)
  f = open(log.file.path)
  lines = f.readlines()
  f.close()
  # TODO: make it easier
  for line in lines:
    l = Line()
    l.ip = line.split(" ")[0]
    l.time = re.search('\[(.+)\]', line).group(1)
    elems = re.findall('"([^"]+)"', line)
    l.request = elems[0]
    l.host = elems[1]
    l.agent = elems[2]
    l.code = re.search('" (\d+) ', line).group(1)
    l.duration = re.search('" (\d+\.\d+)', line).group(1)
    l.log = log
    l.save()
#  log.is_parsed = True
#  log.save()
