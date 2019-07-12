#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Now you'll notice that I had these three parameters, and I don't have an 
# easy way of really remembering the order of them
# so a lot of times instead, somebody will do it this way. 

# We'll use "kwargs", 
# and then each of these can be "kwargs" sub type, and name
# you can also assign default values if no kwargs are pass on instantiation
class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'

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

# Then down here, you'd assign the args in the following way. This is a bit
# easier to understand
def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type = 'velociraptor', name = 'veronica', sound = 'hello'))

if __name__ == '__main__': main()
