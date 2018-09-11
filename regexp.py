#!/usr/bin/env python3

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
  print('ok')
else:
  print('failed')

print('a b  c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,\;]+', 'a, b;;c  d'))

m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

def is_valid_email(addr):
  return re.match(r'[\w+\.]+?@[\w+\.]+', addr)

def name_of_email(addr):
  m = re.match(r'(<([^/>]+?)>)?([\s\w]+?)@[\w\.]+', addr)
  return m.group(3) if m.group(2) == None else m.group(2)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')