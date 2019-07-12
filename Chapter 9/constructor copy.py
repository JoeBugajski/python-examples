#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# An instance of a class is called an object. It's creating by calling the 
# class itself as if it were a function.

# There's a special class method name called init, with double underscores 
# before and after, so those are two underscore characters. One and two, 
# both before and after the word init. And that's a special name for a class 
# function which operates as an initializer, or a constructor.

class Animal:
    def __init__(self, type, name, sound): # The first argument is always self
        # the others are object variables because they're never initialized 
        # until after the object is defined, so they don't exist in the class 
        # without having been constructed into an object. 
        self._type = type 
        self._name = name
        self._sound = sound
        # And you notice that 
        # the object variables all have an underscore at the beginning of the 
        # name. Again, this is traditional, and this discourages users of the 
        # object from accessing these variables directly.
        # Instead, you have these accessors, or getters, I call them getters, 
        # some people call them accessors.
    def type(self): 
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

# So the object is created by using the class name as if it were a function 
# name. And this calls the constructor
def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
