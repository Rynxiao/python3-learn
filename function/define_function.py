#!/usr/bin/env python3

# define function
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print('def my_abs', my_abs(-99))

# 空函数
def nop():
	pass

print('空函数，啥也没干', nop())

# 参数检查
# print(my_abs('A'))

# my other abs function
def my_abs2(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

# print(my_abs2('a'))

# 返回多个值
import math
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print('返回多个值', x, y)
r = move(100, 100, 70, math.pi / 6)
print('返回的是一个tuple', r)

