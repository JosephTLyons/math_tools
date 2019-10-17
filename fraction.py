from number_theory import euclids_gcd


class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def reduce(self):
        gcd = euclids_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def get_fraction_tuple(self):
        return (self.numerator, self.denominator)

    def add(self, other_fraction):
        new_num = (self.denominator * other_fraction.numerator) + \
                  (self.numerator * other_fraction.denominator)
        new_demom = self.denominator * other_fraction.denominator
        new_fraction = Fraction(new_num, new_demom)
        new_fraction.reduce()
        return new_fraction
