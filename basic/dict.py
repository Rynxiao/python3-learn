#!/usr/bin/env python3

# dict/map
d = { 'Michael': 95, 'Bob': 75, 'Tracy': 85 }
print('dict Michael', d['Michael'])

# insert
d['Adam'] = 78
print('after append', d)

# overwrite
d['Jack'] = 90
print('before overwrite', d)

d['Jack'] = 88
print('after overwrite', d)

# is In dict
print('Thomas is in dict?', 'Thomas' in d)

# get
print('get Thomas None', d.get('Thomas'))
print('get Thomas -1', d.get('Thomas', -1))

# delete
print('before delete', d)
d.pop('Bob')
print('after delete', d)

print('list can not be a dict key')