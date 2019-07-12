#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack quack.' # data in the form of variables with values
    movement = 'Walks like a duck.'

    def quack(self): # methods, functions available for this class
        print(self.sound)

    def move(self): 
        print(self.movement)
        # You'll notice that the first parameter of a method is always self.
        # Self is not a keyword. You can actually name that first parameter
        # whatever you want, but self is traditional
        # self is a reference to the object, not the class. So when an object
        # is created from the class, self will reference that object.
        # And then everything that references anything defined in the class 
        # is dereferenced off of self to get the instantiated object version of it.
        # And the period operator is used to dereference the object.
        
        # And the same is true outside of the class.
def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__': main()
