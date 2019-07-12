#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    
    # It's very easy to create a new sequence from the values in
    # another sequence
    
    # I really like this syntax
    seq2 = [x * 2 for x in seq] # Creates new seq by doubling the values
    
    # This next sequence will only use values not divisible by 3
    seq3 = [x for x in seq if x % 3 != 0]
    
    # I can create a set of tuples
    # Each tuple in the list will have the number, and the num squared
    seq4 = [(x, x**2) for x in seq]
    
    # You can call functions as well
    from math import pi
    seq5 = [ round(pi, i) for i in seq] # Pi rounded to the i decimal place
    
    # You can even create a dictionary
    seq6 = { x: x**2 for x in seq} # for each, the key is x and the value is x squared
    
    # You can perform these operations on strings as well
    # The following will create a seq of all chars in 'superduper' that are not in 'pd'
    seq7 = {f'Not in pd: {x},' for x in 'superduper' if x not in 'pd'}
    
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
