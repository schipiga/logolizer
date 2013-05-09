import re

def parse(line):
  ip = line.split(" ")[0]
  time = re.search('\[(.+)\]', line).group(1)
  elems = re.findall('"([^"]+)"', line)
  reqwest = elems[0]
  host = elems[1]
  agent = elems[2]
  code = re.search('" (\d+) ', line).group(1)
  duration = re.search('" (\d+\.\d+)', line).group(1)
  return (ip, time, reqwest, code, host, agent, duration)
