#! /usr/bin/env python
"""
Print the multiplication table from 1 to 10.

---multiplication table 1---
        1 X 1 = 1
        2 X 1 = 2
        3 X 1 = 3
...
############################

multiplication table 2
        2 X 1 = 2
        2 X 2 = 4
        3 X 2 = 6
...
############################
"""
__version__ = "0.1.1"
__author__ = "Fabiano Alves"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = list(range(1,11))

# Iterables

for number_1 in numbers:
        print("{:-^18}".format(f"Multiplication Table {number_1}"))
        print()
        for number_2 in numbers:
            result = number_1 * number_2
            print("{:^18}".format(f"{number_1} X {number_2} = {result}\n"))
        print("#" * 23)
