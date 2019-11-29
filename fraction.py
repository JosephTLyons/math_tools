import number_theory


class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def reduce(self):
        gcd = number_theory.euclids_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other_fraction):
        new_denom = number_theory.lcm(self.denominator, other_fraction.denominator)

        partial_num_1 = (new_denom // self.denominator) * self.numerator
        partial_num_2 = (new_denom // other_fraction.denominator) * other_fraction.numerator

        return Fraction(partial_num_1 + partial_num_2, new_denom)

    def __sub__(self, other_fraction):
        other_fraction.numerator *= -1
        return self.__add__(other_fraction)

    def __mul__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_demoninator = self.denominator * other_fraction.denominator

        new_fraction = Fraction(new_numerator, new_demoninator)
        new_fraction.reduce()

        return new_fraction

    def __truediv__(self, other_fraction):
        return self.__mul__(Fraction(other_fraction.denominator, other_fraction.numerator))

    def __eq__(self, other_fraction):
        return self.numerator == other_fraction.numerator and self.denominator == other_fraction.denominator

    def evaluate(self):
        return self.numerator / self.denominator
