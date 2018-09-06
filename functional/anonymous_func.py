#!/usr/bin/env python3

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

f = lambda x: x * x
print(f)

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)