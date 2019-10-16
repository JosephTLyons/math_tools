#!/usr/bin/env python3

import math


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    total = 1

    while n > 0:
        total *= n
        n -= 1

    return total


def fibonacci(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n < 2:
        return n

    total = 0
    previous_one = 1
    previous_two = 0

    while n >= 2:
        total = previous_one + previous_two
        previous_two = previous_one
        previous_one = total
        n -= 1

    return total


def euclids_gcd(a, b):
    remainder = 1

    if a == b:
        return a

    while remainder != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def reduce_fraction(a, b):
    gcd = euclids_gcd(a, b)
    return (a / gcd, b / gcd)
