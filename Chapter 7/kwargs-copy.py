#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Key-word args are list args that are dictionaries instead of tuples
# Allows your function to have a variable number of named arguments
def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

def kitten(**kwargs): # Note two asterisks. kwargs is conventional name
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()

# Another example of how to pass in kwargs
x = dict(Todd = 'Bingo', Mike = 'Pizza Boy', Jerry = 'racecar')
kitten(**kwargs)