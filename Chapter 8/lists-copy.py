#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1])
    # Just like range, lists can take in beginning, end and step args
    print(game[1:5:2]) # This will skip every other game
    # You can search a list like this
    i = game.index('Paper') # This will return the index matching the arg
    print(game[i]) # We can then print the result like this
    # You can append an item to a list like this:
    game.append('Computer')
    # Or you can insert an item like this
    game.insert(0, 'Laser_Tag')
    # You can remove an item by value
    game.remove('Scissors')
    # remove an item from the end of a list when no args are passed
    x = game.pop() # pop returns the popped value
    print(f'value popped off: {x}')
    # you can also pass pop an index to pop off a particular index
    y = game.pop(3)
    print(f'value popped off by index: {y}')
    # del is also available for removing items
    # you can pass it just an index
    # pass it a second arg for the end of the slice
    # pass it a third arg for step size
    print_list(game)
    del game[3]
    # You can join list items while printing in the following way
    print(', '.join(game))
    # You can get the length of a list this way
    print(len(game))
    del game[1:2]
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
