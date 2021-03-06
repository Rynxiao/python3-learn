#!/usr/bin/env python3

# __str__, __repr__

class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__

print(Student('Michael'))
s = Student('Michael')
print(s)

# __iter__, __getitem__

class Fib(object):
	def __init__(self):
		# 初始化两个计数器a，b
		self.a, self.b = 0, 1

	def __iter__(self):
		# 实例本身就是迭代对象，故返回自己
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

for n in Fib():
	print(n)

print('Fib()[5]', Fib()[5])
print('Fib()[0:5]', Fib()[0:5])

# __getattr__

class Student(object):

	def __init__(self):
		self.name = 'Michael'

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())

class Chain(object):

	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __call__(self, path = ''):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)

# __call__

class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Ryn')
print(s())

# callable
print(callable(Student('Ryn')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))














