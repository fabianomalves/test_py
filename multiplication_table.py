#! /usr/bin/env python
"""
Print the multiplication table from 1 to 10.

multiplication table 1
1
2
3
...
__________

multiplication table 2
2
4
6
...
__________
"""
__version__ = "0.0.1"
__author__ = "Fabiano Alves"


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = list(range(1,11))

# Iterables

for number in numbers:
    print(f"Multiplication table {number}")
    for other_number in numbers:
        print(number * other_number)
    print ("_________________")
