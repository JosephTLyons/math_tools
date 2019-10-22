import number_theory


class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def reduce(self):
        gcd = number_theory.euclids_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def get_fraction_tuple(self):
        return (self.numerator, self.denominator)

    def add(self, other_fraction):
        new_denom = number_theory.lcm(self.denominator, other_fraction.denominator)

        partial_num_1 = (new_denom // self.denominator) * self.numerator
        partial_num_2 = (new_denom // other_fraction.denominator) * other_fraction.numerator

        return Fraction(partial_num_1 + partial_num_2, new_denom)

    def subtract(self, other_fraction):
        other_fraction.numerator *= -1
        return self.add(other_fraction)

    def multiply(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_demoninator = self.denominator * other_fraction.denominator

        new_fraction = Fraction(new_numerator, new_demoninator)
        new_fraction.reduce()

        return new_fraction
