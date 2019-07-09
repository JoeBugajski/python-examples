#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# In Python, a collection in brackets like this is called a list
x = [ 1, 2, 3, 4, 5 ]

# Lists are mutable, so we can change list values like this
x[2] = 69
for i in x:
    print('i is {}'.format(i))
