#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string & encoded

print('包含中文的str')

print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')

x = b'ABC'
print(x)

# encode
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

# decode
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# decode error
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
# decode error ignore
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 字符len
print(len('ABC'))
print(len('中文'))

# 字节len
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

# 格式化
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
