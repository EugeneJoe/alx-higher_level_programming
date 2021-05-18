# Classes and Objects

## Introduction

The files in this directory demonstrate how to define classes in python 3 and
how to instantiate instances of a class to create objects.
They demonstrate the basic principles of Object-Oriented Programming such as
1. Data Encapsulation
2. Information hiding
3. Data Abstraction
executed in the pythonic way.

## 0-square.py

Define an empty class called Square.

## 1-square.py

Define a class Square based on 0-square.py that has a private attribute
called size.

## 2-square.py

Define a class Square based on 1-square.py that also has an __init__ method
that instantiates the size attribute that checks for the following:
1. If the argument passed is not an integer, a TypeError exception is raised
   with the message "size must be an integer"
2. If size is less than 0, raise a ValueError exception with the message
   "size must be >= 0"

## 3-square.py

Define a class Square based on 2-square.py that:
1. Has a default value of 0 for the size attribute
2. Has a public instance method called "area" that returns the square's area

## 4-square.py

Define a class Square based on 3-square.py that:
1. Has a property size that retrieves the value of the size attribute
2. Has a property setter size that sets the value of the private attribute size

## 5-square.py

Define a class Square based on 4-square.py that:
1. Has a public instance method called "my_print" that prints in stdout the
   square with the character '#'. If size is equal to 0,, ,print an empty line.

## 6-square.py

Define a class Square based on 5-square.py that:
1. Has a private instance attribute called position that is a tuple of 2
   positive integers.
2. Has a property setter position that checks that the tuple is of the right
   type. If not, raise a TypeError exception with the message
   "position must be a tuple of 2 positive integers".
3. Use position in the my_print method. If position[1] > 0, don't fill lines
   by spaces.
