#!/usr/bin/env python3

g = (x * x for x in range(10))
print(g)

print(next(g))
print(next(g))

for n in g:
	print(n)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

print(fib(6))

def generator_fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

print(generator_fib)
for n in generator_fib(6):
	print(n)

g = generator_fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 3
	print('step 3')
	yield 5

o = odd()
print(next(o))
print(next(o))
print(next(o))

def triangles():
	last = [1]
	while True:
		yield last	

		if len(last) == 1:
			last = [1, 1]
		else:
			N = []
			for i in range(len(last) - 1):
				N.append(last[i] + last[i + 1])

			N.insert(0, 1)
			N.append(1)
			last = N

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break






