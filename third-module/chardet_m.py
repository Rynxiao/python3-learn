#!/usr/bin/env python3

import chardet

print(chardet.detect(b'Hello, world!'))

data = '天王盖地虎,小鸡炖蘑菇'.encode('gbk')
print(chardet.detect(data))

data2 = '你好中国'.encode('utf-8')
print(chardet.detect(data2))

data3 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data3))