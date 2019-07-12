#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# For a list of all the special method names, please refer to 
# https://docs.python.org/3/reference/datamodel.html
# Click on special method names in the left-side directory to see a whole
# bunch of them

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'
# Look at this method called type which serves as both a getter and a setter, 
# and so I call it a getter setter. You'll notice that the first argument to the 
# function is self, and that's what makes this a method and not just a plain function. 
# This is filled in automatically, when I call this method on the object, I don't 
# provide this argument. So I'll just provide one argument, and the fact that it's 
# being called on the method will provide the first argument, self. It's common to 
# name this argument self, although it's not required, you can name it whatever 
# you'd like. But it's a really good idea to always use the word self, because 
# it's traditional, and when people are reading your code, they'll know what it 
# means. So in this case, the second argument is t, and you notice it has a default 
# value of none, so if there is no value, or if it's none, then this if will fail 
# and it'll just return the value of None. If there is a value, then it'll go ahead 
# and it'll set type, before returning it. So that's what makes it a setter getter.
    def type(self, t = None):
        if t: self._type = t
        return self._type
    # You'll also notice that the object variables are named with a leading underscore, 
    # and this again is traditional. Python doesn't have private variables, and so 
    # there's no way to actually prevent somebody from using these. But this indicates 
    # that it's a private variable and it should not be set or retrieved outside of the 
    # setter getter.

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound
# you'll also notice this special method called str, with two underscores before and 
# two underscores after. We've seen this before, in our constructor init, with two 
# underscores before and two underscores after. So this is a specially-named method, 
# which provides the string representation of the object. And this allows us to print 
# it with simply this print and the object like that, without needing a special function, 
# like we had in the previous lessons.
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    a0.sound('bark') # if I take, say, a0 and I want to change its sound, I simply 
    # call the sound function and I change it to, say, a bark. And now, when I run 
    # this, you'll notice that fluffy says bark, instead of rwar, like it was 
    # initialized to. And that's because I have set this variable, using the 
    # setter getter for sound
    print(a0)
    print(a1)

if __name__ == '__main__': main()
