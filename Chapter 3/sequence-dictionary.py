#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A dictionary is a searchable set of key-value pairs.

x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
for i in x:
    print('i is {}'.format(i))

# The above will only give us the keys.
# If we want to print key-value pairs, 
# we can do this:

y = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
for k, v in y.items():
    print('k: {}, v: {}'.format(k, v))