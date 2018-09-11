#!/usr/bin/env python3

import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

def safe_base64_decode(s):
  t_s = s.decode('ascii')
  if len(t_s) % 4 == 0:
    return base64.b64decode(s)
  else:
    left = 4 - len(t_s) % 4
    t_s = t_s + '=' * left
    b_s = t_s.encode('ascii')
    return base64.b64decode(b_s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
