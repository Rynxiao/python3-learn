#!/usr/bin/env python3

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax  + n
		return ax
	return sum

f = lazy_sum(1, 43, 5, 7, 9)
print(f())

def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def createCounter():
	count = 0
	def counter():
		nonlocal count
		count = count + 1
		return count
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

