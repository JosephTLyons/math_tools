import math


class Line:
    def __init__(self, slope, y):
        self.slope = slope
        self.y = y

    def get_x_intercept_of_line(self):
        return (-self.y / self.slope)

    def intersection(self, other_line):
        if self.slope == other_line.slope:
            if self.y == other_line.y:
                raise ValueError("Lines are equal")

            else:
                raise ValueError("The lines do not intersect")

        x = (other_line.y - self.y) / (self.slope - other_line.slope)
        y = (self.slope * x) + self.y

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
