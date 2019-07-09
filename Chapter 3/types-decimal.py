#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
