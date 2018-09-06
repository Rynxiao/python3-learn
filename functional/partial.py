#!/usr/bin/env python3

import functools
int2 = functools.partial(int, base = 2)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000', base = 10))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))