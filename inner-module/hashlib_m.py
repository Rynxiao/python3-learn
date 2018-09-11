#!/usr/bin/env python3

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in pyhton hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('pyhton hashlib?'.encode('utf-8'))
print(md5.hexdigest())