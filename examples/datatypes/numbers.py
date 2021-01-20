#!/usr/bin/env python3

# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller

"""Integers and Floats, Arithmetic Operators (Numbers)

Offers examples and notes on how to define and assign numbers across
Python, including arithmetic operators and tips and tricks for dealing
with integers and floats. Python supports int, floats, and complex.
"""


def arithmetic_operators(x, y):

    print(x + y)   # the sum (addition) of two numbers
    print(x - y)   # the difference (subtraction) of two numbers
    print(x * y)   # the product (multiplication) of two numbers
    print(x / y)   # the remainder (division) of two numbers
    print(x // y)  # the floor remainder (division) of two numbers
    print(x ** y)  # the exponent (multiple) of a number
    print(x % y)   # the modulus of a number


def comparison_operators():

    x, y = 3, 2
    print(f"x = {x}, y ={y}")

    print(x == y)  # Equal to, equality operator, True if both operands are equal
    print(x != y)  # Not equal, True if the operands are not equal to one another
    print(x > y)   # Greater than, True if left operand is greater than right
    print(x < y)   # Less than, True if left operand is less than right
    print(x >= y)  # Greater or equal to, True if left operand is greater than or equal to the right
    print(x <= y)  # Less than or equal to, True if left operand is less than or equal to the right


def logical_operators():

    x, y, = True, False
    print(f"x = {x}, y = {y}")

    print(x and y)  # and, True if both operands are true
    print(x or y)   # or, True if either of the operands is true
    print(not x)    # True if operand is false, compliments operand


def assignment_operators():

    x = 12      # = operator

    x += 12     # += operator (x = x + 5)
    x -= 12     # -= operator (x = x - 5)
    x *= 12     # *= operator (x = x * 5)
    x /= 12     # /= operator (x = x / 5)
    x //= 12    # //= operator (x = x // 5)
    x %= 12     # %= operator (x = x % 5)
    x **= 12    # **= operator (x = x ** 5)
    # x &= 12   # &= operator (x = x & 5)
    # x |= 12   # |= operator (x = x | 5)
    # x ^= 12   # ^= operator (x = x ^ 5)
    # x >>= 12  # >>= operator (x = x >> 5)
    # x <<= 12  # <<= operator (x = x << 5)


def numbers(x, y, z):

    print(x, y, z)

    num_int = x + x           # integers
    print(num_int)            # output: 8
    print(type(num_int))      # output: <class 'int'>

    num_float = y + y         # floats
    print(num_float)          # output: 5.4
    print(type(num_float))    # output: <class 'float'>

    num_complex = y + z       # complex numbers
    print(num_complex)        # output: (2.7+3j)
    print(type(num_complex))  # output: <class 'complex'>

    print(isinstance(num_int, int))      # returns true because int is an integer
    print(isinstance(num_int, float))    # returns false because int is not a float
    print(isinstance(num_int, complex))  # returns false because int is not complex


if __name__ == "__main__":
    arithmetic_operators(3, 2)
    assignment_operators()
    comparison_operators()
    logical_operators()
    numbers(4, 2.7, 3j)
