#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = ( 1, 2, 3, 4, 5, 0 )
y = len(x) # length of x
z = list(reversed(x)) # x tuple reversed, and turned into a list
print(x)
print(y)
for i in z:
    print(i)

# You can also add the tuple values like so
a = sum(x)
print(a)
# You can also give the sum a starting value, and the values will be added to it
b = sum(x, 10)
print(b)
# There's a max() function and a min() function
c = (f'Maximum value in x: {max(x)}', f'Minimum value in x: {min(x)}')
print(c)
# any() will check if any of the values are true
d = any(x)
print(d)
# all() will check if all values are true
e = all(x)
print(e)
# There's an interesting zip() function
f = (1, 2, 3, 4, 5)
g = (6, 7, 8, 9, 10)
h = zip(f, g)
for a, b in h: print(f'{a} - {b}')
# enumerate() works like this
j = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(j): print(f'{i}: {v}')