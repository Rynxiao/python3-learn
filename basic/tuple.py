#!/usr/bin/env python3

# tuple
classmates = ('Michael', 'Bob', 'Tracy')
print('tuple', classmates)

# index
print('index', classmates[1])

# 空
t = ()
print('空', t)

# 一个元素的元组
t1 = (1,)
print('一个元素的元组', t1)

# 地址不变
t2 = ('a', 'b', ['A', 'B'])
t2[2][0] = 'X'
t2[2][1] = 'Y'
print('地址不变', t2)


