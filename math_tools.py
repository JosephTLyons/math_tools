#!/usr/bin/env python3

import math


def quadratic(a, b, c):
    if a == 0:
        raise ValueError("Not a quadratic function")

    preliminary = (b ** 2) - (4 * a * c)

    if preliminary < 0:
        return []

    common_1 = math.sqrt(preliminary)
    common_2 = 2 * a

    x_1 = (-b + common_1) / common_2
    x_2 = (-b - common_1) / common_2

    if x_1 == x_2:
        return [x_1]

    return sorted([x_1, x_2])


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    total = 1

    while (n > 0):
        total *= n
        n -= 1

    return total


def fibonacci(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n < 2:
        return n

    total = 1
    next = 1
    last = 1

    while (n > 2):
        total = next + last
        last = next
        next = total
        n -= 1

    return total