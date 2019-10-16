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


def intersection(a_1, b_1, a_2, b_2):
    if a_1 == a_2:
        if b_1 == b_2:
            raise ValueError("Lines are equal")

        else:
            raise ValueError("The lines do not intersect")

    x = (b_2 - b_1) / (a_1 - a_2)
    y = (a_1 * x) + b_1

    return (x, y)


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


def are_coprimes(a, b):
    return euclids_gcd(a, b) == 1


def reduce_fraction(a, b):
    gcd = euclids_gcd(a, b)
    return (a / gcd, b / gcd)


def get_first_prime_factor(x):
    upper_limit = int(math.sqrt(x))

    for possible_factor in range(2, upper_limit + 1):
        if x % possible_factor == 0:
            return possible_factor

    return None


def get_prime_factors(x):
    prime_list = []
    first_factor = get_first_prime_factor(x)

    if first_factor is None:
        return []

    while first_factor is not None:
        prime_list.append(first_factor)
        x /= first_factor
        first_factor = get_first_prime_factor(int(x))

    if len(prime_list) != 0:
        prime_list.append(x)

    return prime_list


# def is_prime(n):
