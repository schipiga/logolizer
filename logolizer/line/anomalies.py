from math import *

MIN_COUNT = 2

def anomalies(data):
  global min_bound_locked, max_bound_locked
  min_bound_locked = max_bound_locked = False
  data.sort()
  return calculate_anomalies(data, [])

def calculate_anomalies(data, anomals_list):
  if len(data) <= MIN_COUNT:
    return anomals_list
  x = find_potential_anomaly(data)
  data.remove(x['number'])
  if check(x, data):
    anomals_list.append(x['number'])
  if min_bound_locked and min_bound_locked:
    return anomals_list
  else:
    return calculate_anomalies(data, anomals_list)

def find_potential_anomaly(data):
  first, second, penult, last = data[0], data[1], data[-2], data[-1]
  if min_bound_locked:
    return {'number': last, 'position': 'last'}
  if max_bound_locked:
    return {'number': first, 'position': 'first'}
  if (second - first) > (last - penult):
    return {'number': first, 'position': 'first'}
  else:
    return {'number': last, 'position': 'last'}

def check(x, data):
  global min_bound_locked, max_bound_locked

  a = avg(data)
  sigma = deviation(data)
  min = a - 3*sigma
  max = a + 3*sigma

  if x['number'] >= min and x['number'] <= max:
    if x['position'] == 'first':
      min_bound_locked = True
    if x['position'] == 'last':
      max_bound_locked = True
    return False
  else:
    min_bound_locked = max_bound_locked = False
    return True

def avg(data):
  return sum(data)/len(data)

def deviation(data):
  a = avg(data)
  x = 0
  for i in data:
    x += (i - a)**2
  return sqrt(float(x)/len(data))
