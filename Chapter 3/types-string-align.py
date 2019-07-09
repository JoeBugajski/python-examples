#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = 8
b = 9
# x = f'seven {a} {b}'
# Same definition with left and right align added to args
x = f'seven {a:<9} {b:>9}'
print(f'x is {x}')
print(type(x))
