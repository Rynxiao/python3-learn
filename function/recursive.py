#!/usr/bin/env python3

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print('fact(1)', fact(1))
print('fact(10)', fact(10))

# 尾递归调用
def fact2(n):
	return fact_iter(n , 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print('尾递归调用 fact2(20)', fact2(20))

# 汉诺塔
def hanoi(n, a, b, c):
	# 如果a只有1盘子
	if n == 1:
		# 直接把盘子从a移到c
		print(a, '-->', c)
	# 如果a有n个盘子(n > 1)，那么分三步
	else:
		# 先把上面n-1个盘子，借助c，从a移到b
		hanoi(n - 1, a, c, b)
		# 再把最下面的1个盘子，借助b，从a移到c
		hanoi(1, a, b, c)
		# 最后把n-1个盘子，借助a，从b移到c
		hanoi(n - 1, b, a, c)

hanoi(4, 'A', 'B', 'C')
