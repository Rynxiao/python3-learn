#!/usr/bin/env python3

from collections import Iterable, Iterator

print('\'abc\' is iterable?', isinstance('abc', Iterable))
print('[1, 2, 3] is iterable?', isinstance([1, 2, 3], Iterable))
print('123 is iterable?', isinstance(123, Iterable))

# 将列表装换为键值对
print('列表[\'A\', \'B\', \'C\']转化为键值对形式，并且进行遍历')
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

print('遍历[(1, 1), (2, 4), (3, 9)]')
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)

# 迭代器
# from collections import Iterator

print('[] is Iterator?', isinstance([], Iterator))
print('{} is Iterator?', isinstance({}, Iterator))
print('(x for x in range(10)) is Iterator?', isinstance((x for x in range(10)), Iterator))
print('\'abc\' is Iterator?', isinstance('abc', Iterator))

# 将可迭代的对象转换为Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))


