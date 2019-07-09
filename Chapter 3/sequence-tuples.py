#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# unlike lists, tuples are not mutable. They are bound in parentheses like this:
x = ( 1, 2, 3, 4, 5 )

# if you uncomment this next line and run the file:
# x[2] = 69
 
# you can see the error you'd get for trying to 
# alter an immutable tuple

# Tuples are arguably favorable to lists due to
# the immutability property. In general, it can
# be good to start with tuples by default, and 
# only swith to list brackets if you have a spe-
# cific reason you want to mutate values.

for i in x:
    print('i is {}'.format(i))
