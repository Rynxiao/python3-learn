#!/usr/bin/env python3

# set
s = set([1, 2, 3])
print('set receive a list, s', s)

# not repeatal
notRepeatSet = set([1, 2, 2, 3, 3])
print('not repeat set', notRepeatSet)

# add
print('before add', s)
s.add(4)
print('after add', s)
s.add(4)
print('after add 4 again', s)

# remove
s.remove(3)
print('after remove 3', s)

# union
s1 = set([1, 2, 3])
s2 = set([1, 2, 4])
print('并集', s1 & s2)
print('交集', s1 | s2)

# with tuple
t = (1, 2, 3)
t1 = (1, 2, [3, 4])
s3 = set([t, t1, 5])
print('with tuple', s3)


