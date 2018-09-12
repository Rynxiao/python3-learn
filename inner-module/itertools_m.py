#!/usr/bin/env python3

import itertools
from functools import reduce

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
  print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
  print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
  print(key, list(group))

def pi(N):
  ' 计算pi的值 '
  # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
  natuals = itertools.count(1, 2)
  # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
  ns = itertools.takewhile(lambda x: x <= 2 * N, natuals)
  # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
  l = []
  for index, i in enumerate(ns):
    if index % 2 == 1:
      l.append(-4 / i)
    else:
      l.append(4 / i)
  # step 4: 求和:
  return reduce(lambda x, y: x + y, l)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

