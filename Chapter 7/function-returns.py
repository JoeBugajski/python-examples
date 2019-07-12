#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# In Python, there is no distinction between a function and a procedure
# All functions return a value. The following demonstrates this rule:

def main():
    x = kitten() # Assign the return value from kitten to a variable
    print(type(x), x) # print that, along with its type.
    # Print is like console.log(), and not a real return value
    # So this function would actuall print <class 'NoneType'> None
    # The return value is None.
    # if there's no return statement, or an empty return statement,
    # a function returns none.
    # uncomment line 18 to add a return statement, and run again
    # with return statement added, terminal says <class 'int'> 42
def kitten():
    print('Meow.')
    return 42
if __name__ == '__main__': main()
