import math

from math_tools import *


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
