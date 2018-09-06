#!/usr/bin/env python3

def now():
	print('2018-08-15')

f = now
f()

print('函数 now 的名字 __name__', now.__name__)
print('函数 f 的名字 __name__', f.__name__)

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def date():
	print('2018-08-15')

date()
print('date function\'s name', date.__name__)

def complex_log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@complex_log('execute')
def now2():
	print('2018-08-15')

now2()

# 显示被装饰之后的函数的真实名字
import time, functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def date():
	print('2018-08-15')

date()
print('date function\'s name', date.__name__)

def complex_log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@complex_log('execute')
def now2():
	print('2018-08-15')

now2()

def metric(fn):
	@functools.wraps(fn)
	def duration(*args, **kw):
		start = time.clock()
		r = fn(*args, **kw)
		end = time.clock()
		d = end - start
		print('%s executed in %s ms' % (fn.__name__, d))
		return r
	return duration

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')








