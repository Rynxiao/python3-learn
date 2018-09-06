#!/usr/bin/env python3
path = '/Users/yhhu/Documents/coding/pythoncode'

try:
  f = open(path + '/hello.py', 'r')
  print(f.read())
finally:
  if f:
    f.close()

with open(path + '/print.py', 'r') as f:
  print(f.read())

with open(path + '/print.py', 'r') as f:
  for line in f.readlines():
    print(line.strip())

# 读取二进制
# f = open('/Users/michael/test.jpg', 'rb')
# f.read()

# encoding
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# write
with open(path + '/io/test.txt', 'w') as f:
  f.write('Hello, python3!')

# append
with open(path + '/io/test.txt', 'a') as f:
  f.write('\nAppend string')