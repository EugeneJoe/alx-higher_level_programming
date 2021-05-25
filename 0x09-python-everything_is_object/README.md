# Everything is Object

## Introduction

In python, everything is an object, from the built-in types such as int, float,
string, list to user-defined types such as classes. This directory explores how
python works with mutable versus immutable types internally.

Mutable types - data types whose values can be changed without changing the
actual object being referred to by the variable name. They include:

    - int
    - float
    - string
    - tuple

Immutable types - data types whose values cannot be changed. Changing the value
a variable name refers to creates a new object. They include:

    - list
    - dictionary
    - class definitions and instances

One method of determining whether an object is mutable or not is by comparing
its ID before and after attempting to change its value.
