#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# in python, everything is an object, including functions

def f1():
    print('this is f1')
    
f1() # ordinary function, nothing special

# I can say x equals f1 without the parenthesis and now 
# I'm assigning that function object to the variable x.

x = f1

# But everything is an object, so a variable is an object too
# and I can simply call the function f1 by calling x.

x()

# weird decorator tricks
def f3(f): # created a function
    def f4(): # that contains another function
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f4

@f3 # This is how you denote that you're about to define a decorator
def f5(): # When you call this function, it will be automatically wrapped in f3 decorator
    print('this is f5')
    
x = f3(f5)
x()
