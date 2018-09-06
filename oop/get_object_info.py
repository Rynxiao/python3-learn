#!/usr/bin/env python3

print(type(123))
print(type(str))
print(type(None))

print(type(abs))

print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

import types
def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# isinstance

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir
print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())
print('ABC'.lower())

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

print('hasattr, obj, x', hasattr(obj, 'x'))
print('hasattr, obj, y', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('hasattr, obj, y', hasattr(obj, 'y'))
print('getattr, obj, y', getattr(obj, 'y'))

# AttributeError: 'MyObject' object has no attribute 'z'
# getattr(obj, 'z')

# getattr default

print('getattr default, obj, z', getattr(obj, 'z', 404))
print('hasattr, obj, power', hasattr(obj, 'power'))
print('getattr, obj, power', getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())










