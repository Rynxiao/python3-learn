#!/usr/bin/env python3

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# list len
len(classmates)

# 访问
print(classmates[0])

# 反向索引
print(classmates[-1])

# append
classmates.append('Adam')
print(classmates)

# 删除末尾
last = classmates.pop()
print(classmates)

# 删除指定位置的元素
spcial = classmates.pop(1)
print(classmates)

# 列表里面的不同元素
L = ['Apple', 123, True]
print(L)

# 嵌套LIST
l = ['python', 'java', ['asp', 'php'], 'scheme']
print(l)
print(len(l))
p = ['asp', 'php']
ll = ['python', 'java', p, 'scheme']
print(ll[2][1])

# 空列表
L1 = []
print(len(L1))

# 拼接
L2 = [1]
L3 = [2]
print(L2 + L3)


