"""
Task 8
1. implement the Vector(x, y) class with operations
of addition, subtraction and multiplication by a number
"""

import numpy as np

lst1 = [10, 20, 30, 40, 50]
lst2 = [1, 2, 3, 4, 5]

x = np.array(lst1)
y = np.array(lst2)


def vector_addition(x, y):
    return print(x + y)


def vector_subtraction(x, y):
    return print(x - y)


def vector_multiplication(x, y):
    return print(x * y)


vector_subtraction(x, y)
vector_multiplication(x, y)
vector_addition(x, y)

