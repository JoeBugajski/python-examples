#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Functions allow variable-length argument lists
def main():
    kitten('meow', 'grrr', 'purr')
# We treat it as a sequence, actually a tuple
def kitten(*args): # It's denoted as *args. args is the conventional name
    if len(args): # If the length of args is greater than zero
        for s in args:
            print(s) # If len(args), print all the items in the tuple
    else: print('Meow.') # otherwise print meow

if __name__ == '__main__': main()

# You can call the kitten function like this:
x = ('hiss', 'howl', 'roar', 'screech')
kitten(*x) # note the star