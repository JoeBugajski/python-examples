#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# This is a good example of how a generator works

def main():
    for i in inclusive_range(25): # you can feed this (start, stop, step)
        print(i, end = ' ')
    print()
# This version of range includes 0-25, not 0-24
# range is actually a generator
def inclusive_range(*args): # variable argument list
    numargs = len(args)
    start = 0 # default start val if no start arg
    step = 1 # default step val if no step arg
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0] # if 1 arg, that arg is assigned to stop
    elif numargs == 2:
        (start, stop) = args # if 2, args are assigned to start and stop
    elif numargs == 3:
        (start, stop, step) = args # if 3, args assigned to start, stop, step
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}') # 4 is right out

    # generator
    i = start
    while i <= stop: # this while loop continues until it hits stop val
        yield i # yield is like return except it's for a generator
        # It yields a value and then after it yields the value the 
        # function continues until it yields the next value.
        i += step

if __name__ == '__main__': main()
