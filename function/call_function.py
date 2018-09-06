#!/usr/bin/env python3

print('--- call function ---')

# abs
print('100 abs', abs(100))
print('-20 abs', abs(-20))
print('12.34 abs', abs(12.34))

# call abs function error
# abs(1, 2) # TypeError: abs() takes exactly one argument (2 given)
# abs('a') # TypeError: bad operand type for abs(): 'str'

# max
print('the max number of 1, 2, 3, 5, 9, 7 is', max(1, 2, 3, 5, 9, 7))

# type transform
print('int(12.34)', int(12.34))
print('float(\'12.34\')', float('12.34'))
print('str(1.23)', str(1.23))
print('bool(100)', bool(100))
print('bool(\'\')', bool(''))

# alias
a = abs
print('function name', a)

