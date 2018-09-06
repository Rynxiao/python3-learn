#!/usr/bin/env python3

import logging

# try
try:
  print('try...')
  r = 10 / int('a')
  print('result:', r)
except ValueError as e:
  print('ValueError:', e)
except ZeroDivisionError as e:
  print('ZeroDivisionError:', e)
else:
  print('no error!')
finally:
  print('finally...')
print('END')

class FooError(ValueError):
  pass

def foo(s):
  n = int(s)
  if n == 0:
    raise FooError('invalid value: %s' % s)
  return 10 / n

def bar(s):
  return foo(s) * 2

def main():
  try:
    bar('0')
  except Exception as e:
    print('Error:', e)
    logging.exception(e)
  finally:
    print('finally...')

# main()
# foo('0')

from functools import reduce

def str2num(s):
  try:
    return int(s)
  except:
    return float(s)

def calc(exp):
  ss = exp.split('+')
  ns = map(str2num, ss)
  return reduce(lambda acc, x: acc + x, ns)

def main1():
  r = calc('100 + 200 + 345')
  print('100 + 200 + 345 =', r)
  r = calc('99 + 88 + 7.6')
  print('99 + 88 + 7.6 =', r)

main1()
