#!/usr/bin/env python3

# power

def power(x): 
	return x * x

print('power(5) is', power(5))

# power n
def powerN(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print('5 ^ 3 = ', powerN(5, 3))

# default args
def defaultPower(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print('defaultPower(5) is', defaultPower(5))

# changeable args
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print('calc([1, 2, 3]) is', calc([1, 2, 3]))
print('calc((1, 3, 5, 7)) is', calc((1, 3, 5, 7)))

def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


print('calc(1, 2, 3) is', calc2(1, 2, 3))
print('calc(1, 3, 5, 7) is', calc2(1, 3, 5, 7))
print('calc(*[4, 5, 6]) is', calc2(*[4, 5, 6]))

# key args
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Bob', 35, city='Beijing'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print('extra', person('Jack', 24, **extra))

# define key args
def person1(name, age, *, city = 'Beijing', job):
	print(name, age, city, job)

print('define key args', person1('Jack', 24, job = 'Engineer'))
print('define key args must pass name', person1('Jack', 24, city = 'Beijing', job = 'Engineer'))

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print('f1(1, 2) = ', f1(1, 2))
print('f1(1, 2, c=3) = ', f1(1, 2, c=3))
print('f1(1, 2, 3, \'a\', \'b\') = ', f1(1, 2, 3, 'a', 'b'))
print('f1(1, 2, 3, \'a\', \'b\', x=99) = ', f1(1, 2, 3, 'a', 'b', x=99))
print('f2(1, 2, d=99, ext=None) = ', f2(1, 2, d=99, ext=None))

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print('f1(*args, **kw) = ', f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print('f2(*args, **kw) = ', f2(*args, **kw))






