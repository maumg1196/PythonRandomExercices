#All code you gonna code in the terminal or W.ide

"""NUMBERS
The first type is integer, Example:
1, 5, 9, 10

type(1)
type(5)

The second type is float, Example:
3.14, 5.13e-2, 62.07, 1.0

type(1.0)
type(3.14)
type(5.13e-2)

The third type is complex, Example:
2 + 1j, 4.18 + 5j, 9 + 2.17j

type(2 + 3j)
type(4.18 + 5j)

Strings
The text o character need to be in ' ' 
Example: 'Hello World'
type('Hello World')

Booleans
This are the text True and False
Example:
type(True)
type(False)

Warning: False is a boolean but false is not the same with True and true

Lists
This are arranges with this syntax name_of_list = []
Example:
new_list = [1, 3.14, True, "Hello World"]

type(new_list)

Tuples
Similar like list but the syntax instead of [] are ()
Example:
new_tuple = (2, 5.83, False, "Bye World")

type(new_tuple)

Differences between lists and tuples:
Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.

You can't add elements to a tuple. Tuples have no append or extend method as lists.
You can't remove elements from a tuple. Tuples have no remove or pop method as lists.
You can find elements in a tuple, since this doesn’t change the tuple.

Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a list is like having an implied assert statement that this data is constant, and that special thought (and a specific function) is required to override that.
Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.

There are some interesting articles on this issue, e.g. "Python Tuples are Not Just Constant Lists" or "Understanding tuples vs. lists in Python". The official Python documentation also mentions this ("Tuples are immutable, and usually contain an heterogeneous sequence ...").

Diccionaries
The diccionaries are similar like the tuples and list but this needs a key for the value as 'dictionary = {key: value}
Example:
new_ dict = {1: 1.34, 2: 'Hello World, 3: 9.28, 4: True}

type(new_dict)
"""
