#!/usr/bin/env python3

# slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('Names', L)
print('取前3个', L[0:3])
print('取前3个，忽略0', L[:3])
print('取1到3个', L[1:3])
print('负向切片，L[-2:-1]', L[-2:-1])

# 跳跃取数
L1 = list(range(100))
print('L', L1)
print('前10个数，每两个取一个，L[:10:2]', L1[:10:2])
print('所有数，每5个取一个，L1[::5]', L1[::5])

# 复制
print('复制，L1[:]', L1[:])

# tuple 操作
T = (0, 1, 2, 3, 4, 5)
print('T', T)
print('取前3个', T[:3])

# 字符串
S = 'ABCDEFG'
print('S', S)
print('取前3个', S[:3])
