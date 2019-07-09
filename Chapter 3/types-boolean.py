#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = True
# x = 7 < 8
x = None
print('x is {}'.format(x))
print(type(x))

# None evaluates as False
# 0 evaluates as False
# Empty string '' evaluates as false
# Pretty much anything else will evaluate as True

if x:
    print("True")
else:
    print("False")