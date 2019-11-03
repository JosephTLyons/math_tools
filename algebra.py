import math


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_x_intercept_of_line(self):
        return (-self.b / self.a)

    def intersection(self, other_line):
        if self.a == other_line.a:
            if self.b == other_line.b:
                raise ValueError("Lines are equal")

            else:
                raise ValueError("The lines do not intersect")

        x = (other_line.b - self.b) / (self.a - other_line.a)
        y = (self.a * x) + self.b

        return (x, y)


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
