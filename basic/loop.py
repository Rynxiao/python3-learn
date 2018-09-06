#!/usr/bin/env python3

# for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print('for in', name)

# sum
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x
print('for sum', sum)

# range
print(list(range(0, 11)))

# while
sum2 = 0
n = 99
while n > 0:
	sum2 = sum2 + n
	n = n - 2
print('while sum', sum2)

# break
m = 1
while m <= 100:
	if m > 10:
		break
	print(m)
	m = m + 1
print('END')

# continue
k = 0
while k < 10:
	k = k + 1
	if k % 2 == 0:
		continue
	print(k)

