#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Another type of sequence is range. 
# range takes in three possible arguments.
# If you're just passing one argument, that
# means you're just specifying 'end', or length
# of the range.

x = range(5)

for i in x:
    print('i is {}'.format(i))

# In the example below, we want to start 
# the range at 5, and continue to 10
# (start, end)

y = range(5, 10)

for i in y:
    print('i is {}'.format(i))

# In the next example, we want to start
# at 5 and continue to 50, skipping 5 each time
# (start, end, step-by)

z = range(5, 50, 5)

for i in z:
    print('i is {}'.format(i))

# Ranges are not mutable, like tuples
# But if you want a mutable range, you can simply
# wrap the range in a list like this:

a = list(range(5))
a[2] = 44
for i in a:
    print('i is {}'.format(i))