#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Set is an unordered list, with no duplicate elements, in curly brackets
# in the examples below, a and b are sets of all the unique chars in each string

def main():
    a = set("We're gonna need a bigger boat.") 
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a) # If you really want them sorted, you can do print_set(sorted(a))
    print_set(b) # otherwise, they'll be in a different order every time you run
    # But if you really wanted an ordered list, you'd use list
    
    # For the most parts, you'd use a set to compare two or more collections
    
    # for example, I can check for the members that are in set a but not in set b
    # by using the minus operator as seen here:
    print('''
          
          a - b?
          
          ''')
    print_set(sorted(a - b))
    
    # I can find the members that are in set a or set b or both by using the vertical 
    # bar operator and that's all of the members that are in one or both of the sets.
    
    print('''
          
          a, b, or both?
          
          ''')
    print_set(sorted(a | b)) # use the vertical bar operator
    
    # Or I can look for the exclusive or using the caret operator.
    # So that's a or b, but not both
    
    print('''
          
          a or b, but not both
          
          ''')
    print_set(sorted(a ^ b))
    
    # Or I can look for only the members that are in both
    
    print('''
          
          both a and b
          
          ''')
    print_set(sorted(a & b))
    
def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
