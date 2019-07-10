#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # You can just create a dictionary like this:
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #    'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    
    # You can also create a dictionary using the dictionary constructor
    # This looks a bit cleaner
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr', giraffe = 'I am giraffe!',     dragon = 'rawr')
    # Keys and Values can be any type
    # keys and values are immutable, so to alter values you have to create
    # a new seq, either a dictionary or some other seq
    # items() is a good method for printing out key value pairs
    print('''
          
          Key-Value pairs: 
          
          ''')
    for k, v in animals.items(): print(f'{k}: {v}')
    # this returns the same as below:
    # print_dict(animals)
    # You can also print keys like this:
    print('''
          
          Just keys: 
          
          ''')
    for k in animals.keys(): print(k)
    # Same goes for values
    print('''
          
          Just values: 
          
          ''')
    for v in animals.values(): print(v)
    
    # A dictionary is indexed by its keys, so you can access values 
    # by simply calling dictionary['key']
    print(animals['puppy'])
    
    # You can search for a key in a dictionary like so:
    print('lion' in animals) # This way will return True
    print('Found it!' if 'lion' in animals else 'nope!') # Return specified strings
    
    # If you try to access a key directly that doesn't exist, you'll get a KeyError
    # That's why it's probably a better idea to use a ternary as above
    # Or you can use this get() method below:
    print(animals.get('godzilla')) # Returns None instead of error
    
    # You can add an item to a dictionary like so:
    animals['monkey'] = 'haha'
    print(animals['monkey'])
    
def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
