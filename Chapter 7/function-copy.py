#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# In functions, we use parentheses to pass variables

def main():
    kitten(5, 6)

# All python functions return something, even if it just returns None
# You'll notice when kitten is called above, it's not passing enough 
# arguments to satisfy the variables defined in kitten. This will throw 
# a TypeError: kitten() missin 1 required positional argument: 'c'

# The way around this is to define a default value for c, as below:
def kitten(a, b, c = 10):
    print(f'Meow. a: {a}, b: {b}, c: {c}')
    # This default value can be overridden by passing a value on function call.

# It's probably best practice to give all vars a default value if you're giving
# one a default value. The rule is that any vars with default values have to
# be at the end of the list. For example, this will throw an error:
# def monkey(a, b, c = 10, d):
#    print(a, b, c, d)
# In fact, my linter wouldn't even let me do it. The error you get is a 
# SyntaxError: non-default argument follows default argument

# You've seen this line a lot:

if __name__ == '__main__': main()

# Here's what's happening with this line.
# When a python program starts to execute, it sets a few special variable, 
# __name__ is one of them. It contains the value __main__ if it’s the main 
# program being executed. But it won’t have the value as __main__ being set, 
# if it’s being imported and executed, since it’s not the main program when 
# imported.
