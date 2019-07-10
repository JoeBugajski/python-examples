#! /usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = ( 1, 2, 3, 4, 5 )
print('x is {}'.format(x))
print(type(x))

# you can iterate through a collection and check the type
# of each item
y = [ 1, 'two', 3.0, [4, 'four'], 5 ]
print('y is {}'.format(y))
print(type(y))
for i in y:
    print('i is {}, and it is type {}'.format(i, type(i)))

# If we did an id check for those two tuples, we'd see that
# they have two different id's

print(id(x))
print(id(y))

# But if we checked the id of the actual values stored within 
# x and y at index 0, we'd see that their id's are exactly the same. 

print(id(x[0]))
print(id(y[0]))

# Why? The two tuples are stored within Python as two separate objects,
# but Python won't create two separate 1's(the value stored at 0 index). 
# Instead, Python stores 1 and uses that id in multiple places. Much more 
# efficient than creating a new 1 everytime someone uses it. 

# This will only work if the compared values actually share the same id
if x[0] is y[0]:
    print('yep')
else:
    print('nope')
    
# How do we check if a collection is an example of a tuple? 
# We have the isinstance operator for that

if isinstance(x, tuple):
    print('tuple')
elif isinstance(x, list):
    print('list')
else:
    print('nope')

if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('nope')